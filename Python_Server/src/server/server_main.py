import socket
import sys
sys.path.insert(1, "/home/ricky/Code/Python_Projects/Python_Projects/Python_Server/src")
import bash_functions as bash
import server_command_functions as cmd_func

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

    bash.go_server_database()

    while True:
        # Send path message
        path_msg = "Current path: " + bash.get_current_directory()
        client_connected.send(path_msg.encode())

        # Uncomment for debugging
        #print(path_msg)

        # Writes, reads and then deletes file list
        bash.save_file_list()
        files_list = bash.read_file_list()
        bash.delete_file_list()

        # For empty file list
        if not files_list:
            client_connected.send(" ".encode())

        client_connected.send(files_list.encode())

        # Uncomment for debugging
        #print("File list sent.")

        command = client_connected.recv(1024).decode()

        # Uncomment for debugging
        print("Command: " + command)

        # ** Go command is finished **
        if command == "GO":
            go_where = client_connected.recv(1024).decode()

            if go_where == "EXIT UPLOAD" or go_where == "UPLOAD FILE":
                cmd_func.upload_command(client_connected, go_where)
                continue

            # Uncomment for debugging
            print("Go: " + go_where)

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
            l = f.read(1024)
            while (l):
                client_connected.send(l)
                l = f.read(1024)
            f.close()

            print("Upload complete\n")

        elif command == "UPLOAD":

            cmd_func.upload_command(client_connected, None)

            """
            uploading = True

            while uploading:

                msg = client_connected.recv(1024).decode()

                if msg == "EXIT UPLOAD":
                    uploading = False
                    bash.go_server_database()
                    continue

                elif msg == "UPLOAD FILE":

                    # Store uploaded files in "Uploads" folder
                    bash.go_server_database()
                    bash.change_directory("Uploads")

                    # Receive file name and size
                    upload_what = client_connected.recv(1024).decode()
                    separator_index = upload_what.index("\n")
                    file_size_str = upload_what[separator_index + 1:]
                    upload_what = upload_what[:separator_index]

                    file_size_int = int(file_size_str)
                    byte_counter = 0
                    packet_size = 1024

                    print("Downloading file: " + upload_what)

                    with open(upload_what, "wb") as f:

                        while byte_counter < file_size_int:

                            if (file_size_int - byte_counter) < 1024:
                                packet_size = file_size_int - byte_counter

                            data = client_connected.recv(packet_size)
                            f.write(data)
                            byte_counter += 1024

                    f.close()

                    bash.go_server_database()

                    print("Download complete\n")
                    """

    client_connected.close()


