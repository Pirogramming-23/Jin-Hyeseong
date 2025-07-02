//gameInit() is called when the game starts
// 시도 가능 횟수 설정, 중복되지 않는 3개의 랜덤한 숫자 설정, html의 input과 결과창의 내용 비움.

let attempts = 9; // 시도 가능 횟수
let answer = []; //정답 배열

document.addEventListener("DOMContentLoaded", () => {
    gameInit();
})

function gameInit() {
    document.getElementById("attempts").textContent = attempts;

    while (answer.length < 3) { // 중복 되지 않는 3개의 랜덤한 숫자 설명
        const rand = Math.floor(Math.random() * 10);
        if(!answer.includes(rand)) answer.push(rand);
    }
    
    // HTML input 및 결과창 초기화
    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";

    document.getElementById("results").innerHTML = "";
    document.getElementById("game-result-img").src = "";
}
console.log(answer);
function check_numbers() {
    const input1 = document.getElementById("number1").value;
    const input2 = document.getElementById("number2").value;
    const input3 = document.getElementById("number3").value;
    const resultImage = document.getElementById("game-result-img");
    const submitButton = document.querySelector(".submit-button");

    if(!input1 || !input2 || !input3) {
        document.getElementById("number1").value = "";
        document.getElementById("number2").value = "";
        document.getElementById("number3").value = "";
        return;
    }

    const guess = [input1, input2, input3];

    // 중복 check
    if (new Set(guess).size < guess.length) {
        alert("서로 다른 3개의 숫자를 입력하세요");
        return;
    }

    let strike = 0;
    let ball = 0;

    for (let i=0; i<3; i++) {
        if(parseInt(guess[i]) === parseInt(answer[i])) strike++;
        else if (answer.includes(parseInt(guess[i]))) ball++;
    }

    const resultsDiv = document.getElementById("results");

    const resultWrapper = document.createElement("div");
    resultWrapper.className = "check-result";

    // 왼쪽 (입력 숫자)
    const left = document.createElement("div");
    left.className = "left";
    left.textContent = guess.join(' ');
    resultWrapper.appendChild(left);

    // 가운데 (:)
    const colon = document.createElement("div");
    colon.textContent = ":";
    resultWrapper.appendChild(colon);

    // 오른쪽 (S, B, O 결과)
    const right = document.createElement("div");
    right.className = "right";

    if (strike === 0 && ball === 0) {
        const out = document.createElement("span");
        out.className = "num-result out";
        out.textContent = "O";
        right.appendChild(out);
    } else {
        if (parseInt(strike) != 0) {
            const s_n = document.createElement("span");
            s_n.className = "num-result";
            s_n.textContent = strike;
    
            const s = document.createElement("span");
            s.className = "num-result strike";
            s.textContent = "S";
            right.append(s_n);
            right.appendChild(s);
        }
        
        if (parseInt(ball) != 0) {
            const b_n = document.createElement("span");
            b_n.className = "num-result";
            b_n.textContent = ball;
    
            const b = document.createElement("span");
            b.className = "num-result ball";
            b.textContent = "B";
            right.appendChild(b_n);
            right.appendChild(b);
        }
    }

    resultWrapper.appendChild(right);
    resultsDiv.appendChild(resultWrapper);

    // 결과창을 맨 아래로 스크롤
    const scrollContainer = document.querySelector('.result-display');
    scrollContainer.scrollTo({
        top: scrollContainer.scrollHeight,
        behavior: 'smooth'
    });

    attempts--;
    document.getElementById("attempts").textContent = attempts;

    if (parseInt(strike) === 3) {
        resultImage.src = "success.png";
        submitButton.disabled = true;
    } else if (parseInt(attempts) === 0) {
        resultImage.src = "fail.png";
        submitButton.disabled = true;
    }

    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";

}