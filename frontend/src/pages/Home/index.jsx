import { css } from "@emotion/react";
import { Box } from "@mui/material";
import Container from "@mui/material/Container";
import './index.css'
import { AiSearchBar } from "../../components/Home/searchBar";



export default function Home() {
  return (
    <div className='app-wrapper'>
      <div>
      <div className="title-text">ShopAI will help you plan an outfit</div>
      <AiSearchBar/>
      </div>
    </div>
  );
}
