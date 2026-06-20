# mini-rag

This is a minimal implementation of the RAG model for question answering

## Requirments

- Python 3.11 or later

### Install Python using Miniconda
1) Download and install Miniconda from [here](https://www.anaconda.com/docs/getting-started/miniconda/install/windows-cli-install#command-prompt) for Windows users or from [here](https://www.anaconda.com/docs/getting-started/miniconda/install/linux-install) for Linus users.
2) Create new environment using the following command:
```bash
$ conda create -n mini-rag-app python=3.11
```
3) Activate the environment using the following command:
```bash
$ conda activate mini-rag-app
```

### Optional: Setup your command line interface for better readability
```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$"
```
## Installations

### Required Packages
Use this command to install packages:
```bash
$ pip install -r requirements.txt
```

### Setup the environment variables
```bash
cp .env.example .env
```
Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value. 

## Run FastApi server
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000 
```
### To run from same machine
```bash
http://localhost:5000/
```
### To run from other devices on the same network
```bash
https://YOUR_IP_ADDRESS:5000/
```
To find your IP address
```bash
ip addr show
# or
hostname -I
```

## Postman Collection
Download Postman collection from [\assets\mini-rag-app.postman_collection.json](\assets\mini-rag-app.postman_collection.json)  

