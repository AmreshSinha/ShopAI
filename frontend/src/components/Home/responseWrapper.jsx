import { useEffect, useState } from "react";
import { ResponseTile } from "./responseTile";

export function ResponseWrapper ({askedQuery}){
    let [recommendations, setRecommendations] = useState([null]);
    let [query,setQuery] = useState("fksdhj");

    console.log(recommendations);

    return <div>
        {
            recommendations.map((recommendation,idx) => {
                console.log(recommendation);
                return <ResponseTile recommendation={recommendation} showSearchBar={idx===recommendations.length-1 ? true : false} setRecommendations={setRecommendations} query={query} setQuery={setQuery}/>;
            })
        }
    </div>
}