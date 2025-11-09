import os

IMAGE = "msmukeshkumarsharma/demo-app-npm-v2"
CONTAINER = "myapp"
PORT = "3000"

commands = [
    f"docker pull {IMAGE}:latest",
    f"docker stop {CONTAINER} || true",
    f"docker rm {CONTAINER} || true",
    f"docker run -d --name {CONTAINER} --restart always -p {PORT}:{PORT} {IMAGE}:latest",
    "docker run -d --name watchtower --restart always -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower " + CONTAINER + " --interval 30"
]

for cmd in commands:
    print(f"$ {cmd}")
    os.system(cmd)
