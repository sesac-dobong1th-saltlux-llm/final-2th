import Sidebar from "./Sidebar";

const BlogDetail = () => {
    return (
        <div className="container mt-4 mb-4">
            <div className="row">
                <div className="col-lg-8">
                    <div className="blog-detail">
                        <img className="w-100" src="/img/product1.jpeg" alt="product" />
                        <span className="blog-detail-category">매매</span>
                        <h1 className="blog-detail-title">용산구 한남 The Hill</h1>
                        <span className="blog-detail-date">29.04.2024</span>
                        <p className="blog-detail-content">
                        한남더힐은 한남동 매봉산 밑에 위치해 있으며 고도제한이 있다 보니 고층이 아닌 저층의 여러 동으로 이루어져 있다. 도로 하나를 두고 마주 보고 있는 유엔빌리지와 달리 한강 조망은 어렵지만, 강변북로의 소음과 번잡함으로부터 자유롭다. 또한, 아파트 한쪽으로 산이 둘러싸고 있어 접근하기 어려운 지역이라는 것이 상류층에게 플러스 요인이 되었다.
                        </p>
                        <h2 className="blog-detail-alttitle">특징</h2>
                        <p className="blog-detail-content">
                        아파트로 분류되지만 12층 이하 건물들로 구성되어 있다 보니 다른 아파트들보다 더 쾌적한 주거환경을 제공한다. 큰 평수일수록 층수가 낮아서 90~100평대는 고작 3~4층에 불과하다. 아파트 안에는 여러 예술 작품들이 설치되어 있으며 단지 곳곳에 산책할 수 있는 정원이 있다. 주차는 모두 지하주차장에 하도록 지어졌다. 주차 대수는 세대당 2.89대로 상당히 여유로운 편이다.
                        </p>
                        <h2 className="blog-detail-alttitle">편의시설 및 교통</h2>
                        <p className="blog-detail-content">
                        단지 중앙에 입주민용 커뮤니티 동이 있다. 1층에는 스크린 골프장, 수영장, 헬스클럽, 사우나가 있고 2층에는 카페, 독서실, 게스트하우스 등 여러 편의 시설들이 있다. 아파트 정문 상가 안에는 더 줌 아트센터와 신한은행 PWM 한남동 센터가 있다.
                        </p>
                    </div>
                </div>
                <Sidebar/>
            </div>
        </div>
    )
}
export default BlogDetail;