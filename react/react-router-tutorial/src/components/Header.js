import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const MenuItem = ({active, children, to}) => (
    <Link to={to} className="menu-item">
        {children}
    </Link>
)

const Header = () => {
    return (
        <div>
            <div className="logo">
                Header
            </div>
            <div className="menu">
                <MenuItem to={'/'}>Home</MenuItem>
                <MenuItem to={'/about'}>About</MenuItem>
                <MenuItem to={'/post'}>Post</MenuItem>
            </div>
        </div>
    )
}

export default Header;