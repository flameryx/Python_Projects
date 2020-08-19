import os

def get_current_directory():
    cwd = os.getcwd()
    database_index = cwd.index("Database")
    cwd = cwd[database_index:]
    return cwd

def go_database():
    os.chdir("../Database")
    return

def go_documents():
    go_database()
    os.chdir("Documents")
    cwd = get_current_directory()
    print("Current directory: ", cwd)
    os.system("ls -l")
    save_file_list()
    return

def go_music():
    go_database()
    os.chdir("Music")
    cwd = get_current_directory()
    print("Current directory: ", cwd)
    os.system("ls -l")
    save_file_list()
    return

def go_videos():
    go_database()
    os.chdir("Videos")
    cwd = get_current_directory()
    print("Current directory: ", cwd)
    os.system("ls -l")
    save_file_list()
    return

def go_pictures():
    go_database()
    os.chdir("Pictures")
    cwd = get_current_directory()
    print("Current directory: ", cwd)
    os.system("ls -l")
    save_file_list()
    return

def save_file_list():
    os.system('ls > ../../file_list.txt')
    return

def delete_file_list():
    os.system('rm ../../file_list.txt')
    return

def list_files():
    os.system("ls")
    return


