# Working with YAML

# import yaml #pip install pyyaml
# with open("Practice_set02\\test.yaml","r") as f:
#     data = yaml.safe_load(f)
#     print(data)

# with open("Practice_set02\\test2.yaml","w") as f:
#     yaml.dump(data,f,sort_keys=False,default_flow_style=False,indent=2)

############################################################################

# Parsing command-line arguments
# import argparse
# parser = argparse.ArgumentParser(description="process some inputs: ")
# parser.add_argument('--num',type=int,help='an integer')
# args = parser.parse_args()
# print(args.num)
# run as : python Practice_set02/ss_2.py --num 4

# import sys
# n1 = int(sys.argv[1])
# operation = sys.argv[2]
# n2 = int(sys.argv[3])
# print(n1 + n2)
############################################################################

# Monitoring system resources
# import psutil
# print(f"CPU usage: {psutil.cpu_percent()}%")
# print(f"Memory usage: {psutil.virtual_memory().percent}%")
############################################################################

#Handling HTTP Requests with Flask
# from flask import Flask, jsonify
# app = Flask(__name__)

# @app.route('/health',methods=['GET'])
# def hc():
#     return jsonify({'status':'healthy'})
# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=5000)
############################################################################

# Creating Docker container

# import docker
# client = docker.from_env()
# containers = client.containers.run('ubuntu','echo Hello World',detach=True)
# containers.wait()
# print(containers.logs().decode('utf-8'))
############################################################################

# Scheduling Tasks
# import schedule
# import time

# def job():
#     print("Running scheduled job...")
# # Schedule for a specific time (24-hour format)
# # schedule.every().day.at("09:00").do(job)
# schedule.every(1).minutes.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

############################################################################

# Version Control with Git

# import git

# # Clone a repo to a local folder
# git.Repo.clone_from("https://github.com/user/repo.git", "D:/DevOps/local_repo")
# print("Repository cloned successfully!")

# repo = git.Repo(r"D:\DevOps\Ansible")
# repo.git.add('D:\\DevOps\\Ansible\\Day01\\installation.txt')
# repo.index.commit("added file")
############################################################################

# Email Notification

# import smtplib
# from email.mime.text import MIMEText

# msg = MIMEText("This is body of email")
# msg['Subject']='Email subject'
# msg['From']='sender@gmail.com'
# msg['To']='receipient@gmail.com'

# with smtplib.SMTP('smtp.email.com',587) as server:
#     server.starttls()
#     server.login('your_user','your_app_pwd')
#     server.send_message(msg)

############################################################################

# Creating virtual env

# import os
# import subprocess

# subprocess.run(['python','-m','venv','myenv']) # D:\Zero_Touch\myenv
# # os.system('myenv\\Scripts\\activate') # no need to activate here

# #add path to env var
# venv_python = os.path.join("myenv", "Scripts", "python.exe")

# # 3. Use that specific python to install something
# subprocess.run([venv_python, "-m", "pip", "install", "requests"])

# # 4. Run your script using that environment
# subprocess.run([venv_python, "your_script.py"], check=True)

# os.system('source myenv/bin/activate') # linux/mac
############################################################################

# Integrating with CI/CD Tools

import requests

url = ""
res = requests.post(url,auth=('user','token'))
print(res.status_code)

############################################################################
