function setup(){
    createCanvas(400, 400);
    console.log("Oke!")
    frameRate(1)

}

function draw() {
    background(0);
    fill(120);
    ellipse(200, 200, 200, 200);

    fill(0, 255, 0, 160);
    ellipse(100, 200, 200, 200);

    fill(0, 255, 160);
    ellipse(300, 200, 200, 200);

    console.log("Oke Main Loop")
}