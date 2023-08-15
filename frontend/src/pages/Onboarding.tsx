import React from "react";
import styled from "styled-components";

export default function Onboarding() {
  return (
    <Container>
      <div>
        <h1>Welcome to ShopAI</h1>
        <p>
          Press fill the below details
          <br />
          before proceeding ahead
        </p>
      </div>
    </Container>
  );
}

const Container = styled.div`
  display: flex;
  width: calc(100vw / 3);
`;
