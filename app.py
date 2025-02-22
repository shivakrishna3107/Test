from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)  # Corrected __name__

@app.route('/')
def home():
    return htop()  # Calls the /htop function

@app.route('/htop')
def htop():
    name = ""  # Replace with your full name
    username = os.getenv("USER", "codespace")  # Fetch the system username safely
    
    # Get current IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get full top output without limiting lines
    top_output = subprocess.getoutput("top -b -n 1")

    # Extract all PID users using ps command (alternative approach)
    pid_users = subprocess.getoutput("ps -eo user,pid,comm --sort=-pid")

    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    
    <h2>TOP Output:</h2>
    <pre>{top_output}</pre>

    <h2>All PID Users:</h2>
    <pre>{pid_users}</pre>
    """

if __name__ == '__main__':  # Corrected __name__
    app.run(host='0.0.0.0', port=5000)
