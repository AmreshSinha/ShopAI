import React from "react";
import styled from "styled-components";
import { PiPaperPlaneRightFill } from "react-icons/pi";

type SearchProps = {
  setQueryAsked: React.Dispatch<React.SetStateAction<string>>;
};

export default function Search<SearchProps>({ setQueryAsked }) {
  const categories = {
    Sports: "Suggest me an outfit for a sports event",
    Wedding: "Suggest me an outfit for a wedding",
    University: "Suggest me an outfit for a university event",
    "Award Ceremony": "Suggest me an outfit for an award ceremony",
    "Prom Night": "Suggest me an outfit for a prom night",
    Club: "Suggest me an outfit for club party",
    Beach: "Suggest me an outfit for going out to beach",
    Trekking: "Suggest me an outfit for trekking",
    Ethnic: "Suggest me an ethnic outfit",
    Western: "Suggest me a western outfit",
    Formal: "Suggest me a formal outfit",
    Casual: "Suggest me a casual outfit",
  };
  const tryThese = [
    "Suggest me an outfit for a Halloween party",
    "Suggest me an outfit for a Bollywood theme party",
    "Recommend me an outfit for Durga Puja in Guwahati",
  ];
  return (
    <SearchWrapper>
      <Container>
        <div
          style={{
            width: "100%",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: "1rem",
          }}
        >
          <div>
            <h1 style={{ fontSize: "64px", color: "#fff" }}>Welcome back</h1>
          </div>
          <form
            id="input"
            onSubmit={(e) => {
              e.preventDefault();
              const formData = new FormData(e.currentTarget);
              const data = Object.fromEntries(formData.entries());
              setQueryAsked(data.query);
            }}
          >
            <input
              type="text"
              name="query"
              id="query"
              placeholder="What Outfit are you looking for today?"
              required
            />
            <button>
              Start <PiPaperPlaneRightFill />
            </button>
          </form>
        </div>
        <div className="bottom">
          <div className="bottom-subsection">
            <h2 className="subtitle">Categories</h2>
            <div className="tilesWrapper">
              {Object.keys(categories).map((category) => (
                <CategoryButton
                  onClick={(e) => {
                    e.preventDefault();
                    setQueryAsked(categories[category]);
                  }}
                >
                  {category}
                </CategoryButton>
              ))}
            </div>
          </div>
          <div className="bottom-subsection">
            <h2 className="subtitle">Try These</h2>
            <div className="tilesWrapper">
              {tryThese.map((example) => (
                <FullWidthTile
                  onClick={(e) => {
                    e.preventDefault();
                    setQueryAsked(example);
                  }}
                >
                  Example: {example}
                </FullWidthTile>
              ))}
            </div>
          </div>
        </div>
      </Container>
    </SearchWrapper>
  );
}

const SearchWrapper = styled.div`
  min-height: 100vh;
  min-width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: 700;
  padding-top: 72px;
`;

const Container = styled.div`
  width: calc(100vw / 3);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 32px;
  #input {
    width: 100%;
    background: #d9d9d9;
    border-radius: 20px;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    input {
      all: unset;
      padding: 0.5rem;
      flex-grow: 1;
    }
    button {
      display: flex;
      gap: 4px;
      border-radius: 16px;
      background: #c86c53;
      color: #fff;
      padding: 8px 12px;
      font-weight: 400;
    }
  }
  .bottom {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 32px;
  }
  .bottom-subsection {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  .subtitle {
    color: #fff;
    font-size: 24px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
  }
  .tilesWrapper {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }
`;

const CategoryButton = styled.button`
  all: unset;
  padding: 12px 16px;
  border-radius: 999px;
  background: #262626;
  color: #fff;
  font-weight: 400;
`;

const FullWidthTile = styled.button`
  all: unset;
  padding: 12px 16px;
  border-radius: 999px;
  background: #262626;
  color: #fff;
  font-weight: 400;
  width: 100%;
`;
