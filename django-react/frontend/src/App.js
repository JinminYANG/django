import {useState, useEffect} from "react";
import {
    BrowserRouter as Router,
    Switch,
    Route,
} from "react-router-dom";
import Home from "./routes/Home";
import Detail from "./routes/Detail";
import Navbar from "./components/Navbar/Navbar";
import Update from "./routes/Update";
import Favorite from "./routes/Favorite";
import Animation from "./routes/Animation";
import SignIn from "./routes/SignIn";


function App() {
    // router를 render 해야 한다
    // router는 url을 보고 있는 컴포넌트이다

    return (
        <Router>
            <Navbar/>
            <Switch>
                <Route exact path="/" component={Home}/>
                <Route path="/movie/:id" component={Detail}/>
                <Route path="/update" component={Update}/>
                <Route path="/favorite" component={Favorite}/>
                <Route path="/animation" component={Animation}/>
                <Route path="/signin" component={SignIn}/>
            </Switch>
        </Router>
    );

    /*const [loading, setLoading] = useState(true);
    const [movies, setMovies] = useState([]);

    const getMovies = async () => {
        const response = await fetch(`https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year`);
        const json = await response.json();
        setMovies(json.data.movies);
        setLoading(false);
    };

    useEffect(() => {
        getMovies();
        /!*
        fetch(`https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year`)
            .then((response) => response.json())
            .then((json) => {
                setMovies(json.data.movies);
                setLoading(false);
            });
        *!/
    }, []);

    return (
        <div>
            {
                loading
                    ?
                    <h1>Loading...</h1>
                    :
                    <div>
                        {movies.map((movie) => (
                            <Movie
                                key={movie.id}
                                coverImg={movie.medium_cover_image}
                                title={movie.title}
                                summary={movie.summary}
                                genres={movie.genres}
                            />
                        ))};
                    </div>
            }

        </div>
    );*/
}

export default App;


function Coin() {
    const [money, setMoney] = useState(0);
    const [loading, setLoading] = useState(true);
    const [coins, setCoins] = useState([]);

    const onChange = (event) => {
        setMoney(event.target.value);
    };

    useEffect(() => {
        fetch(`https://api.coinpaprika.com/v1/tickers`)
            .then((response) => response.json())
            .then((json) => {
                setCoins(json);
                setLoading(false);
            });
    }, []);

    return (
        <div>
            <h1>The Coins! {loading ? "" : `(${coins.length})`}</h1>

            <input type="number" placeholder="Input your total money..." value={money} onChange={onChange}/>
            <hr/>

            {
                loading ?
                    (<strong>Lodaing...</strong>)
                    :
                    (<select>
                        {coins.map((coin) => (
                            <option key={coin.id}>
                                {coin.name} ({coin.symbol}) : {coin.quotes.USD.price} USD /
                                getItemCount: {Math.round(money / coin.quotes.USD.price)}
                            </option>
                        ))}
                    </select>)
            }

        </div>
    );
}


function ToDoList() {
    const [toDo, setToDo] = useState("");
    const [toDos, setToDos] = useState([]);
    const onChange = (event) => setToDo(event.target.value);
    const onSubmit = (event) => {
        event.preventDefault();
        if (toDo === "") {
            return;
        }
        setToDos((currentArray) => [toDo, ...currentArray]);
        setToDo("");

    };

    return (
        <div>
            <h1>My to Dos {toDos.length}</h1>
            <form onSubmit={onSubmit}>
                <input
                    type="text"
                    placeholder="Write your to do..."
                    value={toDo}
                    onChange={onChange}
                />
                <button>Add To Do</button>
            </form>
            <hr/>
            <ul>
                {toDos.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>
        </div>
    );
}

function Hello() {

    useEffect(() => {
        console.log("created!");
        return () => console.log("destroyed... ");      // called by 'Cleanup Function'
    }, []);


    return <h1>Hello</h1>;
}

function App_v2() {

    const [showing, setShowing] = useState(false);
    const onLClick = () => setShowing((prev) => !prev);

    return (
        <div>
            {showing ? <Hello/> : null}
            <button onClick={onLClick}>{showing ? "Hide" : "Show"}</button>
        </div>
    );
}

/*
* App 컴포넌트
* Node.js로 작업하고 있기 때문에 파일들을 각각 분리 시키는게 가능하고, 조직적을 구성할 수 있다.
* */

function App_v1() {


    const [counter, setCounter] = useState(0);
    const [keyword, setKeyword] = useState("");
    const onClick = () => setCounter((prev) => prev + 1);
    const onChange = (event) => setKeyword(event.target.value);

    useEffect(() => {
        console.log("I run only once");
    }, []);

    useEffect(() => {
        console.log("I run when 'keyword' changes.");
    }, [keyword]);

    useEffect(() => {
        console.log("I run when 'counter' changes.");
    }, [counter]);

    useEffect(() => {
        console.log("I run when 'keyword & counter' changes.");
    }, [keyword, counter]);

    return (
        <div>
            <input type="text" placeholder="Search here..." onChange={onChange} value={keyword}/>
            <h1>{counter}</h1>
            <button onClick={onClick}>Click me</button>

            {/*<h1 className={styles.title}>Welcome back!</h1>*/}
            {/*<Button text={"Continue"}/>*/}
        </div>
    );
}






