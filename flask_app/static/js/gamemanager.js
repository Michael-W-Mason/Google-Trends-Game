document.getElementById("page-content").style.visibility = 'hidden';
document.getElementById("leaderboard").style.visibility = 'hidden';
let current_question_id = undefined;
let timerObj = null;

let myForm = document.getElementById('leaderboard-form');
myForm.onsubmit = function(e){
    e.preventDefault();
    console.log(myForm)
    let form = new FormData();
    let score = document.getElementById('game-score').innerHTML;
    let name = document.getElementById('player-name').value;
    if (name == ""){
        return alert("Name Cannot Be Empty")
    }
    form.append('name', name);
    form.append('score', score);
    fetch('http://127.0.0.1:5000/submit_leaderboard', {method : 'POST', body : form})
        .then(response => response.json)
        .then(data => {
            myForm.style.visibility = 'hidden';
            getLeaderboard();
        })
}

function startGame() {
    timerValue = 31;
    timerObj =  setInterval(manageTime, 1000, -1);
    document.getElementById('game-score').innerText = 0;
    document.getElementById("overlay").style.visibility = 'hidden';
    document.getElementById("leaderboard").style.visibility = 'hidden';
    document.getElementById("page-content").style.visibility = 'visible';
    myForm.style.visibility = 'hidden';
    getQuestion();
}

function gameOver(){
    clearInterval(timerObj);
    timerObj = null;
    score = parseInt(document.getElementById('game-score').innerText, 10);
    document.getElementById('form-score').innerText = score;
    document.getElementById("page-content").style.visibility = 'hidden';
    document.getElementById("leaderboard").style.visibility = 'visible';
    getLeaderboard();
    myForm.style.visibility = 'visible';
}

function checkAnswer(element){
    answer = element.getAttribute('value');
    fetch('http://127.0.0.1:5000/get_answer/' + current_question_id)
    .then(res => res.json())
    .then(data => {
        if (data.answer === answer){
            score = parseInt(document.getElementById('game-score').innerText, 10) + 1;
            document.getElementById('game-score').innerText = score;
            manageTime(3);
            getQuestion();
        }
        else{
            manageTime(-5)
            getQuestion();
        }
    });
}

function getQuestion(){
    fetch('http://127.0.0.1:5000/get_question')
    .then(res => res.json())
    .then(data => {
        current_question_id = data.id;
        document.getElementById('question').innerText = data.question;
        document.getElementById('choice0').innerText = data.question_choices[0];
        document.getElementById('choice1').innerText = data.question_choices[1];
        document.getElementById('choice2').innerText = data.question_choices[2];
        document.getElementById('choice3').innerText = data.question_choices[3];
        document.getElementById('choice0').setAttribute('value', data.question_choices[0]);
        document.getElementById('choice1').setAttribute('value', data.question_choices[1]);
        document.getElementById('choice2').setAttribute('value', data.question_choices[2]);
        document.getElementById('choice3').setAttribute('value', data.question_choices[3]);
    });
}

function getLeaderboard(){
    fetch('http://127.0.0.1:5000/get_leaderboard')
    .then(res => res.json())
    .then(data => {
        tableElement = document.getElementById('leaderboard-table');
        tableElement.innerHTML = '';
        for(let i = 0; i < data.leaderboard.length; i++){
            let row = tableElement.insertRow(i);
            let cell1 = row.insertCell(0);
            cell1.innerHTML = i + 1;
            let cell2 = row.insertCell(1);
            cell2.innerHTML = data.leaderboard[i].name;
            let cell3 = row.insertCell(2);
            cell3.innerHTML = data.leaderboard[i].score;
        }
    });
}

function manageTime(offset=-1){
    timerValue += offset;
    document.getElementById("game-timer").innerText = timerValue;
    if(timerValue <= 0){
        gameOver();
    }
}

