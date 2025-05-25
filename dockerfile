# 1. Use a base image with Python already installed
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy everything in your current folder into the container
COPY . .

# 4. Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Command to run your chatbot script
CMD ["python", "mistral_chatbot.py"]
