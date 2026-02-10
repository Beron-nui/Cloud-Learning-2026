# StellarOrbit Docker Deployment Guide

This guide will help you containerize your StellarOrbit application and deploy it to GitHub.

## 📋 Prerequisites

- Docker Desktop installed ([Download here](https://www.docker.com/products/docker-desktop))
- Git installed ([Download here](https://git-scm.com/downloads))
- GitHub account
- Docker Hub account (optional, for hosting Docker images)

---

## 🐳 Step 1: Prepare Your Project

### 1.1 Update Your Project Structure

Ensure your project has the following files in the root directory:

```
StellarOrbit/
├── backend/
├── frontend/
├── fire/
├── .ipynb_checkpoints/
├── Dockerfile              # Create this
├── .dockerignore          # Create this
├── docker-compose.yml     # Create this (optional)
├── requirements.txt
├── kaggle.json
├── README.md
├── Train_Fire_Model.ipynb
└── Train_Water_Model.ipynb
```

### 1.2 Update requirements.txt

Make sure your `requirements.txt` includes all necessary dependencies:

```txt
flask==2.3.0
numpy==1.24.0
pandas==2.0.0
scikit-learn==1.3.0
tensorflow==2.13.0
# Or pytorch if you're using it
# torch==2.0.0
jupyter==1.0.0
kaggle==1.5.16
python-dotenv==1.0.0
# Add other dependencies as needed
```

### 1.3 Create .gitignore (if not exists)

Add a `.gitignore` file to exclude sensitive and unnecessary files:

```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
*.egg-info/

# Jupyter
.ipynb_checkpoints/

# Credentials (IMPORTANT!)
kaggle.json
*.env
.env

# Models (if too large)
*.h5
*.pkl
*.pt
*.pth

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Docker
.dockerignore
```

---

## 🔨 Step 2: Build Docker Image

### 2.1 Build the Image

Open terminal in your project root directory and run:

```bash
# Basic build
docker build -t stellarorbit:latest .

# Or build with a specific tag
docker build -t yourusername/stellarorbit:v1.0 .
```

### 2.2 Verify the Build

```bash
# List Docker images
docker images | grep stellarorbit
```

---

## 🚀 Step 3: Run Docker Container

### Option A: Using Docker Command

```bash
# Run the container
docker run -d \
  --name stellarorbit-app \
  -p 5000:5000 \
  -p 3000:3000 \
  -v $(pwd)/models:/app/models \
  -v $(pwd)/data:/app/data \
  stellarorbit:latest

# View running containers
docker ps

# View logs
docker logs stellarorbit-app

# Stop the container
docker stop stellarorbit-app

# Remove the container
docker rm stellarorbit-app
```

### Option B: Using Docker Compose (Recommended)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild and restart
docker-compose up -d --build
```

---

## 📤 Step 4: Push to GitHub

### 4.1 Initialize Git Repository (if not already done)

```bash
cd /path/to/StellarOrbit
git init
```

### 4.2 Add Files to Git

```bash
# Add all files (respecting .gitignore)
git add .

# Or add specific files
git add Dockerfile .dockerignore docker-compose.yml requirements.txt

# Commit changes
git commit -m "Add Docker configuration for containerization"
```

### 4.3 Create GitHub Repository

1. Go to [GitHub](https://github.com) and log in
2. Click the "+" icon → "New repository"
3. Name it: `StellarOrbit` or `stellarorbit2`
4. Choose public or private
5. **DO NOT** initialize with README (you already have one)
6. Click "Create repository"

### 4.4 Link Local Repository to GitHub

```bash
# Add remote repository (replace with your GitHub username)
git remote add origin https://github.com/yourusername/StellarOrbit.git

# Verify remote
git remote -v

# Push to GitHub
git push -u origin main

# If your default branch is 'master', use:
# git push -u origin master
```

### 4.5 If You Get Branch Name Error

```bash
# Rename branch to main (if needed)
git branch -M main

# Then push
git push -u origin main
```

---

## 🐙 Step 5: Push Docker Image to Docker Hub (Optional)

### 5.1 Login to Docker Hub

```bash
docker login
# Enter your Docker Hub username and password
```

### 5.2 Tag and Push Image

```bash
# Tag image
docker tag stellarorbit:latest yourusername/stellarorbit:latest
docker tag stellarorbit:latest yourusername/stellarorbit:v1.0

# Push to Docker Hub
docker push yourusername/stellarorbit:latest
docker push yourusername/stellarorbit:v1.0
```

### 5.3 Update docker-compose.yml to Use Docker Hub Image

```yaml
services:
  backend:
    image: yourusername/stellarorbit:latest
    # Remove 'build' section
```

---

## 🔐 Step 6: Handle Sensitive Data (IMPORTANT!)

### 6.1 Remove kaggle.json from Git

```bash
# If you accidentally committed kaggle.json
git rm --cached kaggle.json
git commit -m "Remove kaggle.json from tracking"
git push
```

### 6.2 Use Environment Variables

Create a `.env` file (add to .gitignore):

```env
KAGGLE_USERNAME=your_username
KAGGLE_KEY=your_api_key
```

Update Dockerfile to use environment variables:

```dockerfile
# Instead of copying kaggle.json, use environment variables
ENV KAGGLE_USERNAME=${KAGGLE_USERNAME}
ENV KAGGLE_KEY=${KAGGLE_KEY}
```

---

## 📝 Step 7: Add GitHub Actions (Optional CI/CD)

Create `.github/workflows/docker-build.yml`:

```yaml
name: Docker Build and Push

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Login to Docker Hub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}
    
    - name: Build and push
      uses: docker/build-push-action@v4
      with:
        context: .
        push: true
        tags: |
          yourusername/stellarorbit:latest
          yourusername/stellarorbit:${{ github.sha }}
```

---

## 🧪 Step 8: Testing

### Test Locally

```bash
# Pull from Docker Hub
docker pull yourusername/stellarorbit:latest

# Run the pulled image
docker run -d -p 5000:5000 yourusername/stellarorbit:latest

# Test endpoints
curl http://localhost:5000/health  # Adjust based on your API
```

### Test from Another Machine

```bash
# Clone repository
git clone https://github.com/yourusername/StellarOrbit.git
cd StellarOrbit

# Run with docker-compose
docker-compose up -d
```

---

## 🔧 Troubleshooting

### Issue: Container exits immediately

```bash
# Check logs
docker logs stellarorbit-app

# Run interactively to debug
docker run -it stellarorbit:latest /bin/bash
```

### Issue: Port already in use

```bash
# Find process using port
lsof -i :5000  # macOS/Linux
netstat -ano | findstr :5000  # Windows

# Kill the process or use different port
docker run -p 8000:5000 stellarorbit:latest
```

### Issue: Cannot connect to Docker daemon

```bash
# Start Docker Desktop
# Or restart Docker service
sudo systemctl restart docker  # Linux
```

---

## 📚 Quick Reference Commands

```bash
# Build
docker build -t stellarorbit:latest .

# Run
docker run -d -p 5000:5000 --name stellarorbit-app stellarorbit:latest

# Stop
docker stop stellarorbit-app

# Remove
docker rm stellarorbit-app

# View logs
docker logs -f stellarorbit-app

# Execute command in container
docker exec -it stellarorbit-app bash

# Docker Compose
docker-compose up -d        # Start
docker-compose down         # Stop
docker-compose logs -f      # Logs
docker-compose restart      # Restart

# Git
git add .
git commit -m "message"
git push origin main
```

---

## 🎯 Next Steps

1. ✅ Test your application locally with Docker
2. ✅ Push to GitHub
3. ✅ Set up CI/CD with GitHub Actions
4. ✅ Deploy to cloud platforms (AWS, GCP, Azure, Heroku)
5. ✅ Set up monitoring and logging
6. ✅ Create comprehensive documentation

---

## 📖 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [GitHub Documentation](https://docs.github.com/)
- [Docker Hub](https://hub.docker.com/)

---

## 💡 Tips

1. **Always** add `kaggle.json` and sensitive files to `.gitignore`
2. Use specific version tags for dependencies, not `latest`
3. Optimize Docker image size by using multi-stage builds
4. Use `.dockerignore` to reduce build context size
5. Document all environment variables needed
6. Set up health checks in your application
7. Use volumes for persistent data

---

Good luck with your deployment! 🚀
