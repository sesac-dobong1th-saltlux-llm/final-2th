from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.utils import DistanceStrategy


loader = CSVLoader(
    file_path="/home/ubuntu/HomeFit/data/data.csv", 
    encoding='utf-8'
)

csv_data = loader.load()
text_splitter = RecursiveCharacterTextSplitter(separators=["\n"], chunk_size=1000, chunk_overlap=0)
all_splits = text_splitter.split_documents(csv_data)

embedding_model = HuggingFaceEmbeddings(
    model_name = "snunlp/KR-SBERT-V40K-klueNLI-augSTS",
    model_kwargs = {'device': 'cpu'},                # 모델 로드드
    encode_kwargs = {'normalize_embeddings':True}    # 벡터가 정규화되도록 지정하여 벡터 간의 거리 비교가 효율적
)

vector = FAISS.from_documents(
    documents = all_splits,
    embedding = embedding_model
)
vector.save_local('FAISS/faiss')