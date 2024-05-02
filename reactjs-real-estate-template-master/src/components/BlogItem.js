import {Link} from "react-router-dom"

const BlogItem = ({title,link}) => {
    return (
        <div className="col-lg-4">
            <div className="blog-item">
                <div className="blog-img">
                    <img src="/img/product1.jpeg" alt="product" className="w-100" />
                </div>
                <div className="blog-content">
                    <h2 className="blog-title"><Link to={`/blog/${link}`}>{title}</Link></h2>
                    <div className="blog-info">
                        <div className="blog-info-item"><i className="far fa-calendar-alt "></i><span>29.04.2024</span></div>
                        <div className="blog-info-item"><i className="far fa-comments"></i><span>0 Comments</span></div>
                    </div>
                    <div className="blog-text">
                    서울숲 트리마제
                                </div>
                </div>
            </div>
        </div>
    )
}

export default BlogItem