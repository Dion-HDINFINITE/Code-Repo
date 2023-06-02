import React from "react"

import "./Header.css"
import Trollface from "../assets/img/Trollface.png"

function Header(){
    return (
        <header>
            <img alt="trollface meme generator" src={Trollface} className="header--image"/>
            <h1>
                Meme Generator
            </h1>

            <h4>
                Mini project react
            </h4>
            <div className="header--toggle--darkmode">
                <span className="header--circle--darkmode">
                    

                </span>
            </div>
        </header>
    )
}

export default Header;