import { useEffect, useState } from "react";
import { CircularProgress } from "@mui/material";
import { Link } from 'react-router-dom';
import axios from "axios";
import './responseTile.css';

function ItemTile({product_link,product_name,product_price,image_link}) {
    return <div>
        <img src={image_link} />
        <div>{product_name}</div>
        <a target="_blank" rel="noreferrer" href={product_link}>Buy Now</a>
    </div>;
}

export function ResponseTile({ recommendationObj, showSearchBar, setRecommendations }) {

    //console.log(recommendation);
    console.log(recommendationObj);

    let [suggestQuery, setSuggestQuery] = useState("");

    useEffect(() => {
        if (recommendationObj.recommendations === null) {
            axios.get(`http://localhost:8000/items/${recommendationObj.askedQuery}`).then((res) => {
                console.log(res.data);
                setRecommendations((prevRecommendations) => {
                    prevRecommendations[prevRecommendations.length - 1].recommendations = JSON.parse(res.data);
                    return [...prevRecommendations];
                });
            });
        }
    }, []);

    function handleSubmit(event) {
        //console.log(event);
        event.preventDefault();
        setRecommendations((prevRecommendations) => {
            //console.log([...prevRecommendations, null]);
            return [...prevRecommendations, { askedQuery: suggestQuery, recommendations: null }];
        });
    }

    return <div style={{ "display": "flex", "justifyContent": "center" }}>
        {
            !recommendationObj.recommendations ? <CircularProgress color="secondary" /> :
                <div className="response-tile-wrapper">
                    <div style={{ "display": "flex" }}>
                        <img src="/user-avatar.svg" />
                        <div className="tile-text">
                            {recommendationObj.askedQuery}
                        </div>
                    </div>
                    <div>
                        {
                            recommendationObj.recommendations.map((product,idx) => <ItemTile {...product}/>)
                        }
                    </div>
                    {
                        showSearchBar ? <form onSubmit={handleSubmit}>
                            <input type="text" className="text-field" autoFocus value={suggestQuery} onInput={e => setSuggestQuery(e.target.value)} />
                        </form> : null
                    }
                </div>
        }
    </div>;
}