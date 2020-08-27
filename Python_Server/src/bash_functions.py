import os

project_name = "Python_Server"
project_name_length = len(project_name)


def get_full_path():
    cwd = os.getcwd()
    return cwd


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
    path = get_full_path()
    if project_name in path:
        project_name_index = path.index(project_name)

    database_path = path[:project_name_index + project_name_length] + "/Client_Database"
    os.chdir(database_path)
    return


def go_server_database():
    path = get_full_path()
    if project_name in path:
        project_name_index = path.index(project_name)

    database_path = path[:project_name_index + project_name_length] + "/Server_Database"
    os.chdir(database_path)
    return


def change_directory(directory_name):
    os.chdir(directory_name)
    return


def save_file_list():
    path = get_full_path()
    if project_name in path:
        project_name_index = path.index(project_name)

    file_list_path = path[:project_name_index + project_name_length] + "/file_list.txt"
    os.system('ls > ' + file_list_path)
    return


def delete_file_list():
    path = get_full_path()
    if project_name in path:
        project_name_index = path.index(project_name)

    file_list_path = path[:project_name_index + project_name_length] + "/file_list.txt"
    os.system('rm ' + file_list_path)
    return


def read_file_list():
    path = get_full_path()
    if project_name in path:
        project_name_index = path.index(project_name)

    file_list_path = path[:project_name_index + project_name_length] + "/file_list.txt"

    f = open(file_list_path, "r")
    if f.mode == "r":
        contents = f.read()
    return contents


def list_files():
    os.system("ls")
    return


def move_file():
    return


