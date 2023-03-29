// const request = new XMLHttpRequest();
// request.onload = function(){
//     const response = JSON.parse(this.responseText);
//     console.log(response);
// }
// request.open("get", "https://www.omdbapi.com/?apikey=26ced797&");
// request.send();

// const request = fetch("https://www.omdbapi.com/?apikey=26ced797&s=star%20wars")
//     .then(response => response.json())
//     .then(response => console.log(response));




// $.ajax({
//     url : "https://www.omdbapi.com/?apikey=26ced797&s=star%20wars",
//     success : response => console.log(response)
// })




// const fulfilled = true;
// const promise = new Promise((resolve, reject) => {
//     if (fulfilled)
//         resolve("Done");
//     else
//     reject("Undone");
// });

// promise
//     .then(response => console.log("Okay..."+response))
//     .catch(response => console.log("Not okay...."+response))

fetch("https://www.omdbapi.com/?apikey=26ced797&s=star%20wars")
    .then(response => response.json())
    .then(response => console.log(response))
    .catch(response => console.log("Sorry UwU" + error));
