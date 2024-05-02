import Slider from "react-slick";
import Title from "./Title"
import ReferenceItem from "./ReferenceItem"

const References = () => {
    const title = {
        text: "최근 방문한 집",
        description: "내가 최근에 확인한 집이에요"
    }
    const settings = {
        infinite: true,
        speed: 1500,
        slidesToShow: 5,
        slidesToScroll: 1,
        autoPlay: true,
        arrows: false,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: false
                }
            },
            {
                breakpoint: 800,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: false
                }
            }
        ]
    };
    return (
        <section className="section-references">
            <div className="container">
                <Title title={title.text} description={title.description} />
                <div className="row">
                    <div className="col-lg-12">
                        <Slider {...settings}>
                            <ReferenceItem />
                            <ReferenceItem />
                            <ReferenceItem />
                            <ReferenceItem />
                            <ReferenceItem />
                            <ReferenceItem />       
                        </Slider>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default References;