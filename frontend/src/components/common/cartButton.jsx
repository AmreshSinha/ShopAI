import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import './cartButton.css';

export function CartButton() {
    return <button className='cart-button' disabled={true}>
        <ShoppingCartIcon sx={{paddingRight: '0.25rem'}} />
        <div className='cart-button-text'>
            Cart
        </div>
    </button>
}