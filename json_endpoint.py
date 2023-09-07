from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/get_info_in_json', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if not slack_name or not track:
        return jsonify({"error": "slack_name and track are required parameters"}), 400

    current_day = datetime.datetime.utcnow().strftime('%A')
    current_utc_time = datetime.datetime.utcnow() + datetime.timedelta(hours=2)

    github_url_file = "https://github.com/yourusername/yourrepository/blob/main/yourscript.py"
    github_url_source = "https://github.com/yourusername/yourrepository"

    response_data = {
        "slack_name": "Micheal_Arifajogun",
        "current_day": current_day,
        "utc_time": current_utc_time.strftime('%Y-%m-%d %H:%M:%S'),
        "track": "backend",
        "github_file_url": github_url_file,
        "github_repo_url": github_url_source,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
