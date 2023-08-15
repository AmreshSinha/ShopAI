import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
// import App from "./App.jsx";
import './index.css';
import { Outlet, RouterProvider, createBrowserRouter } from "react-router-dom";
import { Navbar } from "./components/common/navbar";

const router = createBrowserRouter([
  {
    element: <>
    <header>
      <Navbar />
    </header>
    <Outlet />
  </>,
    children: [
      {
        path: "/",
        element: <App />
      }
    ]
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
