import socket
import sys
import server_command_functions as cmd_func
sys.path.insert(1, "..")
import bash_functions as bash

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 15000

while port < 15003:
    try:
        server_socket.bind(("", port))

        break
    except:
        port += 1

print("Socket binded to port %d" % port)

server_socket.listen(1)

while True:
    client_connected, client_address = server_socket.accept()
    print("Got connection from", client_address)
    print()

    bash.go_server_database()

    while True:
        # Send path message
        path_msg = "Current path: " + bash.get_current_directory()
        client_connected.send(path_msg.encode())

        # Uncomment for debugging
        # print(path_msg)

        # Writes, reads and then deletes file list
        bash.save_file_list()
        files_list = bash.read_file_list()
        bash.delete_file_list()

        # For empty file list
        if not files_list:
            client_connected.send(" ".encode())

        client_connected.send(files_list.encode())

        # Uncomment for debugging
        # print("File list sent.")

        command = client_connected.recv(1024).decode()

        # Uncomment for debugging
        # print("Command: " + command)

        # ** Go command is finished **
        if command == "GO":
            go_where = client_connected.recv(1024).decode()

            if go_where == "EXIT UPLOAD" or go_where == "UPLOAD FILE":
                cmd_func.upload_command(client_connected, go_where)
                continue

            # Uncomment for debugging
            # print("Go: " + go_where)

            if go_where == "BACK":
                bash.change_directory("..")
            else:
                bash.change_directory(go_where)

        # ** Exit command is finished **
        elif command == "EXIT":
            break

        elif command == "DOWNLOAD":
            download_what = client_connected.recv(1024).decode()
            file_size_str = bash.get_file_size(download_what)
            client_connected.send(file_size_str.encode())

            print("Uploading file: " + download_what)

            f = open(download_what, "rb")
            lel = f.read(1024)
            while lel:
                client_connected.send(lel)
                lel = f.read(1024)
            f.close()

            print("Upload complete\n")

        elif command == "UPLOAD":

            cmd_func.upload_command(client_connected, None)

    client_connected.close()


