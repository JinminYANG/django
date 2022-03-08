import {useEffect, useState} from "react";
import styles from "./Home.module.css";
import Movie from "../components/Movie";

function Animation() {
    const [loading, setLoading] = useState(true);
    const [movies, setMovies] = useState([]);

    const getMovies = async () => {
        const json = await (
            await fetch(`https://yts.mx/api/v2/list_movies.json?genre=animation&sort_by=like_count`)).json();
        setMovies(json.data.movies);
        setLoading(false);
        console.log(json);
    };

    useEffect(() => {
        getMovies();
    }, []);

    return (
        <div className={styles.container}>
            {
                loading
                    ?
                    <div className={styles.loader}>
                        <span>Loading...</span>
                    </div>
                    :
                    <div>
                        <div className={styles.movies}>
                            {movies.map((movie) => (
                                <Movie
                                    key={movie.id}
                                    id={movie.id}
                                    year={movie.year}
                                    coverImg={movie.medium_cover_image}
                                    title={movie.title}
                                    summary={movie.summary}
                                    genres={movie.genres}
                                />
                            ))}
                        </div>
                    </div>
            }

        </div>
    )
}

export default Animation;