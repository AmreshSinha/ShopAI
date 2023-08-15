import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route} from "react-router-dom";
import { HomeScreen } from "./pages/homeScreen";
import { Navbar } from "./components/common/navbar";
import App from "./App";
// import App from "./App.jsx";
import './index.css';

// const router = createBrowserRouter([
//   {
//     path: "/",
//     element: <App />
//   },
// ]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App/>
  </React.StrictMode>
);
