from flask import Flask, request
import subprocess
import json
# running app point
app = Flask(__name__)

IMAGE = "msmukeshkumarsharma/demo-app-npm-v2"
CONTAINER = "myapp"
PORT = "3000"

def sh(cmd):
    print(f"→ {cmd}")
    subprocess.run(cmd, shell=True, check=False)

def deploy():
    sh(f"docker pull {IMAGE}:latest")
    sh(f"docker stop {CONTAINER} || true")
    sh(f"docker rm {CONTAINER} || true")
    sh(
        f"docker run -d "
        f"--name {CONTAINER} "
        f"--restart always "
        f"-p {PORT}:{PORT} "
        f"{IMAGE}:latest"
    )

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        payload = request.get_json()
        print("Received Webhook:")
        print(json.dumps(payload, indent=2))
    except:
        print("Received Webhook (no JSON body)")

    print("Deploying new version...")
    deploy()
    return "OK", 200

if __name__ == "__main__":
    print("Listening for Docker Hub webhooks on port 5001 ...")
    app.run(host="0.0.0.0", port=5001)
