import sys
sys.path.insert(1, "..")
import bash_functions as bash


def upload_command(client_connected, message):
    uploading = True

    if message:
        msg = message

    while uploading:

        if not message:
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

            message = None
