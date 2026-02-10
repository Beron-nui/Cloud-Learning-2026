# 🚀 Quick Start: Dockerize & Deploy to GitHub

## Step-by-Step Instructions

### ✅ STEP 1: Add Docker Files to Your Project

1. **Copy these 3 files to your StellarOrbit project root:**
   - `Dockerfile`
   - `.dockerignore`
   - `docker-compose.yml`

2. **Make sure these files are in the same directory as:**
   - `requirements.txt`
   - `README.md`
   - `backend/` folder
   - `frontend/` folder

---

### ✅ STEP 2: Update .gitignore (IMPORTANT!)

**Add these lines to your `.gitignore` file:**

```
# Sensitive files - DO NOT COMMIT
kaggle.json
*.env
.env

# Docker
.dockerignore

# Python
__pycache__/
*.pyc
.ipynb_checkpoints/
venv/
env/
```

---

### ✅ STEP 3: Build Docker Image

Open terminal in your project folder and run:

```bash
docker build -t stellarorbit:latest .
```

**Expected output:** "Successfully built..." and "Successfully tagged stellarorbit:latest"

---

### ✅ STEP 4: Test the Container

```bash
# Start the container
docker run -d --name stellarorbit-test -p 5000:5000 stellarorbit:latest

# Check if it's running
docker ps

# View logs
docker logs stellarorbit-test

# Stop and remove
docker stop stellarorbit-test
docker rm stellarorbit-test
```

---

### ✅ STEP 5: Push to GitHub

#### 5.1 Initialize Git (if not already done)

```bash
git init
```

#### 5.2 Add and Commit Files

```bash
# Add all files
git add .

# Commit
git commit -m "Add Docker configuration for containerization"
```

#### 5.3 Create GitHub Repository

1. Go to https://github.com
2. Click "+" → "New repository"
3. Name: `StellarOrbit` (or `stellarorbit2`)
4. Click "Create repository"
5. **DO NOT** check "Initialize with README"

#### 5.4 Link and Push

```bash
# Replace 'yourusername' with your GitHub username
git remote add origin https://github.com/yourusername/StellarOrbit.git

# Check if main or master branch
git branch

# If no branch, rename to main
git branch -M main

# Push to GitHub
git push -u origin main
```

**🎉 Done! Your code is now on GitHub!**

---

### ✅ STEP 6 (Optional): Push to Docker Hub

#### 6.1 Login to Docker Hub

```bash
docker login
# Enter your Docker Hub username and password
```

#### 6.2 Tag and Push

```bash
# Replace 'yourusername' with your Docker Hub username
docker tag stellarorbit:latest yourusername/stellarorbit:latest

# Push
docker push yourusername/stellarorbit:latest
```

---

### ✅ STEP 7: Use Docker Compose (Recommended)

Instead of manual docker commands, use docker-compose:

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

---

## 🔧 Common Issues & Solutions

### Issue: "Port already in use"

```bash
# Find what's using the port
lsof -i :5000  # macOS/Linux

# Use a different port
docker run -p 8000:5000 stellarorbit:latest
```

### Issue: "Permission denied" on kaggle.json

```bash
chmod 600 kaggle.json
```

### Issue: Container exits immediately

```bash
# Check logs
docker logs stellarorbit-test

# Run interactively to debug
docker run -it stellarorbit:latest /bin/bash
```

### Issue: Cannot connect to Docker daemon

- **Mac/Windows:** Make sure Docker Desktop is running
- **Linux:** Run `sudo systemctl start docker`

---

## 📝 Verify Everything Works

After pushing to GitHub, anyone should be able to:

```bash
# Clone your repository
git clone https://github.com/yourusername/StellarOrbit.git
cd StellarOrbit

# Run with Docker
docker-compose up -d

# Or pull from Docker Hub
docker pull yourusername/stellarorbit:latest
docker run -d -p 5000:5000 yourusername/stellarorbit:latest
```

---

## 🎯 Final Checklist

- [ ] Dockerfile created
- [ ] .dockerignore created
- [ ] docker-compose.yml created
- [ ] .gitignore updated (kaggle.json excluded)
- [ ] Docker image builds successfully
- [ ] Container runs without errors
- [ ] Code pushed to GitHub
- [ ] Docker image pushed to Docker Hub (optional)

---

## 📚 Command Reference

```bash
# Docker
docker build -t stellarorbit:latest .
docker run -d -p 5000:5000 --name stellarorbit stellarorbit:latest
docker ps                          # List running containers
docker logs stellarorbit           # View logs
docker stop stellarorbit           # Stop container
docker rm stellarorbit             # Remove container
docker images                      # List images
docker rmi stellarorbit:latest     # Remove image

# Docker Compose
docker-compose up -d               # Start
docker-compose down                # Stop
docker-compose logs -f             # Logs
docker-compose restart             # Restart
docker-compose ps                  # Status

# Git
git status                         # Check status
git add .                          # Stage all files
git commit -m "message"            # Commit
git push origin main               # Push to GitHub
git pull origin main               # Pull from GitHub
```

---

**Need help?** Check the full guide in `DOCKER_DEPLOYMENT_GUIDE.md`
