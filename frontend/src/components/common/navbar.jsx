import { CartButton } from "./cartButton";
import './navbar.css';

export function Navbar(){
    return <div className="navbar">
        <div className="navbar-logo">ShopAI</div>
        <CartButton/>
    </div>
}