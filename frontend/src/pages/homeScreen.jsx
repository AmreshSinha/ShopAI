import { css } from "@emotion/react";
import { Box } from "@mui/material";
import Container from "@mui/material/Container";
import './homeScreen.css'
import { useState } from "react";
import { AiSearchBar } from "../components/Home/searchBar";
import { ResponseWrapper } from "../components/Home/responseWrapper";

export function HomeScreen() {
  let [askedQuery, setAskedQuery] = useState(null);
  console.log(askedQuery);
  return (
    <ResponseWrapper/>
  );
}