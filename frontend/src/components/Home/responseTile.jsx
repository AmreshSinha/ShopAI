import { useEffect, useState } from "react";
import { CircularProgress } from "@mui/material";
import axios from "axios";

export function ResponseTile({ recommendation, showSearchBar, setRecommendations, query, setQuery }) {

    //console.log(recommendation);

    let [suggestQuery, setSuggestQuery] = useState("");

    useEffect(() => {
        if (recommendation===null) {
            axios.get(`http://localhost:8000/items/${query}`).then((res) => {
                //console.log(res.data);
                setRecommendations((prevRecommendations) => {
                    let resp=[]
                    for(let i=0;i<prevRecommendations.length-1;i++){
                        resp.push(prevRecommendations[i]);
                    }
                    resp.push(res.data);
                    return resp;
                });
            });
        }
    }, []);

    function handleSubmit(event) {
        //console.log(event);
        event.preventDefault();
        setRecommendations((prevRecommendations) => {
            //console.log([...prevRecommendations, null]);
            return [...prevRecommendations, null];
        });
        setQuery(suggestQuery);
    }

    return <>
        {
            !recommendation ? <CircularProgress color="secondary" /> :
                <>
                    {recommendation}
                    {
                        showSearchBar ? <form onSubmit={handleSubmit}>
                            <input type="text" className="text-field" autoFocus value={suggestQuery} onInput={e => setSuggestQuery(e.target.value)} />
                        </form> : null
                    }
                </>
        }
    </>;
}