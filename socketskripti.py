import socket

def fetch_data(group_id, filename):
    server_address = ('172.20.241.9', 20000)
    buffer_size = 4096  # Määritellään puskuri

    try:
        # Luodaan TCP-socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Yhdistetään palvelimeen
            sock.connect(server_address)
            # Lähetetään group_id rivinvaihdolla
            sock.sendall(f"{group_id}\n".encode())

            # Avataan tiedosto kirjoitustilassa
            with open(filename, 'wb') as file:
                while True:
                    # Vastaanotetaan dataa palvelimelta
                    data = sock.recv(buffer_size)
                    if not data:
                        break
                    # Kirjoitetaan vastaanotettu data tiedostoon
                    file.write(data)

        print(f"Data tallennettu tiedostoon: {filename}")

    except Exception as e:
        print(f"Virhe: {e}")

if __name__ == "__main__":
    group_id = 19
    output_file = "vastaanotetut_datat.txt"
    fetch_data(group_id, output_file)

