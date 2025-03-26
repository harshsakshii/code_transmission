import socket, json
from huffman_encoding_decoding import huffman_encoding, huffman_decoding

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(10)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"\nConnection from {addr}")

        # Receive the length of incoming data first (16 bytes)
        data_length = int(client_socket.recv(16).strip())
        
        # Now receive the actual data based on length
        serialized_data = client_socket.recv(data_length).decode('utf-8')
        received_data = json.loads(serialized_data)
        
        encoded_message = received_data["encoded_message"]
        huffman_codes = received_data["huffman_codes"]

        # Decode the message
        decoded_message = huffman_decoding(encoded_message, huffman_codes)
        if decoded_message == 'exit':
            print("Client disconnected")
            client_socket.close()
            break
        print(f"Decoded message from client: {decoded_message}")

        # Prepare a response
        response_message = f"Message received: {decoded_message}"
        encoded_response, response_huffman_codes, _ = huffman_encoding(response_message)
        response_data = {
            "encoded_response": encoded_response,
            "huffman_codes": response_huffman_codes
        }
        serialized_response = json.dumps(response_data)
        response_length = len(serialized_response)

        # Send the length of the response first
        client_socket.sendall(str(response_length).encode('utf-8').ljust(16))  # 16 bytes for length
        
        # Send the actual response
        client_socket.sendall(serialized_response.encode('utf-8'))
        
        print(f"Response sent to client")

        client_socket.close()

if __name__ == "__main__":
    start_server()
