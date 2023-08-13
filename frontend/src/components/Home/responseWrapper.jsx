import { useEffect, useState } from "react";
import { ResponseTile } from "./responseTile";

export function ResponseWrapper ({askedQuery}){
    let [recommendations, setRecommendations] = useState([{askedQuery, recommendations: null}]);

    console.log(recommendations);

    return <div>
        {
            recommendations.map((recommendationObj,idx) => {
                console.log(recommendationObj);
                return <ResponseTile recommendationObj={recommendationObj} showSearchBar={idx===recommendations.length-1 ? true : false} setRecommendations={setRecommendations}/>;
            })
        }
    </div>
}