import socket
import sys
sys.path.insert(1, "..")
import bash_functions as bash
import client_command_functions as cmd_func

client_socket = socket.socket()
port = 15000

# Uncomment for remote host connection
ip_address = input("Write servers' IP: ")

while port < 15003:
    try:
        # Uncomment for remote host connection
        client_socket.connect((ip_address, port))

        # Uncomment for local host connection
        # client_socket.connect(("localhost", port))
        break
    except:
        port += 1

print("Socket connected to NUBE on port %d" % port)

while True:

    path_msg = client_socket.recv(1024).decode()
    print(path_msg + "\n")
    files_list = client_socket.recv(1024).decode()
    print(files_list)

    command = input("Choose command: ")
    command = command.upper()

    #Send Command
    client_socket.send(command.encode())

    # ** Go command is finished **
    if command == "GO":
        cmd_func.go_command(client_socket, files_list, "SERVER")

    elif command == "EXIT":
        client_socket.close()
        exit()

    elif command == "DOWNLOAD":
        # Store downloaded files in Downloads Folder
        bash.go_client_database()
        bash.change_directory("Downloads")

        cmd_func.transfer_file_command(client_socket, files_list, "DOWNLOAD")

        # Go back to main database folder
        bash.go_client_database()

    elif command == "UPLOAD":
        print()
        print("Changing to client database...")
        bash.go_client_database()

        cmd_func.navigate_client_command(client_socket)

    #elif command == "STREAM":

    #elif command == "MOVE":

    #elif command == "DELETE":

    else:
        print("That's not a command.")
        print("Command list: go, download, upload, stream, move, exit\n")


client_socket.close()