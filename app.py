from flask import Flask, jsonify, render_template, request, redirect, url_for
import webbrowser
import threading
import subprocess

app = Flask(__name__)

# Biến toàn cục để lưu trữ kết quả chuẩn đoán
diagnosis_result = ""

@app.route('/api/voice', methods=['POST'])
def call_voice_api():
    return jsonify({"message": "Voice API called"})

@app.route('/api/symptoms', methods=['POST'])
def call_symptoms_api():
    # Thực hiện hành động cho symptoms API ở đây
    subprocess.run(["python", "Ai/test.py"])  # Chạy file data.py
    return jsonify({"message": "Symptoms API called"})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnosis', methods=['GET', 'POST'])
def diagnosis():
    global diagnosis_result
    if request.method == 'POST':
        diagnosis_result = request.json['result']  # Giả sử kết quả được gửi từ một form hoặc API khác
        return redirect(url_for('show_diagnosis'))
    return render_template('diagnosis.html')

@app.route('/show-diagnosis')
def show_diagnosis():
    return render_template('show_diagnosis.html', diagnosis=diagnosis_result)

def open_browser():
    webbrowser.open_new('http://localhost:5000/')

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()  # Đợi một chút để server khởi động
    app.run(debug=True, use_reloader=False)
