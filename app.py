from flask import Flask
import os
import subprocess
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get full name
    full_name = "Your Full Name Here"  # Replace with your name
    
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown"
    
    # Get current IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # Run htop command and get output
    try:
        htop_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        htop_output = f"Error fetching top output: {str(e)}"
    
    # Create response
    response = f"""
    <pre>
    Name: {full_name}
    Username: {username}
    Server Time (IST): {server_time}
    
    TOP output:
    {htop_output}
    </pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
