const About = () => {
    return (
        <section className="about">
            <div className="page-top">
                <div className="container">
                    <div className="row">
                        <div className="col-lg-12">
                            <h1 className="page-title">설명</h1>
                            <h2 className="page-description">나에게 딱 맞는 집 추천이란?</h2>
                        </div>
                    </div>
                </div>
            </div>
            <div className="page-content">
                <div className="container">
                    <div className="row">
                        <div className="col-lg-6">
                            <img src="/img/product1.jpeg" alt="product" className="w-100" />
                        </div>
                        <div className="col-lg-6">
                            <div className="about-item">
                                <div className="title">
                                    인공지능 추천이란?
                            </div>
                                <div className="about-text">
                                    지금껏 경험해보지 못한 최고의 경험! 인공지능이 당신에게 가자 딱 맞는 집을 찾아드립니다!
                            </div>
                                <div className="about-features">
                                    <p className="about-feature"><i className="fas fa-long-arrow-alt-right"></i>인기 매물</p>
                                    <p className="about-feature" ><i className="fas fa-long-arrow-alt-right"></i>급매물</p>
                                    <p className="about-feature"><i className="fas fa-long-arrow-alt-right"></i>단기거주</p>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default About