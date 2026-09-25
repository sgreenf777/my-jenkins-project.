from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = os.uname().nodename
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Susana's DevOps App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-align: center;
                padding: 50px;
                margin: 0;
            }}
            h1 {{ font-size: 3em; margin-bottom: 20px; }}
            .card {{
                background: rgba(255, 255, 255, 0.2);
                padding: 30px;
                border-radius: 15px;
                display: inline-block;
                margin-top: 30px;
            }}
            .highlight {{ color: #FFD700; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>🌟 Hello from Susana's DevOps App! 🌟</h1>
        <div class="card">
            <p><span class="highlight">Container Hostname:</span> {hostname}</p>
            <p><span class="highlight">Current Time:</span> {current_time}</p>
            <p><span class="highlight">Deployed with:</span> Jenkins + AWS CodePipeline + ECS</p>
        </div>
        <p style="margin-top: 40px;">Toda Raba Yeshua! 🕊️</p>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


