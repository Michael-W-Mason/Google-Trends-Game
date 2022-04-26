let countdown = setInterval(manageTime, 1000);
function manageTime(){
    let timer = document.getElementById("game-timer").innerText
    timer -= 1;
    document.getElementById("game-timer").innerText = timer;
}

function gameOver(){

}