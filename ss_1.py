# File Operation

# with open ("Day14\Readme.md","r") as f:
#     print(f.read())

# with open("Day14\Readme1.md","w") as f:
#     f.write()

########################################################
# Environment variable

# import os
# print(os.getenv("Path1"))
# os.environ['Veda']='Dhole'
# print(os.getenv("Veda"))
########################################################
# Subprocess

# import subprocess
# res = subprocess.run(['tasklist'], capture_output=True, text=True, shell=True)
# if "Docker Desktop.exe" in res.stdout:
#     print("✅ Docker is running.")
# else:
#     print("❌ Docker is NOT running.")

# res = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True)

# if res.returncode == 0:
#     branch_name = res.stdout.strip() # .strip() removes the newline character
#     print(f"🚀 Deploying from branch: {branch_name}")
# else:
#     print("⚠️ Not a git repository or Git is not installed.")

# # res = subprocess.run(['ls','-l'],capture_output=True,text=True)
# res = subprocess.run(['dir'],capture_output=True,text=True, shell=True)
#print(res.stdout)

########################################################
# API and JSON Handling

# import requests
# import json
# res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# data = res.json()
# with open("Practice_set02\\sample.json","w") as f:
#     json.dump(data, f, indent=4)

# with open("Practice_set02\\sample.json","r") as f:
#     data = json.load(f)
#     print(data)

########################################################

# Basic Logging steup

# import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("This is info log")

########################################################

# Working with Databases

# import sqlite3
# conn = sqlite3.connect('example.db')
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTX users (id INTIGER PRIMARY KEY,name TEXT)')
# conn.commit()
# conn.close()
########################################################

# AUtomation with libraries
# Using Paramiko for SSH

# import paramiko
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh.connect('host',username="user",password='pwd')

# move file from local to remote and vice versa
# sftp_client = ssh.open_sftp()
# sftp_client.get("remote path","local path")
# sftp_client.put("local path", "remote path")
# stdin, stdout, stderr = ssh.exec_command('ls')
# print(stdout.read().decode())

# sftp_client.close()
# ssh.close()

########################################################
# Exception handling

try:
    # code that raise exception
    pass
except Exception as e:
    print("Error occurred",e)

########################################################
# Docker integration

import docker
client = docker.from_env()
containers = client.containers.list()
# for c in containers:
#     print(c.name)

for c in containers:
    if "test" in c.name:
        print(f"Stopping container: {c.name}")
        c.stop()
########################################################


########################################################


########################################################
