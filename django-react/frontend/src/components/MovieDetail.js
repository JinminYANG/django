import PropTypes from "prop-types";
import {Link} from "react-router-dom";
import styles from "./MovieDetail.module.css";
import {FaStar} from "react-icons/fa";
import {useState} from "react";
import RatingStar from "./RatingStar";

function MovieDetail({coverImg, title, description, rating, genres}) {
    return (
        <div className={styles.content}>
            <img src={coverImg} alt={title}/>
            <h1>{title}</h1>
            <p>desc: {description}</p>
            <ul>
                {genres.map((g) => (
                    <li key={g}>{g}</li>
                ))}
            </ul>
            <div>
                rating: <RatingStar
                number={rating}
            />
            </div>

            <hr/>
            <Link to={"/"}>Home</Link>
        </div>
    );
}


MovieDetail.propTypes = {
    coverImg: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    rating: PropTypes.number.isRequired,
    genres: PropTypes.arrayOf(PropTypes.string).isRequired
};


export default MovieDetail;