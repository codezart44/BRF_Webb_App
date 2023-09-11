import React from 'react'
import "./navbar.css"

function Navbar() {
  return (
    <header className="header">
        <div className="navbar">
            <a href="#" className="navbar__leftItem">BRF Osqars Backe</a>
                <ul className="navbar__rightItemList">
                    <li><a href="#"  className="navbar__rightItem">Hem</a></li>
                    <li><a href="#"  className="navbar__rightItem">Boka tvättid</a></li>
                    <li><a href="#"  className="navbar__rightItem">Kontakta oss</a></li>
                </ul>
        </div>
    </header>
  )
}

export default Navbar
