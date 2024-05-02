import React from "react";
import ImageGallery from 'react-image-gallery';


const FlatDetail = () => {
    const images = [
        {
            original: '/img/product1.jpeg',
            thumbnail: '/img/product1.jpeg',
        },
        {
            original: '/img/banner.jpg',
            thumbnail: '/img/banner.jpg',
        },
        {
            original: '/img/product1.jpeg',
            thumbnail: '/img/product1.jpeg',
        },
    ];

    return (
        <div className="flat-detail">
            <div className="page-top">
                <div className="container">
                    <div className="row">
                        <div className="col-lg-12">
                            <h1 className="page-title">세부정보</h1>
                            <h2 className="page-description">이 집에 대해 조금 더 알아볼까요?</h2>
                        </div>
                    </div>
                </div>
            </div>
            <div className="container mt-5 mb-5">
                <div className="row">
                    <div className="col-lg-12">
                        <div className="fd-top flat-detail-content">
                            <div>
                                <h3 className="flat-detail-title">잠실 시그니엘 레지던스</h3>
                                <p className="fd-address"> <i className="fas fa-map-marker-alt"></i>
                                잠실의 최고급 오피스텔</p>
                            </div>
                            <div>
                                <span className="fd-price">65억</span>
                            </div>
                        </div>
                        <ImageGallery flickThreshold={0.50} slideDuration={0} items={images} showNav={false} showFullscreenButton={false} showPlayButton={false} />
                        <div className="row">
                            <div className="col-lg-8">
                                <div className="fd-item">
                                    <h4>설명</h4>
                                    <p>서울특별시 송파구 잠실역 롯데월드타워에 위치해 있는 롯데건설의 고급 오피스텔로 롯데물산에 따르면 대한민국 역대 주택 분양·매매 가격 기록을 경신했으며 시그니엘 레지던스 매매가는 최고 370억 원을 기록했다. 2022년에 롯데는 5년 만에 시그니엘 레지던스를 완판하는데 성공했다. 총 223세대로 롯데월드타워 42층부터 71층을 사용한다. 42층은 라운지로 입주민들을 위한 커뮤니티 시설(미팅룸, 파티룸)과 레지던스 카페, 피트니스룸, 실내 골프연습장 등이 갖춰져 있다. 44 ~ 58층, 61 ~ 71층이 세대층으로 구성되어 있으며 68, 69, 70, 71층은 복층 구조다. 공급면적은 237 ~ 1,227㎡이며 전용면적 기준으로는 133 ~ 829㎡이다. 3.3㎡당 분양가는 6,700만 원에서 1억 원이다. 실당 분양가는 42억 ~ 370억 원 정도이며 관리비는 3.3㎡ 당 25,000원 선으로 237㎡ 기준으로 월 120만 원이 청구된다. 물론 전기료, 수도세 등 공과금은 별도이며 입주 후 1년간은 관리비 혜택이 주어진다.</p>
                                </div>
                                <div className="fd-item fd-property-detail">
                                    <h4>집 구성</h4>
                                    <div className="row">
                                        <div className="col-lg-4">
                                            <span>주방: </span>
                                            <span>1</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <span>방: </span>
                                            <span>5</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <span>주방:  </span>
                                            <span>1</span>
                                        </div>
                                    </div>
                                    <div className="row">
                                        <div className="col-lg-4">
                                            <span>주방: </span>
                                            <span>1</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <span>방: </span>
                                            <span>5</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <span>주방:  </span>
                                            <span>1</span>
                                        </div>
                                    </div>
                                    <div className="row">
                                        <div className="col-lg-4">
                                            <span>주방: </span>
                                            <span>1</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <span>방: </span>
                                            <span>5</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <span>주방:  </span>
                                            <span>1</span>
                                        </div>
                                    </div>
                                </div>
                                <div className="fd-item fd-features">
                                    <h4>상세정보</h4>
                                    <div className="row">
                                        <div className="col-lg-4">
                                            <i className="fa fa-check"></i>
                                            <span>허위매물 없음</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>신축</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>엘베있음</span>
                                        </div>
                                    </div>
                                    <div className="row">
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>반려견 가능</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>주차장 있음</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <i className="fa fa-check"></i>
                                            <span>단기계약 가능</span>
                                        </div>
                                    </div>
                                    <div className="row">
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>전입 신고 가능</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>남향</span>
                                        </div>
                                        <div className="col-lg-4">
                                            <i className="fa fa-check" ></i>
                                            <span>친구랑 동거 가능</span>
                                        </div>
                                    </div>
                                </div>
                                <div className="fd-item">
                                    <h4>위치</h4>
                                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15105200.564429!2d37.538383!3d127.045083!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14b0155c964f2671%3A0x40d9dbd42a625f2a!2zVMO8cmtpeWU!5e0!3m2!1str!2str!4v1630158674074!5m2!1str!2str" width="100%" height="450" loading="lazy"></iframe>
                                </div>
                            </div>
                            <div className="col-lg-4">
                                <div className="fd-sidebar-item">
                                    <h4>최근 내가 본 항목</h4>
                                    <div className="recently-item">
                                        <img src="/img/product1.jpeg" alt="detail" width="50px" />
                                        <span>한남 더힐</span>
                                    </div>
                                    <div className="recently-item">
                                        <img src="/img/product1.jpeg" alt="detail" width="50px" />
                                        <span>서울숲 트리마제</span>
                                    </div>
                                    <div className="recently-item">
                                        <img src="/img/product1.jpeg" alt="detail" width="50px" />
                                        <span>잠실 시그니엘 레지던스</span>
                                    </div>
                                </div>
                                <div className="fd-sidebar-item">
                                    <h4>카테고리</h4>
                                    <ul className="category-ul">
                                        <li>카테고리 1</li>
                                        <li>카테고리 2</li>
                                        <li>카테고리 3</li>
                                        <li>카테고리 4</li>
                                        <li>카테고리 5</li>
                                    </ul>
                                </div>
                                <div className="fd-sidebar-item">
                                    <h4>최근 내가 찜한 집</h4>
                                    <div className="recently-item">
                                        <img src="/img/product1.jpeg" alt="detail" width="50px" />
                                        <span>한남 더힐</span>
                                    </div>
                                    <div className="recently-item">
                                        <img src="/img/product1.jpeg" alt="detail" width="50px" />
                                        <span>서울숲 트리마제</span>
                                    </div>
                                    <div className="recently-item">
                                        <img src="/img/product1.jpeg" alt="detail" width="50px" />
                                        <span>잠실 시그니엘 레지던스</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default FlatDetail