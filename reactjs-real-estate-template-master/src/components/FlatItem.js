import { Link } from "react-router-dom";

const FlatItem = ({slug}) => {
    return (
        <div className="text-center col-lg-4 col-12 col-md-6 ">
            <div className="item">
                <div className="item-image">
                    <img className="img-fluid" src="/img/product1.jpeg" alt="flat" />
                </div>
                <div className="item-description">
                    <div className="d-flex justify-content-between mb-3">
                        <span className="item-title">자고싶다 자고싶다 자고싶다 자고싶다 자고싶다 자고싶다 자고싶다</span>
                        <span className="item-price">100조</span>
                    </div>
                    <div className="item-icon d-flex alig-items-center justify-content-between">
                        <div>
                            <i className="fas fa-check-circle"></i> <span>확인된 매물</span>
                        </div>
                        <div>
                            <i className="fas fa-check-circle"></i> <span> 매매 </span>
                        </div>
                        <Link to={`/flat/${slug}`} className="item-title">
                            <button className="btn btn-detail">보기</button>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default FlatItem