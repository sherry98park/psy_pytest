from flask import Flask, render_template, jsonify, request
import io
import contextlib

app = Flask(__name__)

# 예시 파이썬 문제 리스트
QUESTIONS = [
    {
        "code": "a = 5\nb = 3\nprint(a + b)",
        "output": "8"
    },
    {
        "code": "for i in range(3):\n    print(i)",
        "output": "0\n1\n2"
    },
    {
        "code": "def greet(name):\n    return 'Hello ' + name\n\nprint(greet('Python'))",
        "output": "Hello Python"
    }
]

# 현재 문제 인덱스 (간단히 첫 번째 문제로 고정)
CURRENT_INDEX = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_question')
def get_question():
    question = QUESTIONS[CURRENT_INDEX]["code"]
    return jsonify({"question": question})


@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    user_answer = data.get("answer", "").strip()

    correct_answer = QUESTIONS[CURRENT_INDEX]["output"].strip()

    # 줄바꿈과 공백을 무시하고 비교할 수도 있음
    is_correct = user_answer == correct_answer

    return jsonify({
        "correct": is_correct,
        "correct_answer": correct_answer
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
