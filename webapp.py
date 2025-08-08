# dashboard.py
from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def show_logs():
    # Read spoof log
    try:
        with open('logs/spoof_log.txt', 'r') as f:
            spoof_lines = f.readlines()
    except FileNotFoundError:
        spoof_lines = ["No spoofed IPs logged yet."]

    # Read all IPs log
    try:
        with open('logs/all_ips.txt', 'r') as f:
            all_ip_lines = f.readlines()
    except FileNotFoundError:
        all_ip_lines = ["No IPs detected yet."]

    # Build spoof log list
    spoof_list = "".join([f"<li>{line.strip()}</li>" for line in spoof_lines])
    all_ip_list = "".join([f"<li>{line.strip()}</li>" for line in all_ip_lines])

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>IP Spoofing Dashboard</title>
        <meta http-equiv="refresh" content="5">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #1e1e2f;
                color: #ffffff;
                padding: 20px;
            }}
            h2 {{
                color: #00ffff;
            }}
            .log-section {{
                margin-bottom: 40px;
            }}
            ul {{
                background-color: #2e2e3e;
                padding: 20px;
                border-radius: 8px;
                list-style-type: none;
            }}
            li {{
                padding: 10px;
                margin-bottom: 8px;
                background-color: #3e3e5e;
                border-left: 5px solid #00ffff;
                border-radius: 4px;
            }}
        </style>
    </head>
    <body>
        <div class="log-section">
            <h2>📡 All Detected IPs</h2>
            <ul>{all_ip_list}</ul>
        </div>

        <div class="log-section">
            <h2>🚨 Spoofing Alerts</h2>
            <ul>{spoof_list}</ul>
        </div>
    </body>
    </html>
    """

    return Response(html, mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True)
