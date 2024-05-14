import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_community.vectorstores import FAISS
from utils import *
from dotenv import load_dotenv

load_dotenv()

bing_custom_key = os.getenv('BINGCUSTOM_API_KEY')

# 허깅 페이스의 임베딩 모델 load 
embedding_model = HuggingFaceEmbeddings(
    model_name = "snunlp/KR-SBERT-V40K-klueNLI-augSTS",
    model_kwargs = {'device' : 'cpu'},
    encode_kwargs = {'normalize_embeddings':True}
)

# 벡터스토어 검색 생성 로컬 경로를 통해 사전에 생성된 벡터스토어 로드
vector_store = FAISS.load_local('/home/ubuntu/HomeFit/FAISS/faiss', embedding_model, allow_dangerous_deserialization=True)

# 벡터 스토어 검색 알고리즘
retriver = vector_store.as_retriever(
    search_type='mmr',
    search_kwargs={'k': 3, 'lambda_mult': 0.80}
)

# 메인 GPT 모델
langchain_agent = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=1)

retriever_pool = create_retriever_tool(retriver, "FAISS_DB_system", description="아파트의 부동산 정보를 검색합니다.")

tools = [retriever_pool]

def question_answering(user_input):

    chat_history = load_history()

    if '추천' in user_input or '알려줘' in user_input:
        best_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """사용자의 입력에 따라 아래 응답 예시 양식과 단계에 따라 응답하세요.

                    응답 예시:
                        gu_name dong_name 에 위치한 articleName
                        매물명 : articleName
                        층수 : floorInfo
                        방향 : direction
                        거래 종류 : tradeTypeName (전세, 매매, 월세)
                        매매가 : (tradeTypeName 컬럼 값이 가 '전세' or '매매' == dealOrWarrantPrc , tradeTypeName in '월세' == rentPrc 가격을 기입하세요.)
                        특징 : articleFeatureDesc
                        태그 : tagList
                        --------------------------------------------------------------
                        응답 생성 단계 :
                            1.사용자의 요구 조건에 맞는 부동산 정보를 관련 문서에서 1개만 검색합니다. 사용자 질문은 "{input}"과 같습니다
                                    1-1. 매물 추천이 아닌 일반 요청이면 '일반 요청'이라고 다음 모델에 전달 만약 아파트 추천 요청이라면 다음 1-1-1 단계 실행합니다.
                                    1-1-1. 사용자가 매물 요청을 하면 vector store에서 매물을 검색 하여 매물 정보 출력합니다.
                                1-2. 매물이 없을 경우엔 ' ' 공백으로 응답. 절대 텍스트를 생성 하지마세요.
                            2. 먼저 gu_name 또는 dong_name에 맞는 articleName를 찾은 다음 나머지 조건도 맞는지 찾습니다.
                                2.1 만약 컬럼들 중 하나라도 사용자 {input}과 일치하지 않는다면 텍스트 말고 공백으로 응답을 마무리하세요.
                            2. tradeTypeName 컬럼은 전세, 매매, 월세를 나타내는 컬럼이므로 잘 분류하여 기입하세요.
                            3. 거래 종류(tradeTypeName)가 '전세' 또는 '매매' 라면 dealOrWarrantPrc, 월세라면 'rentPrc' 중 알맞은 가격을 매매가에 가격을 기입하세요.
                            4. 검색된 정보를 기반으로 사용자 질문에 적합한 행을 가져와서 응답합니다.
                            (gu_name, dong_name 컬럼은 지역명, articleName은 건물이름 입니다, dealOrWarrantPrc는 전세 / 매매 가격, rentPrc는 월세 가격입니다. 이 정보에 맞게 정보를 검색하세요.)
                            """
                ),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

        first_best_agent = create_tool_calling_agent(langchain_agent, tools, best_prompt) # 에이전트 생성
        forst_best_agent_pool = AgentExecutor(agent=first_best_agent, tools=tools, verbose=False, handle_parsing_errors=True)

        first_result = forst_best_agent_pool.invoke({"input": user_input})

        # 찾는 조건의 매물이 없을 경우
        if not first_result['output'].strip():
            second_best_keyword = keyword_extraction(user_input)

            sencond_best_search = bing_news_search(second_best_keyword, 3, bing_custom_key) 

            sencond_best_agent = create_tool_calling_agent(langchain_agent, tools, best_prompt)
            sendond_bst_agent_pool = AgentExecutor(agent=sencond_best_agent, tools=tools, verbose=False, handle_parsing_errors=True)
            sencond_result = sendond_bst_agent_pool.invoke({"input": f"{second_best_keyword} 아파트 추천해줘."})

            sencond_best_response = sencond_result['output']

            sencond_final_result = summarize_GPT_api(sencond_best_search , sencond_best_response, second_best_keyword)

            # 키워드로 5개 까지 검색
            save_history(user_input, sencond_best_response) # 채팅 내역에 사용자 입력값과 응답 저장
            return sencond_final_result # 대안 매물 응답
        else : 
            keyword = keyword_extraction(user_input)

            serch_result = bing_news_search(keyword, 3, bing_custom_key)  # 키워드로 5개 까지 검색

            sum_result = summarize_GPT_api(serch_result, first_result['output'], keyword) # 세가지 정보를 바탕으로 최종응답 후처리

            save_history(user_input, first_result['output']) # 채팅 내역에 사용자 입력값과 응답 저장

            return sum_result # 사용자 요구 조건에 맞는 응답 생성
    else :
        prompt = [
        {"role": "system", "content": "너는 부동산 추천 관련해서 도움을 주는 AI 홈핏이야. 사용자와 대화의 흐름을 파악해서 잘 대화해."
        },
        {"role": "user", "content": f"""{user_input}"""}
        ]
        talk_llm = OpenAI()
        talk = talk_llm.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages= prompt,
        temperature = 0.7,
        top_p=0.85
        )
    
        talk_responce_final = talk.choices[0].message.content

        return talk_responce_final