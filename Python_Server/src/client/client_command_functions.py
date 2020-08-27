import sys
sys.path.insert(1, "/home/ricky/Code/Python_Projects/Python_Projects/Python_Server/src")
import bash_functions as bash


def navigate_client_command(client_socket):

    while True:
        print("Current path: " + bash.get_current_directory() + "\n")

        bash.save_file_list()
        files_list = bash.read_file_list()
        bash.delete_file_list()
        print(files_list)

        command = input("Choose command: ")
        command = command.upper()

        if command == "GO":
            res = go_command(client_socket, files_list, "CLIENT")
            if res == "EXIT CLIENT":
                return

        elif command == "DOWNLOAD" or command == "EXIT":
            print()
            print("Changing to server database...")
            client_socket.send("EXIT UPLOAD".encode())
            return

        elif command == "UPLOAD":
            transfer_file_command(client_socket, files_list, "UPLOAD")

        else:
            print("That's not a command.")
            print("Command list: go, download, upload, stream, move, exit\n")


def go_command(client_socket, files_list, file_database):
    go_where = "___"

    while go_where not in files_list:
        go_where = input("Where: ")
        print()
        go_where = go_where.upper()

        if go_where == "BACK":

            if file_database == "SERVER":
                # Send BACK message to server_database
                client_socket.send(go_where.encode())
            elif file_database == "CLIENT":
                # Go back in client_database
                bash.change_directory("..")
            return

        elif go_where == "CLIENT" and file_database == "SERVER":
            print()
            print("Changing to client database...")
            bash.go_client_database()

            navigate_client_command(client_socket)
            return

        elif go_where == "SERVER" and file_database == "CLIENT":
            print()
            print("Changing to server database...")
            client_socket.send("EXIT UPLOAD".encode())
            return "EXIT CLIENT"

        elif go_where == "SERVER" and file_database == "SERVER":
            print("You are already in the servers' database.\n")
            continue

        elif go_where == "CLIENT" and file_database == "CLIENT":
            print("You are already in the clients' database.\n")
            continue

        else:
            first_letter = go_where[0]
            rest = go_where[1:].lower()
            go_where = first_letter + rest + "\n"

            if go_where not in files_list:
                print("That's not a directory. Try again.\n")

        # Deletes '\n' in the end of string for sending
        go_where = go_where[0:-1]

        if file_database == "SERVER":
            # Send to change to new directory in server_database
            client_socket.send(go_where.encode())
            #print("Go where: " + go_where)
        elif file_database == "CLIENT":
            # Change to new directory in client_database
            bash.change_directory(go_where)

        return


def transfer_file_command(client_socket, files_list, transfer_type):

    transfer_what = "___"

    while (transfer_what + "\n") not in files_list:
        transfer_what = input("What: ")
        print()

        if (transfer_what + "\n") not in files_list:
            print("That's not a valid file. Try again.\n")

        elif transfer_type == "DOWNLOAD":
            download_command(client_socket, transfer_what)

        elif transfer_type == "UPLOAD":
            upload_command(client_socket, transfer_what)
            return

    return


def download_command(client_socket, download_what):

    client_socket.send(download_what.encode())          #diff
    file_size_str = client_socket.recv(1024).decode()   #diff

    print("File size in Bytes: %s" % file_size_str)

    file_size_int = int(file_size_str)
    byte_counter = 0
    packet_size = 1024

    with open(download_what, "wb") as f:
        print("Downloading...")
        while byte_counter < file_size_int:

            if (file_size_int - byte_counter) < 1024:
                packet_size = file_size_int - byte_counter

            data = client_socket.recv(packet_size)
            f.write(data)
            byte_counter += 1024

        f.close()
        print("Download complete\n")
        return


def upload_command(client_socket, upload_what):
    client_socket.send("UPLOAD FILE".encode())
    file_size_str = bash.get_file_size(upload_what)

    print("File size in Bytes: %s" % file_size_str)
    print("Uploading...")

    # Send file name and size
    client_socket.send((upload_what + "\n" + file_size_str).encode())

    f = open(upload_what, "rb")
    l = f.read(1024)
    while (l):
        client_socket.send(l)
        l = f.read(1024)
    f.close()

    print("Upload complete\n")

    return