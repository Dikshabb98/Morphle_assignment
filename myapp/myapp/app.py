import os
import datetime
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Diksha Beniwal"

    system_user = subprocess.getoutput("whoami")
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)

    top_output = subprocess.getoutput("top -b -n 1")

    response = f"""
    <h2>Name: {full_name}</h2>
    <h2>User: {system_user}</h2>
    <h3>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h3>
    <h3>TOP output:</h3>
    <pre>{top_output}</pre>
    """

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
