import os

def list_of_files(folder):
    
    try:
        files = os.listdir(folder)
        return files, None

    except FileNotFoundError as e:
        print(e)
        return None, "Folder not found"


def main():
    folders = input("Provide folder names : ").split()

    for folder in  folders:
        files, error_msg = list_of_files(folder)
        if files:
            for file in files:
                print(file)
        elif error_msg:
            print("Folder not found error")


if __name__ == "__main__":
    main()
