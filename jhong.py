from flask import Flask, jsonify
from flask_cors import CORS
import logging

# Suppress default Flask logs
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
CORS(app)

# Shared state
state = {
    "img": False,
    "bg": False,
    "all": False,
    "full": False
}

@app.route('/status')
def status():
    return jsonify(state)

@app.route('/reset')
def reset():
    for key in state:
        state[key] = False
    return jsonify({"message": "All states reset."})

@app.route('/set/<flag>/<action>')
def set_flag(flag, action):
    if action not in ["on", "off"]:
        return jsonify({"error": "Invalid action, use 'on' or 'off'"}), 400

    value = action == "on"

    if flag in state:
        state[flag] = value
        print(f"[+] {flag} set to {value}.")
        return jsonify({"message": f"{flag} set to {value}."})
    elif flag == "all":
        state["img"] = state["bg"] = state["all"] = value
        return jsonify({"message": f"All features set to {value}."})
    else:
        return jsonify({"error": "Invalid flag"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
