import { css } from "@emotion/react";
import { Box } from "@mui/material";
import Container from "@mui/material/Container";

const homeCss = {
  homeWrapper: {
    minWidth: "100vw",
    minHeight: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },
  extraWrapper: {
    width: "fit-content",
    height: "fit-content",
    backdropFilter: "blur(16px) saturate(180%)",
    padding: "16px",
    backgroundColor: "rgba(255, 255, 255, 0.5)",
    borderRadius: "28px",
    border: "0.1px solid rgb(255, 255, 255, 0.3)",
  },
  container: {
    background: "rgba(255, 255, 255, 0.9)",
    height: "90vh",
    width: "60vw",
    borderRadius: "20px",
    boxShadow: "0px 0px 8px 0px rgba(0,0,0,0.08)",
    display: "flex",
    flexDirection: "center",
    justifyContent: "center",
    padding: "16px 0 16px 0",
  },

};

export default function Home() {
  return (
    <div style={homeCss.homeWrapper}>
      <div id="extra-wrapper" style={homeCss.extraWrapper}>
        <Container style={homeCss.container}>
          
        </Container>
      </div>
    </div>
  );
}
