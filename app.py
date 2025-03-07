from flask import Flask
import os
import subprocess
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Surya Bhargav"  
    
    # Get system username
    username = os.environ.get("USER") or os.environ.get("LOGNAME") or os.environ.get("USERNAME") or "unknown"
    
    # Get current IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # Run 'top' command and get output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"
    
    # Create response
    response = f"""
    <pre>
    Name: {full_name}
    Username: {username}
    Server Time (IST): {server_time}
    
    TOP output:
    {top_output}
    </pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 
