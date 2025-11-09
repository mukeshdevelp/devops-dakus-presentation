from flask import Flask, request
import subprocess

app = Flask(__name__)



@app.route('/deploy', methods=['POST'])
def deploy():
    

    try:
        # Pull latest Docker image
        subprocess.run(
            "docker pull msmukeshkumarsharma/my-flask-docker-app:latest",
            shell=True,
            check=True
        )
        
        # Stop old container if exists
        subprocess.run("docker stop my-app || true", shell=True)
        
        # Remove old container
        subprocess.run("docker rm my-app || true", shell=True)
        
        # Run new container
        subprocess.run(
            "docker run -d --name my-app -p 5000:80 msmukeshkumarsharma/my-flask-docker-app:latest",
            shell=True,
            check=True
        )
        return "Deployment successful!", 200

    except subprocess.CalledProcessError as e:
        return f"Deployment failed: {e}", 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
