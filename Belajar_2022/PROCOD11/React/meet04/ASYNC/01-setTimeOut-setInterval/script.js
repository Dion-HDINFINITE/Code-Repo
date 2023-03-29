document.addEventListener("DOMContentLoaded"), () => {
    
    
    function consoleLogDelay(number){
        setTimeout(() => {
            console.log(number);
        }, 2000);
    }


    var i = 100;
    let consoleInterval = setInterval(() => {
        console.log(i);
        i--;
    }, 1000);


    console.log(1);
    consoleLogDelay(2);
    console.log(3);

    document.querySelector("#btn-stop-interval").addEventListener("click", () => {
    })
}

