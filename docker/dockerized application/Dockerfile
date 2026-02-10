# Use Python 3.10 as base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p models data logs

# Copy kaggle.json to the correct location (if using Kaggle API)
RUN mkdir -p /root/.kaggle && \
    if [ -f kaggle.json ]; then cp kaggle.json /root/.kaggle/; fi && \
    chmod 600 /root/.kaggle/kaggle.json 2>/dev/null || true

# Expose ports (adjust based on your backend/frontend ports)
# Backend port
EXPOSE 5000
# Frontend port (if applicable)
EXPOSE 3000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Default command (adjust based on your main application entry point)
CMD ["python", "backend/app.py"]

# Alternative: If you want to run both backend and frontend
# CMD ["sh", "-c", "cd backend && python app.py & cd ../frontend && npm start"]
