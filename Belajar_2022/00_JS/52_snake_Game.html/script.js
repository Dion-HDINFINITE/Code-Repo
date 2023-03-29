document.addEventListener('DOMContentLoaded', () => {

	let canvas = document.getElementById("canvas");
	let ctx = canvas.getContext("2d");

	let score = 0;
	let start = false;

	// console.log(canvas.width, canvas.height);
	const blockSize = 20;
	const column = canvas.width / blockSize;
	const row = column;

	const border = {

		color : "Black",
		size : blockSize,
		width : canvas.width,
		height : canvas.height,

		draw : function() {

			ctx.fillStyle = this.color;
			const top = ctx.fillRect(0, 0, this.width, this.size);
			const right = ctx.fillRect(this.width-this.size, 0, this.size, this.height);

			const bottom = ctx.fillRect(0, this.height-this.size, this.width, this.size);
			const left = ctx.fillRect(0, 0, this.size, this.height);

		}
	}

	let scoreText = {
		font : "20px Courier",
		color : "White",
		align : "left",
		baseline : "top",

		draw : function () {
			const x = 0;
			const y = 0;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText(`Score : ${score}`, x, y);
		}
	}

	const gameOverText = {
		font : "60px Courier",
		color : "White",
		align : "center",
		baseline : "middle",

		draw : function () {
			clearInterval(mainloop);
			const x = canvas.width/2;
			const y = canvas.height/2;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText(`Game Over`, x, y);
		}
	}

	const startButton = {
		x : canvas.width/2,
		y : canvas.height/2,
		width : 6 * blockSize,
		height : 3 * blockSize,
		color : "Black",
		textColor : "White",
		font : "32px Courier",
		align : "center",
		baseline : "middle",

		draw : function (){
			ctx.fillStyle = this.color;
			ctx.fillRect(this.x - this.width/2, this.y - this.height/2, this.width, this.height);

			ctx.fillStyle = this.textColor;
			ctx.font = this.font;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText('Start', this.x, this.y);
		},

		checkClicked : function (event){
			if ((event.offsetX >= this.x- this.width/2) && (event.offsetY >= this.y- this.height/2) && (event.offsetX <= (this.x+this.width/2)) && (event.offsetY <= (this.y+this.height/2))) start = true;
		}

	}

	class Block {

		constructor(row, column){ //(y, x)
			this.row = row;
			this.column = column;

			this.size = blockSize;
		}

		circle(x, y, radius, color, isFilled) {
			ctx.strokeStyle = color;
			ctx.beginPath();
			ctx.arc(x, y, radius, 0, 2*Math.PI, false);
			// ctx.stroke();
			if (isFilled) {
				ctx.fillStyle = color;
				ctx.fill();
			}
		}

		drawSquare(color){
			let x = this.column * this.size;
			let y = this.row * this.size;
			this.color = color;

			ctx.fillStyle = this.color;
			ctx.fillRect(x, y, this.size, this.size);
		}

		drawCircle(color){
			let x = this.column * this.size + this.size/2;
			let y = this.row * this.size + this.size/2;
			this.color = color;

			this.circle(x, y, this.size/2, this.color, true);
		}

	}

	class Snake {

		constructor(){
			this.segments = [
				new Block(7, 5), // head
				new Block(6, 5),
				new Block(5, 5) // tail
			]
			this.direction = "right";
			this.nextDirection = "right";
		}

		draw(){
			this.segments.forEach((segment) => {
				segment.drawSquare("Blue");
			});

		}

		setDirection(newDirection){
			if (this.direction === "right" && newDirection === "left") return;
			if (this.direction === "left" && newDirection === "right") return;
			if (this.direction === "up" && newDirection === "down") return;
			if (this.direction === "down" && newDirection === "up") return;

			console.log(newDirection);
			this.nextDirection = newDirection;
		}

		move(){

			let head = this.segments[0];
			let newHead;

			this.direction = this.nextDirection;

			if (this.direction === "right") newHead = new Block(head.row, head.column+1);
			else if (this.direction === "down") newHead = new Block(head.row+1, head.column);
			else if (this.direction === "left") newHead = new Block(head.row, head.column-1);
			else if (this.direction === "up") newHead = new Block(head.row-1, head.column);

			if (this.checkCollision(newHead)){
				gameOverText.draw();
				return;
			}

			this.segments.unshift(newHead);
			// this.segments.pop();

			if (this.eatApple(head)){
				score++;
				apple.move();
			} else {
				this.segments.pop();
			}

		}

		checkCollision(head){
			const leftCollision = head.column === 0;
			const topCollision = head.row === 0;
			const rightCollision = head.column === column - 1;
			const bottomCollision = head.row === row - 1;

			const wallCollision = leftCollision || topCollision || rightCollision || bottomCollision;

			this.segments.forEach((segment, i) => {
				// console.log(head.row, segment.row, head.column, segment.column);
				if (head.row === segment.row && head.column === segment.column){
					const selfCollision = true;
					return selfCollision;
				}
			});

			return wallCollision;

		}

		eatApple(head){
			if (head.row === apple.block.row && head.column === apple.block.column){
				return true;
			}
			return false;
		}


	}

	class Apple {

		constructor(){
			this.block = new Block(0,0);
			this.move();
		}

		draw(){
			this.block.drawCircle("Green");
		}

		move(){
			let randomRow = Math.floor(Math.random() * (row-2)) + 1;
			let randomColumn = Math.floor(Math.random() * (column-2)) + 1;
			this.block.row = randomRow;
			this.block.column = randomColumn;
		}


	}




	// gameOverText.draw();
	// document.querySelector("body").onkeydown = (event) => {
	// 	console.log(event.code);
	// }
	// Jquery
	// $('body').keydown( (event) => {
	// 	console.log(event.keyCode);
	// })

	document.addEventListener('keydown', () => {
		// console.log(event.code);
		switch (event.code) {
			case "KeyW":
				snake.setDirection("up");
				break;
			case "KeyS":
				snake.setDirection("down");
				break;
			case "KeyA":
				snake.setDirection("left");
				break;
			case "KeyD":
				snake.setDirection("right");
				break;
			default:
				console.log("undefined");

		}
	})

	document.querySelector("#canvas").addEventListener('click', function(event){
		if (!start) startButton.checkClicked(event);
	})

	let snake = new Snake();
	let apple = new Apple();

	let mainloop = setInterval( () => {
		ctx.clearRect(0, 0, canvas.width, canvas.height);
		border.draw();
		scoreText.draw();
		snake.draw();
		apple.draw();
		if (start){
			snake.move();
		} else {
			startButton.draw();
		}
	}, 100)

})

// 1. Tema Kebersihan Sekitar
// 2. Tema Kesehatan Selama Mudik
// 3. Tema Kedisiplinan Dalam belajar
// dll
// 1 Kelompok Ber2
// Konsep : Game Tebak Kata, Game Flappy Bird, Game Tong Sampah
// Konsep : Game Snake, Game Alien, Game RPG, Type Text, Konsep Dinasurus
// OPSI SMA