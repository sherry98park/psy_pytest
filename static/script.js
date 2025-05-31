// 문제 로딩
window.onload = function () {
    fetch('/get_question')
        .then(response => response.json())
        .then(data => {
            document.getElementById('python-question').textContent = data.question;
        });
};

// 정답 제출
function submitAnswer() {
    const userAnswer = document.getElementById('user-answer').value;

    fetch('/check_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ answer: userAnswer })
    })
        .then(response => response.json())
        .then(data => {
            const resultText = document.getElementById('result-text');
            if (data.correct) {
                resultText.textContent = '🎉 정답입니다!';
                resultText.style.color = '#00e676';
            } else {
                resultText.textContent = `❌ 오답입니다. 정답은: ${data.correct_answer}`;
                resultText.style.color = '#ff5252';
            }
        });
}
