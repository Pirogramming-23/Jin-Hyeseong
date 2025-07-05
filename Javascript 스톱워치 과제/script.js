let timer;
let miliseconds = 0;
let isRunning = false;
let stopwatchMod = true;

let countdownTime = 0;
let countdownTimer = null;
let isCountdownRunning = false;


const timeDisplay = document.getElementById("time-display");
const timerDisplay = document.getElementById("time-display-timer");
const startButton_s = document.querySelector("#stopwatch .start");
const stopButton_s = document.querySelector("#stopwatch .stop");
const resetButton_s = document.querySelector("#stopwatch .reset");
const startButton_t = document.querySelector("#timer .start");
const stopButton_t = document.querySelector("#timer .stop");
const resetButton_t = document.querySelector("#timer .reset");
const recordList = document.querySelector(".records");
const deleteSelectedBtn = document.querySelector("#record-header i");
const selectAllBtn = document.querySelector("#record-header .circle");
const modeToggleBtn = document.querySelector("#mod-toggle-section .btn");
const timerSetup = document.getElementById("timer");
const stopwatchSetup = document.getElementById("stopwatch")
const title = document.querySelectorAll("#title h2");

let allSelected = false;

modeToggleBtn.addEventListener("click", () => {
    stopwatchMod = !stopwatchMod;

    if (stopwatchMod) {
        modeToggleBtn.textContent = "타이머 모드로 전환";
        document.getElementById("record-section").style.display = "block";
        title[0].style.display = "block";
        title[1].style.display = "none";
        timerSetup.style.display = "none";
        stopwatchSetup.style.display = "block";
        recordList.style.display = "block";
        resetCountdown();
        resetTimer();
        updateDisplay();
    } else {
        modeToggleBtn.textContent = "스톱워치 모드로 전환";
        document.getElementById("record-section").style.display = "none";
        title[0].style.display = "none";
        title[1].style.display = "block";
        stopwatchSetup.style.display = "none";
        timerSetup.style.display = "block";
        recordList.style.display = "none";
        resetTimer();
        resetCountdown();
        updateCountdownDisplay();
    }
});

document.getElementById("set-timer").addEventListener("click", () => {
    const timer_min = parseInt(document.getElementById("min-input").value) || 0;
    const timer_sec = parseInt(document.getElementById("sec-input").value) || 0;
    countdownTime = (timer_min * 60 + timer_sec) * 1000;
    updateCountdownDisplay();
});

function updateCountdownDisplay() {
    const min_t = String(Math.floor(countdownTime / 60000)).padStart(2, "0");
    const sec_t = String(Math.floor(((countdownTime % 60000)/1000))).padStart(2, "0");
    document.getElementById("min-input").value = "";
    document.getElementById("sec-input").value = "";
    timerDisplay.textContent = `${min_t} : ${sec_t}`;
}

function startCountdown() {
    if (isCountdownRunning || countdownTime <= 0) return;
    isCountdownRunning = true;
    countdownTimer = setInterval(() => {
        countdownTime -= 1000;
        updateCountdownDisplay();
        if (countdownTime <= 0) {
            clearInterval(countdownTimer);
            isCountdownRunning = false;
            countdownTime = 0;
            updateCountdownDisplay();
            alert("타이머 종료!");
        }
    }, 1000);
}

function stopCountdown() {
    isCountdownRunning = false;
    clearInterval(countdownTimer);
}

function resetCountdown() {
    clearInterval(countdownTimer);
    isCountdownRunning = false;
    countdownTime = 0;
    updateCountdownDisplay();
}


// 시간 포맷
function formatTime(ms) {
    const sec = String(Math.floor(ms / 1000)).padStart(2, "0");
    const msStr = String(Math.floor((ms % 1000) / 10)).padStart(2, "0");
    return `${sec} : ${msStr}`;
}

// 디스플레이 업데이트
function updateDisplay() {
    timeDisplay.textContent = formatTime(miliseconds);
}

// 타이머 시작
function startTimer() {
    if (isRunning) return;
    isRunning = true;
    timer = setInterval(() => {
        miliseconds += 10;
        updateDisplay();
    }, 10);
}

// 타이머 정지
function stopTimer() {
    isRunning = false;
    clearInterval(timer);
    addRecord();
}

// 타이머 리셋
function resetTimer() {
    isRunning = false;
    clearInterval(timer);
    miliseconds = 0;
    updateDisplay();
}

// 기록 추가
function addRecord() {
    const li = document.createElement("li");
    li.className = "record-item";
    li.innerHTML = `
        <div class="circle"></div>
        <span>${formatTime(miliseconds)}</span>
        <span class="delete" style = "cursor: pointer">❌</span>
    `;

    const circle = li.querySelector(".circle");
    const deleteBtn = li.querySelector(".delete");

    // 선택 토글
    circle.addEventListener("click", () => toggleSelection(li, circle));

    // 삭제 기능
    deleteBtn.addEventListener("click", () => {
        li.remove();
        updateSelectAllState();
    });

    recordList.appendChild(li);
    updateSelectAllState();
}

// 선택된 항목 삭제
deleteSelectedBtn.addEventListener("click", () => {
    const selectedItems = recordList.querySelectorAll(".record-item.selected");
    selectedItems.forEach(item => item.remove());
    updateSelectAllState();
});

// 전체 선택/해제
selectAllBtn.addEventListener("click", () => {
    toggleAllSelection();
});

// 개별 선택 토글
function toggleSelection(li, circle) {
    li.classList.toggle("selected");
    circle.classList.toggle("selected");
    updateSelectAllState();
}

// 전체 선택 토글
function toggleAllSelection() {
    const items = recordList.querySelectorAll(".record-item");
    allSelected = !allSelected;

    items.forEach(item => {
        const circle = item.querySelector(".circle");
        if (allSelected) {
            item.classList.add("selected");
            circle.classList.add("selected");
        } else {
            item.classList.remove("selected");
            circle.classList.remove("selected");
        }
    });

    updateSelectAllButton();
}

// 전체 선택 버튼 UI 동기화
function updateSelectAllButton() {
    if (allSelected) {
        selectAllBtn.classList.add("selected");
    } else {
        selectAllBtn.classList.remove("selected");
    }
}

// 전체 선택 상태 계산
function updateSelectAllState() {
    const total = recordList.querySelectorAll(".record-item").length;
    const selected = recordList.querySelectorAll(".record-item.selected").length;

    allSelected = total > 0 && total === selected;
    updateSelectAllButton();
}

// 버튼 이벤트
startButton_s.addEventListener("click", startTimer);
stopButton_s.addEventListener("click", stopTimer);
resetButton_s.addEventListener("click", resetTimer);
startButton_t.addEventListener("click", startCountdown);
stopButton_t.addEventListener("click", stopCountdown);
resetButton_t.addEventListener("click", resetCountdown);