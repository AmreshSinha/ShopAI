import { useEffect, useState } from "react";
import { ResponseTile } from "./responseTile";
import './responseWrapper.css';
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";
export function ResponseWrapper ({askedQuery}){
    const sampleResponse = [
        {"product_link": "https://www.flipkart.com/anime-printed-typography-men-round-neck-red-t-shirt/p/itm29b6e8e150523?pid=TSHGRWKZMVYEDGVY&lid=LSTTSHGRWKZMVYEDGVYRT2QWP&marketplace=FLIPKART&q=Red+Anime+Shirt&store=clo%2Fash%2Fank%2Fedy&srno=s_1_3&otracker=search&iid=64a4f9d2-c7dd-4e9a-bac7-0c97aad974c3.TSHGRWKZMVYEDGVY.SEARCH&ssid=hk1im3eycw0000001692032407275&qH=84f370617203b766",
         "product_name": "Men Printed, Typography Round Neck Pure Cotton Red T-Sh...", 
         "product_price": "\u20b9799", 
         "image_link": "https://rukminim2.flixcart.com/image/612/612/xif0q/t-shirt/c/2/h/m-dsred-anime-original-imagrwknnnrhd6w7.jpeg?q=70"},
         {
            "product_link": "https://www.flipkart.com/urbano-fashion-slim-men-black-jeans/p/itma0bff19937afa?pid=JEAG2Q2TWBAWDDH3&lid=LSTJEAG2Q2TWBAWDDH3FSSQT7&marketplace=FLIPKART&q=Black+Ripped+Pant&store=clo%2Fvua&srno=s_1_3&otracker=search&iid=01f91877-0c72-48fd-9554-3944f0ea3eb5.JEAG2Q2TWBAWDDH3.SEARCH&ssid=ng059qckjk0000001692032409954&qH=eea035c817016d74",
            "product_name": "Men Slim Mid Rise Black Jeans",
            "product_price": "\u20b9715",
            "image_link": "https://rukminim2.flixcart.com/image/612/612/xif0q/jean/c/0/r/38-dis-heavy-black-01-urbano-fashion-original-imag2q2tqxfxk5kd-bb.jpeg?q=70"},
            {"product_link": "https://www.flipkart.com/aadi-synthetic-leather-lightweight-comfort-summer-trendy-walking-outdoor-daily-use-sneakers-men/p/itma442bf9226209?pid=SHOGDZZENAJYR87Z&lid=LSTSHOGDZZENAJYR87ZVP3RIY&marketplace=FLIPKART&q=Superhero+Sneakers&store=osp&spotlightTagId=BestsellerId_osp&srno=s_1_3&otracker=search&fm=organic&iid=b462c20c-d683-4912-9573-1ed1ad4e3f04.SHOGDZZENAJYR87Z.SEARCH&ppt=sp&ppn=sp&ssid=4ikl1pbzgg0000001692032411676&qH=2fef452791cacd87",
            "product_name": "Synthetic Leather |Lightweight|Comfort|Summer|Trendy|Wa...",
            "product_price": "\u20b9398",
            "image_link": "https://rukminim2.flixcart.com/image/612/612/l51d30w0/shoe/z/w/c/10-mrj1914-10-aadi-white-black-red-original-imagft9k9hydnfjp.jpeg?q=70"}
        ]
        let [recommendations, setRecommendations] = useState([{askedQuery, recommendations: sampleResponse}]);
        let [suggestQuery, setSuggestQuery] = useState("");
    console.log(recommendations);
    function handleSubmit(event) {
        //console.log(event);
        event.preventDefault();
        setRecommendations((prevRecommendations) => {
            //console.log([...prevRecommendations, null]);
            return [...prevRecommendations, { askedQuery: suggestQuery, recommendations: null }];
        });
    }


    return (<div>
        <div>
        {
            recommendations.map((recommendationObj,idx) => {
                console.log(recommendationObj);
                return <ResponseTile recommendationObj={recommendationObj} showSearchBar={idx===recommendations.length-1 ? true : false} setRecommendations={setRecommendations} suggestQuery={suggestQuery}/>;
            })
        }
        </div>
        <div className="p-6 flex justify-center">
            <div className="chatbar-wrapper" >
                <form onSubmit={handleSubmit}>
                    <IconButton type="submit" aria-label="search">
                        <SearchIcon style={{ fill: "black", fontSize: "1.5rem", margin: "0px" }} />
                    </IconButton>
                    <input type="text" className="text-field" autoFocus value={suggestQuery} onInput={e => setSuggestQuery(e.target.value)}/>
                </form>
            </div>
        </div>
    </div>);
}