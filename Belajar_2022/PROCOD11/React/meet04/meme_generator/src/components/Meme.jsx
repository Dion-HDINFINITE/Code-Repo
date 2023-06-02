import React from "react"

import "./Meme.css"

function Meme(){

    const [state, setState] = React.useState({
        isLoading : true,
        topText : "",
        bottomText : "",
        image : "imah"
    })

    const [allMemeData, setAllMemeData] = React.useState([]);

    React.useEffect( () => {

        fetch("https://api.imgflip.com/get_memes")
            .then(res => res.json())
            .then(data => {
                setAllMemeData(data.data.memes);
                setState({
                    ...state,
                    isLoading : false,
                    image : data.data.memes[Math.floor(Math.random() * data.data.memes.length)]["url"]
                });

            })
            .catch(err => console.log(err));

    }, [])

    // console.log(state.image);
    function handleChange(event){
        const {name, value} = event.target;
        setState(state => ({
            ...state,
            [name] : value
        }))
    }

    function getRandomMemeImage(){
        const memeArr = allMemeData;
        const randomIndex = Math.floor(Math.random()*memeArr.length);
        const imageUrl = memeArr[randomIndex].url;
        return imageUrl;
    }

    function getMemeImage(event){
        event.preventDefault();
        setState(state => ({
            ...state,
            image : getRandomMemeImage()
        }))
    }

    return (
        <section className="section--meme">
            <form className="meme--form" onSubmit={getMemeImage}>
                <input  type="text" 
                        name="topText"
                        placeholder="Top Text"
                        className="meme--form--input"
                        value={state.topText}
                        onChange={handleChange} 
                        id="" />
                <input  type="text" 
                        name="bottomText"
                        placeholder="Bottom Text"
                        className="meme--form--input" 
                        value={state.bottomText}
                        onChange={handleChange}
                        id="" />
                <input  type="submit" 
                        value="Get new image"
                        className="meme--form--button" />
            </form>

            <div className="meme--content">
                <img    src={state.image}
                        className="meme-image" 
                        alt="" />
                <h2 className="meme--top--text">{state.topText}</h2>
                <h2 className="meme--bottom--text">{state.bottomText}</h2>
            </div>
        </section>
    )
}

export default Meme;