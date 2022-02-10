const grid = document.getElementById('grid');
const actual = "ROBOT";
let currRow = 0;
let currCol = 0;

const init = (rows, cols) => {
    let html = ``;

    for (let i = 0; i < rows; i++) {
        html += `<div class='row' id='row-${i+1}'>`;

        for (let j = 0; j < cols; j++) {
            html += `<div class='box' id='box-${i+1}-${j+1}'></div>`
        }
        html += `</div>`;
    }

    grid.innerHTML += html;
}


const colorizeRow = (guess, actual) => {
    let res = true;
    for (let i = 0; i < 5; i++) {
        if (guess.charAt(i) == actual.charAt(i)) {
            document.getElementById(`box-${currRow + 1}-${i + 1}`).style.backgroundColor = 'green';
        } else if (actual.includes(guess.charAt(i))) {
            document.getElementById(`box-${currRow + 1}-${i + 1}`).style.backgroundColor = 'yellow';
            res = false;
        } else {
            document.getElementById(`box-${currRow + 1}-${i + 1}`).style.backgroundColor = 'grey';
            res = false;
        }
    }

    if (res) {
        // alert('You win!');
    }
    currRow++;
    currCol = 0;
}

document.body.onkeydown = (e) => {
    
    console.log(currRow, currCol);

    let currLetter = String.fromCharCode(e.keyCode);

    if (currLetter.length === 1 && currLetter.match(/[A-Z]/i) && currCol <= 4) { 
        document.getElementById(`box-${currRow + 1}-${currCol + 1}`).innerHTML = currLetter;
        currCol++;
    } else if (e.keyCode == 8 && currCol >= 0) { // backspace
        document.getElementById(`box-${currRow + 1}-${currCol}`).innerHTML = "";
        currCol--;
    } else if (e.keyCode == 13 && currCol == 5) { // enter
        let currInput = "";
        for (let i = 0; i < 5; i++) {
            currInput += document.getElementById(`box-${currRow + 1}-${i + 1}`).innerHTML
        }
        console.log(currInput);
        colorizeRow(currInput, actual);
    }
    
}

init(5, 5);