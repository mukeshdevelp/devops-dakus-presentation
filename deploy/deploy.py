from flask import Flask, request
import subprocess
import json


app = Flask(__name__)

IMAGE = "msmukeshkumarsharma/demo-app-npm-v2"
CONTAINER = "myapp"
PORT = "3000"

CONTAINER = "myapp"
PORT = "3000"

def deploy():
    run(f"docker pull {IMAGE}:latest")
    run(f"docker stop {CONTAINER} || true")
    run(f"docker rm {CONTAINER} || true")
    run(f"""
docker run -d \
  --name {CONTAINER} \
  --restart always \
  -p {PORT}:{PORT} \
  {IMAGE}:latest
""")

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
