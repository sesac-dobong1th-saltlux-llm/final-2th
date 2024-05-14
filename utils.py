import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta
from openai import OpenAI
from langchain.memory import ConversationSummaryBufferMemory
from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.tools.retriever import create_retriever_tool
from langchain_core.prompts import ChatPromptTemplate

# api key 설정
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
bing_custom_key = os.getenv('BINGCUSTOM_API_KEY')

history_summarize_api = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
memory = ConversationSummaryBufferMemory(llm=history_summarize_api, max_token_limit=100, return_messages=True)

# 대화 기록 요약 
def summarize_GPT_api(serch_result, response, keywords):
    summarize_prompt = [
        {"role": "system", "content": f"""너는 세가지의 정보를 입력받아서 정리해주는 최종 출력을 처리하는 AI야.
        응답 생성 단계와 최종 출력 양식을 참고하여 응답해줘. 최종 응답은 양식에 맞게만 응답합니다. 다른 텍스트는 생성하지마세요.
    
        최종 출력 양식 :

            사용자님의 요구조건에 맞는 아파트 중에서 추천해드릴 수 있는 매물은 dong_name 에 위치한 articleName 입니다.
            
            1. gu_name  dong_name 에 위치한 articleName
            - 매물명 : gu_name dong_name articleName
            - 층수 : floorInfo
            - 방향 : direction
            - 매매가 : rentPrc dealOrWarrantPrc
            - 특징 : articleFeatureDesc (특징은 그대로 추출하지 말고 문장으로 자연스럽게 다듬으세요)
            - 태그 : tagList
            - 추천 이유 : 

            매물 시세 : 

            뉴스 정보 : 
        ----------------------------------------------------------
        응답 생성 단계 :
            1. {response} 에서 전달 받는 매물 정보를 바탕으로 다음 단계에 따라 응답을 생성하세요.
                1-1. 만약 위에서 전달받은 매물 정보가 없다면 {keywords}를 활용해 차선책 매물을 제시하세요.
            2. 추천 이유에는 각 매물 정보를 종합하여 합리적으로 이유를 설명하여 사용자를 납득시키세요.
            3. 매물 시세에는 매물의 부동산 시세 언급하고, 매물의 가격이 부동산 시세에 비하여 얼마나 비싸거나 싼지 근거를 들며 설명합니다
            4. 뉴스 정보에는 {serch_result}에서 얻은 정보를 바탕으로 매물정보와 관련해서 사용자의 조건과 매물 정보가 일치한지 추천 근거를 설명하고 요약하세요.
            그 다음 추천에 대한 개인적인 견해도 추가하세요. 제목과 링크도 넣으세요.
            5. 프롬프트에서의 최종 출력 양식에 따라 응답하세요.
            """
        },

        {"role": "user", "content": f"""{serch_result}, {response}"""}
        ]
    sub_lm = OpenAI()
    summary = sub_lm.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages= summarize_prompt,
    temperature = 0.4,
    top_p=0.85
    )

    final_response_text = summary.choices[0].message.content
    return final_response_text # 최종 응답문 출력

def bing_news_search(user_requests, max_requests, bing_custom_key):
    custom_config_id = '244eaf6d-2328-4f47-ae58-8268db9d2b1f'
    endpoint = f'https://api.bing.microsoft.com/v7.0/custom/search'
    headers = {'Ocp-Apim-Subscription-Key': bing_custom_key}
    params = {
        'q': f'2024 서울 {user_requests} 아파트 뉴스 기사',
        'customconfig': custom_config_id,
        'mkt': 'ko-KR',
        'count': max_requests,
    }
    
    response = requests.get(endpoint, headers=headers, params=params)
    search_results = response.json()
    
    one_week_ago = datetime.now() - timedelta(days=90)
    output_results = []

    # 결과를 검사하고 결과가 있는지 확인
    if 'webPages' in search_results and 'value' in search_results['webPages']: 
        for result in search_results['webPages']['value']:
            date_string = result['dateLastCrawled']
            formatted_date_string = date_string[:-4] + date_string[-1]
            article_date = datetime.strptime(formatted_date_string, '%Y-%m-%dT%H:%M:%S.%fZ')
            if article_date >= one_week_ago:
                article_info = {
                    "title": result['name'],
                    "url": result['url'],
                    "snippet": result['snippet'],
                    "published_on": article_date.strftime('%Y-%m-%d')
                }
                output_results.append(article_info)

    if output_results:
        for article in output_results:
            print("{:<100} {:<100} {:<150} {:<15}".format(
            article['title'], article['url'], article['snippet'], article['published_on']))
            print("-" * 365)

    return output_results # 뉴스 기사 리스트중 첫번째 뉴스 반환


def keyword_extraction(user_requests):
    key_extraction_prompt = [
        {"role": "system", "content": """입력 받은 매물 정보에서 지역명(강북구. 강남구 성북동, 대치동 등)만 추출해서 인터넷 검색에 알맞게 키워드를 추출해줘. 추출한 키워드만 말해줘."""},
        {"role": "user", "content": f"{user_requests}에서 지역명 하나만 추출하고 나머지는 무시해. 그 키워드만 반환해."}
        ]
    Keyword_extraction_api = OpenAI()
    extraction = Keyword_extraction_api.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages= key_extraction_prompt,
    temperature = 0 # 키워드 추출은 창의성이 있으면 안되기 때문에 0으로 설정
    )

    keyword_text = extraction.choices[0].message.content

    return keyword_text # 최종적으로 키워드만 반환

# 대화 내용을 저장
def save_history(user_input, response):
    memory.save_context(
        inputs={"human": user_input},
        outputs={"ai": response}
    )
    
#대화 이력을 load. 시스템 메세지와 사용자 메세지 둘 다 가져옴
def load_history():
    history_data = memory.load_memory_variables({})
    history = history_data.get("history", [])
    return " ".join([f"{SystemMessage}: {HumanMessage}" for turn in history])
