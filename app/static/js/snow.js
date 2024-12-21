// 페이지 로드 시 배경음악 재생
window.addEventListener('load', function() {
    const backgroundMusic = new Audio("{{ url_for('static', filename='sounds/christmas_bgm.mp3') }}");
    backgroundMusic.loop = true;  // 반복 재생
    backgroundMusic.volume = 0.5; // 볼륨 조절
    backgroundMusic.play();
});

function updateCountdown() {
    const countdownElement = document.getElementById("countdown");
    const now = new Date();
    const currentYear = now.getFullYear();
    
    // 크리스마스 날짜 설정 (12월 25일)
    const christmasDate = new Date(currentYear, 11, 25); // 월은 0부터 시작하므로 11은 12월을 의미

    // 현재 날짜가 크리스마스를 지나면 내년 크리스마스를 설정
    if (now > christmasDate) {
        christmasDate.setFullYear(currentYear + 1);
    }

    // 남은 시간 계산
    const timeDiff = christmasDate - now;
    const daysLeft = Math.ceil(timeDiff / (1000 * 60 * 60 * 24)); // 밀리초를 일로 변환

    countdownElement.textContent = `크리스마스까지 ${daysLeft}일 남았습니다!`;
}

// 초기 카운트다운 업데이트
updateCountdown();

// 하루마다 업데이트 (86400000 밀리초)
setInterval(updateCountdown, 1000 * 60 * 60 * 24);


  

function createSnowflake() {
    const snowflake = document.createElement('div');
    snowflake.classList.add('snowflake');
    
    snowflake.style.left = Math.random() * window.innerWidth + 'px';
    snowflake.style.animationDuration = Math.random() * 3 + 2 + 's';
    snowflake.style.opacity = Math.random();
    snowflake.style.fontSize = Math.random() * 10 + 10 + 'px';
    
    snowflake.innerHTML = '❄';
    document.body.appendChild(snowflake);
    
    setTimeout(() => {
        snowflake.remove();
    }, 5000);
}

setInterval(createSnowflake, 100);
