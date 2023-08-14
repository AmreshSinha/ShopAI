import { useEffect, useState } from "react";
import { CircularProgress } from "@mui/material";
import { Link } from 'react-router-dom';

import axios from "axios";
import './responseTile.css';
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";
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
function ItemTile({product_link,product_name,product_price,image_link}) {
    return <div>
    {/* <Card sx={{ maxWidth: 160 }}>
      <CardMedia
        sx={{ height: 160 }}
        image={image_link}
      />
      <CardContent>
        <Typography gutterBottom variant="h7" component="div">
          {product_name}
        </Typography>
        <Typography variant="body4" color="text.secondary">
          Price : {product_price}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Buy Now</Button>
      </CardActions>
    </Card> */}
    <div class="relative flex w-44 flex-col rounded-xl bg-white bg-clip-border text-gray-700 shadow-md">
  <div class="relative mx-2 mt-2 h-44 overflow-hidden rounded-xl bg-white bg-clip-border text-gray-700 ">
    <img src={image_link} alt="profile-picture" />
  </div>
  <div class="p-2 text-center">
    <h4 class="mb-2 block h-24 font-sans text-md font-semibold leading-snug tracking-normal text-blue-gray-900 antialiased overflow-hidden text-ellipsis">
      {product_name}
    </h4>
    <p class="block text-black bg-clip-text font-sans text-base font-medium leading-relaxed antialiased">
      Price: {product_price}
    </p>
  </div>
  <div class="flex justify-center gap-7 p-6 pt-2">
    <a href={product_link}><button>Buy Now</button></a>
  </div>
</div>
    </div>;
}

export function ResponseTile({ recommendationObj, showSearchBar, setRecommendations,suggestQuery }) {

    //console.log(recommendation);
    console.log(recommendationObj);

    

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
                    <div style={{ "display": "flex", "margin" : "1rem"}}>
                        <img src="/user-avatar.svg" />
                        <div className="tile-text">
                            {recommendationObj.askedQuery}
                        </div>
                    </div>
                    <div className="flex flex-col bg-gray-400 w-full p-4">
                    <div className="tile-text">
                            Here's your recommended outfit
                        </div>
                        <div className="flex flex-row gap-4 mt-4 flex-wrap">
                            
                            {
                                recommendationObj.recommendations.map((product,idx) => <ItemTile {...product}/>)
                            }
                        </div>
                    </div>
                    
                </div>
        }
    </div>;
}