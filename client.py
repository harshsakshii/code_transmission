import socket, json, time
from huffman_encoding_decoding import huffman_encoding, huffman_decoding

def start_client(host='127.0.0.1', port=12345):
    while True:

        # Display menu for user input
        inp = int(input("\nMenu\n-------------------\n1. Text \n2. Text File \n3. Help \n4. Exit \n\nEnter your choice: "))
        
        if inp == 1:
            message = input("\nEnter message to send (type 'exit' to quit): ")
        elif inp == 2:
            filename = input("\nEnter the file path: ")
            with open(filename, 'r') as file:
                message = file.read()
        elif inp == 3:
            print("\nHelp Menu:")
            print("1. Text: Enter a message to send directly.")
            print("2. Text File: Provide the raw path of a text file to send its content.")
            print("3. Help: Displays this help menu.")
            print("4. Exit: Exits the application.")
            client_socket.close()
            continue
        elif inp == 4:
            message = 'exit'
        else:
            print("Invalid option.")
            client_socket.close()
            continue

        # Encode the message
        encoded_message, huffman_codes, _ = huffman_encoding(message)

        # Prepare the data to send
        data = {
            "encoded_message": encoded_message,
            "huffman_codes": huffman_codes
        }
        serialized_data = json.dumps(data)  # Convert to JSON string
        data_length = len(serialized_data)  # Length of serialized data

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            # Send the length of the data first
            client_socket.sendall(str(data_length).encode('utf-8').ljust(16))  # Send length as 16-byte padded string
            
            # Send the actual data
            client_socket.sendall(serialized_data.encode('utf-8'))
            
            # Receive response length from the server
            response_length = int(client_socket.recv(16).strip())  # Receive 16 bytes for response length
            
            # Now receive the actual response data based on the length
            encoded_response = client_socket.recv(response_length).decode('utf-8')

            # Parse and decode the server's response
            response_data = json.loads(encoded_response)
            decoded_response = huffman_decoding(response_data["encoded_response"], response_data["huffman_codes"])

            # Display results
            print("\nMessage sent to server")
            print("Original Message:", message)
            print("Encoded Message:", encoded_message)
            print("Decoded Response from Server:", decoded_response)

            # Log details to file
            with open("client_log.txt", "a") as log_file:
                log_file.write(f"\nTime: {time.ctime()}\n")
                log_file.write(f"Connection details: {host}:{port}\n")
                log_file.write(f"Original Message: {message}\n")
                log_file.write(f"Encoded Message: {encoded_message}\n")
                log_file.write(f"Decoded Response: {decoded_response}\n")
                
        except Exception as e:
            print(f"Error communicating with server: {e}")
        
        finally:
            client_socket.close()

        # Exit loop if user chose to quit
        if message == 'exit':
            break

if __name__ == "__main__":
    start_client()
