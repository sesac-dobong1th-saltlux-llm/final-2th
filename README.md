# 홈핏(HomeFit)
### 프로젝트 소개
사용자 요구 조건에 맞게 부동산 매물을 추천하는 AI 서비스

### 실행 안내
#### DB
* Amazon RDS 인스턴스 생성, 보안그룹 생성
* 인스턴스의 Public Host IP, 관리자명(기본값 `postgres`), DB명(기본값 `postgres`) 등 정보를 `database.py` 파일에 반영
* bash에 `psql -h [엔드포인트 주소] -U postgres`와 같이 입력

#### Frontend & Backend
* bash 환경에서 프로젝트 폴더로 이동하여 `uvicorn main:app --reload` 실행
* `localhost:8000`으로 접속
