import socket
import threading
import bash_functions as bash

print("Directories: ")

bash.go_database()
bash.list_files()

valid_input = False

while not valid_input:

    where_to = input("Choose a directory: ")
    where_to = where_to.lower()

    if where_to == "documents":
        bash.go_documents()
        valid_input = True
    elif where_to == "music":
        bash.go_music()
        valid_input = True
    elif where_to == "pictures":
        bash.go_pictures()
        valid_input = True
    elif where_to == "videos":
        bash.go_videos()
        valid_input = True
    else:
        print("That's not a valid directory.")



