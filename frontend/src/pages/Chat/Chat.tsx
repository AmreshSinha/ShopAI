import styled from "styled-components";
import React, { useState, useEffect } from "react";
import { Navbar } from "../../components/common/navbar";
import { useLocation } from "react-router-dom";
import Search from "./Search";
import ChatBot from "./ChatBot";

export default function Chat() {
  const location = useLocation();
  const userPref = location.state;
  const [queryAsked, setQueryAsked] = useState();
  const [cartItems, setCartItems] = useState([]);
  return (
    <HomeWrapper>
      <Navbar cartItems={cartItems} setCartItems={setCartItems} />
      {!queryAsked && <Search setQueryAsked={setQueryAsked} />}
      {queryAsked && (
        <ChatBot
          queryAsked={queryAsked}
          setQueryAsked={setQueryAsked}
          userPref={userPref}
          cartItems={cartItems}
          setCartItems={setCartItems}
        />
      )}
    </HomeWrapper>
  );
}

const HomeWrapper = styled.div`
  min-width: 100vw;
  min-height: 100vh;
  background: #171717;
`;
