import "./main_section.css"
import React, {useState} from "react"

export default function MainSection(props){

    // const [status, setStatus] = React.useState(true);
    
    const [state, setState] = useState({
        num1 : Math.floor((Math.random() * 10)),
        num2 : Math.floor((Math.random() * 10)),
        oprlist : ["+", "-", "*"],
        opr : "+",
        color : "black",
        score : 0,
        respondlist : ["Correct Answer!", "Incorrect Answer!", "You Win!", "Game Over!"],
        respondText : "",
        answer : ""
    });

    // const [num1, setNum1] = React.useState(1);

    function updateResponse(event){
        setState({
            ...state,
            answer : event.target.value
        })
    }

    function checkResponse(event){
        if (event.key === "Enter"){
            if (JSON.parse(state.answer) === state.num1 + state.num2) {

                generateQuestion()

            } else if (JSON.parse(state.answer) === state.num1 * state.num2) {

                generateQuestion()

            } else if (JSON.parse(state.answer) === state.num1 - state.num2) {

                generateQuestion()

            } else {

                setState({
                    ...state,
                    score : state.score - 1,
                    answer : "",
                    num1 : Math.floor((Math.random() * 10)),
                    color : 'red',
                    num2 : Math.floor((Math.random() * 10)),
                    opr : state.oprlist[Math.floor(Math.random() * state.oprlist.length)],
                    respondText : state.respondlist[1]
                })

            }
        }
    }

    function generateQuestion(){
        setState({
            ...state,
            score : state.score + 1,
            answer : "",
            num1 : Math.floor((Math.random() * 10)),
            num2 : Math.floor((Math.random() * 10)),
            color : 'black',
            opr : state.oprlist[Math.floor(Math.random() * state.oprlist.length)],
            respondText : state.respondlist[0]
        })
    }

    if (state.score > 4) {
        return (
            <div className="container">
                <h1>{state.respondlist[2]}</h1>
            </div>
        )
    } 
    
    if (state.score === -5) {
        return (
            <div className="container" style={{'background-color' : state.color}}>
                <h1>{state.respondlist[3]}</h1>
            </div>
        )
    }

    return  (
        <div className="container">
            <h1 style={{'color' : state.color}}>{state.num1} {state.opr} {state.num2} = ?</h1>
            <br></br>
            <input 
                type="text"
                placeholder="Put your answer here" 
                onChange={updateResponse} 
                value={state.answer} 
                onKeyPress={checkResponse}
            />
            <br></br>
            <p>Your score is : {state.score}</p>
            <br></br>
            <p>{state.respondText}</p>
        </div>
    )
}

// export default main_section;