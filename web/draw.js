"use strict";

var context = document.getElementById('drawingCanvas').getContext("2d");
var clickX = new Array();
var clickY = new Array();
var clickDrag = new Array();
var paint;

var curColor = 'black';
var clickColor = new Array();

var clickSize = new Array();
var curSize = 10;

var clickTool = new Array();
var curTool = setBrushSize($('#brush-size-range').val());

$('#drawingCanvas').mousedown(function(e){
	var mouseX = e.pageX - this.offsetLeft;
	var mouseY = e.pageY - this.offsetTop;
		
	paint = true;
	addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
	redraw();
});

$('#drawingCanvas').mousemove(function(e){
	if(paint){
		addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
		redraw();
	}
});

$('#drawingCanvas').mouseup(function(e){
	paint = false;
});

$('#drawingCanvas').mouseleave(function(e){
	paint = false;
});

// -------------------

function setBrushSize(value){
	console.log(value)
	curSize = 0.5 + 50.0 * parseFloat(value) / 100.0;
	console.log(curSize);
}

// -------------------

function setTool(toolName){
	curTool = toolName;
	switch(toolName){
		case 'brush':
			console.log('switching to brush tool');
			break;
		case 'eraser':
			console.log('switching to eraser tool');
			break;
		case 'bucket':
			break;
		case 'eyeDropper':
			break;
		default:
			break;
	}
}

// -------------------

function colorChange(jscolor){
	curColor = '#' + jscolor;
}

// -------------------

function addClick(x, y, dragging){
	clickX.push(x);
	clickY.push(y);
	clickDrag.push(dragging);
	if(curTool == "eraser"){
		clickColor.push("white");
	}else{
		clickColor.push(curColor);
	}
	clickSize.push(curSize);
}

// -------------------

function redraw(){
	context.clearRect(0, 0, context.canvas.width, context.canvas.height); // Clears the canvas
	context.lineJoin = "round";

	for(var i=0; i < clickX.length; i++) {		
		context.beginPath();
		if(clickDrag[i] && i){
			context.moveTo(clickX[i-1], clickY[i-1]);
		}else{
			context.moveTo(clickX[i]-1, clickY[i]);
		}
		context.lineTo(clickX[i], clickY[i]);
		context.closePath();
		context.strokeStyle = clickColor[i];
		context.lineWidth = clickSize[i];
		context.stroke();
	}
}