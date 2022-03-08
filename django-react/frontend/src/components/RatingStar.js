import ReactStars from "react-rating-stars-component";

function RatingStar({number}) {
    const firstExample = {
        count: 10,
        size: 25,
        value: number,
        isHalf: true,
        edit: false
    };

    return (
        <div>
            <ReactStars
                {...firstExample}
                emptyIcon={<i className="far fa-star"></i>}
                halfIcon={<i className="fa fa-star-half-alt"></i>}
                fullIcon={<i className="fa fa-star"></i>}
            />
        </div>
    );
}


export default RatingStar;