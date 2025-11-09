# Step 1: Base image
FROM python:3.10-slim

# Step 2: Set working directory inside the container
WORKDIR /app

# Step 3: Copy your project files into the container
COPY . /app

# Step 4: Install dependencies (if you have requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose a port (Flask default = 5000)
EXPOSE 5000

# Step 6: Command to run the app
CMD ["python", "app.py"]
