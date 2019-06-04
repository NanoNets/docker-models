# Guide to exposing Deep Learning Models through Docker

## What is Docker?

I won't take much of your time explaining this. There are tons of guides that will do a much better job than I ever will. Here's a link to a few of them.

https://github.com/veggiemonk/awesome-docker#what-is-docker

## Why Docker + DL

`As a result, IT can ship faster and run the same app, unchanged, on laptops, data center VMs, and any cloud.`
Package once, run anywhere is why docker is the best suited tool. If you've ever setup Tensorflow or any other tool you'll remember the pain it is to install all the drivers and ensure compatibility with your GPU.


## How to Dockerize

### Clone this Repo

### Install Docker

#### Linux

`curl -fsSL get.docker.com -o get-docker.sh && sudo sh get-docker.sh && rm get-docker.sh`

#### Windows

https://docs.docker.com/docker-for-windows/install/

#### MacOS

https://docs.docker.com/docker-for-mac/install/

### Build Docker

`docker `

### Push to regsitry

## Run

`docker run -p 8081:8080 docker.nanonets.com/gesture-model`
