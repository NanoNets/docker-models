# Guide to exposing Deep Learning Models through Docker

[![Watch the video](https://media.giphy.com/media/QUQo9nWGMVUiJpWVkD/giphy.gif)]
## How to Dockerize

### Step 1. Clone this Repo

```git clone https://github.com/NanoNets/docker-models.git```

### Step 2. Install Docker

#### Linux

`curl -fsSL get.docker.com -o get-docker.sh && sudo sh get-docker.sh && rm get-docker.sh`

#### Windows

`https://docs.docker.com/docker-for-windows/install/`

#### MacOS

`https://docs.docker.com/docker-for-mac/install/`

### 3. Build Docker

```docker build -t face-model .```

## 4. Run

```docker run -p 5000:5000 face-model```

## 5. Predict

```python camera.py```
