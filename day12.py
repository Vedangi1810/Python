import os
def update_server_conf(file_path,key,value):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()

        with open(file_path,"w") as file:
            for line in lines:
                if key in line:
                    file.write(f"{key}={value}\n")
                else:
                    file.write(line)
    else:
        print("File does not exist")


update_server_conf("Day12\\server.conf","MAX_CONNECTIONS","800")
