import os


def get_current_directory():
    cwd = os.getcwd()
    if "/Client_Database" in cwd:
        database_index = cwd.index("Client_Database")
    elif "/Server_Database" in cwd:
        database_index = cwd.index("Server_Database")
    else:
        return cwd

    cwd = cwd[database_index:]
    return cwd


def get_file_size(file_name):
    file_size = os.stat(file_name).st_size
    file_size_str = str(file_size)
    return file_size_str


def go_client_database():
    os.chdir("/home/ricky/Code/Python_Projects/Python_Projects/Python_Server/Client_Database")
    return


def go_server_database():
    os.chdir("/home/ricky/Code/Python_Projects/Python_Projects/Python_Server/Server_Database")
    return


def change_directory(directory_name):
    os.chdir(directory_name)
    return


def save_file_list():
    os.system('ls > /home/ricky/Code/Python_Projects/Python_Projects/Python_Server/file_list.txt')
    return

def delete_file_list():
    os.system('rm /home/ricky/Code/Python_Projects/Python_Projects/Python_Server/file_list.txt')
    return

def read_file_list():
    f = open('/home/ricky/Code/Python_Projects/Python_Projects/Python_Server/file_list.txt', "r")
    if f.mode == "r":
        contents = f.read()
    return contents

def list_files():
    os.system("ls")
    return

def move_file():
    return

