import React from "react";
import ShoppingCartIcon from "@mui/icons-material/ShoppingCart";
import "./cartButton.css";

type CartButtonProps = {
  CartDisabled?: boolean;
};

export function CartButton<CartButtonProps>({ CartDisabled = false }) {
  return (
    <button className="cart-button" disabled={CartDisabled}>
      <ShoppingCartIcon sx={{ paddingRight: "0.25rem" }} />
      <div className="cart-button-text">Cart</div>
    </button>
  );
}
