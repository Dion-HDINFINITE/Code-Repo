document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("button").addEventListener("click", () => {

        const request = new XMLHttpRequest()

        request.onload = function(){
            const data = JSON.parse(this.responseText);
            console.log(data);
        }
        request.open("GET", "https://api.openweathermap.org/data/2.5/weather?lat=10.99&lon=44.34&appid=b6907d289e10d714a6e88b30761fae22");
        request.send();

    })
})