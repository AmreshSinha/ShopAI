import styled from "styled-components";
import React, { useState, useEffect } from "react";
import { Navbar } from "../../components/common/navbar";
import { useLocation } from "react-router-dom";
import axios from "axios";
import Search from "./Search";
import ChatBot from "./ChatBot";

export default function Chat() {
  const location = useLocation();
  const userPref = location.state;
  const [queryAsked, setQueryAsked] = useState();
  return (
    <HomeWrapper>
      <Navbar />
      {!queryAsked && <Search setQueryAsked={setQueryAsked} />}
      {queryAsked && <ChatBot queryAsked={queryAsked} userPref={userPref} />}
    </HomeWrapper>
  );
}

const HomeWrapper = styled.div`
  min-width: 100vw;
  min-height: 100vh;
  background: #171717;
`;
