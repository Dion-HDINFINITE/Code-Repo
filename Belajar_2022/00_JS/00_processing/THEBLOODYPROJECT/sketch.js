const player1 = new Player();
player1.controller = 'mouse';
const player2 = new Player();
const ball = new Ball();
const ball2 = new Ball2();
const ball3 = new Ball3();

function setup() {
  createCanvas(500, 400);
  resetGame();
}

function resetGame(){
  player1.pos.x = 10;
  player2.pos.x = width - 20;
  player1.pos.y = 180;
  player2.pos.y = 180;
  ball.pos.x = (ball.direction === 1) ? 40 : 400;
  ball.pos.y = 200;
  ball.speed = 3;
  ball2.pos.x = (ball2.direction === 1) ? 40 : 400;
  ball2.pos.y = 200;
  ball2.speed = 3;
  ball3.pos.x = (ball3.direction === 1) ? 40 : 400;
  ball3.pos.y = 200;
  ball3.speed = 3;
}

function checkscore(){
  if(ball.pos.x > width){
    console.log('player 1 made the point');
    player1.points++;
    resetGame();
  }
  
  if(ball.pos.x + ball.size.w < 0){
    player2.points++;
    resetGame()
  }

  if(ball2.pos.x > width){
    console.log('player 1 made the point');
    player1.points++;
    resetGame();
  }
  
  if(ball2.pos.x + ball2.size.w < 0){
    player2.points++;
    resetGame()
  }

  if(ball3.pos.x > width){
    console.log('player 1 made the point');
    player1.points++;
    resetGame();
  }
  
  if(ball3.pos.x + ball3.size.w < 0){
    player2.points++;
    resetGame()
  }
}

function showScore() {
  fill('pink');
  textSize(48);
  text(player1.points,190,50);
  text(player2.points,284,50);
}

function ObjectCollisions(obj1, obj2) {
  if(
      (
      obj1.pos.x + obj1.size.w > obj2.pos.x 
       && 
      obj1.pos.x < obj2.pos.x + obj2.size.w
      )
    &&
      (
      obj1.pos.y + obj1.size.h > obj2.pos.y
        &&
      obj1.pos.y < obj2.pos.y + obj2.size.h
      )
  ){
    return true;  
  }
  return false;
}

function checkCollision(){
  if(ObjectCollisions(ball, player2)){
    ball.direction = -1;
    ball.speed += 0.1;
  }
  
  if(ObjectCollisions(ball, player1)){
    ball.direction = 1;
    ball.speed += 0.1;
  }
  
  if((ball.pos.y + ball.size.h) > height){
    ball.directionVertical = -1;
  }
  
  if(ball.pos.y < 0){
    ball.directionVertical = 1;
  }


  if(ObjectCollisions(ball2, player2)){
    ball2.direction = -1;
    ball2.speed += 0.1;
  }
  
  if(ObjectCollisions(ball2, player1)){
    ball2.direction = 1;
    ball2.speed += 0.1;
  }
  
  if((ball2.pos.y + ball2.size.h) > height){
    ball2.directionVertical = -1;
  }
  
  if(ball2.pos.y < 0){
    ball2.directionVertical = 1;
  }


  if(ObjectCollisions(ball3, player2)){
    ball3.direction = -1;
    ball3.speed += 0.1;
  }
  
  if(ObjectCollisions(ball3, player1)){
    ball3.direction = 1;
    ball3.speed += 0.1;
  }
  
  if((ball3.pos.y + ball3.size.h) > height){
    ball3.directionVertical = -1;
  }
  
  if(ball3.pos.y < 0){
    ball3.directionVertical = 1;
  }
}

function draw() {
  background("black");
  strokeWeight(5);
  stroke("white");
  line(width / 2, 0, width / 2, height);

  player1.update();
  player2.update();
  ball.update();
  ball2.update();
  ball3.update();
  
  checkCollision();
  
  checkscore();

  player1.show();
  player2.show();
  ball.show();
  ball2.show();
  ball3.show();
  
  showScore();
}
