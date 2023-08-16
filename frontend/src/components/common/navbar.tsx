import React from "react";
import { CartButton } from "./cartButton";
import "./navbar.css";

type NavbarProps = {
  CartDisabled?: Boolean;
};

export function Navbar<NavbarProps>({ CartDisabled = false }) {
  return (
    <div className="navbar">
      <div className="navbar-logo">ShopAI</div>
      <CartButton CartDisabled={CartDisabled} />
    </div>
  );
}
