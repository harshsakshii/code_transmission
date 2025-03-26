import streamlit as st
from huffman_encoding_decoding import huffman_encoding, huffman_decoding
import socket
import json

# Server connection settings
HOST = '127.0.0.1'
PORT = 12345

# Streamlit UI
st.title("Client for Huffman Encoding TCP/IP Communication")

# User input options
option = st.selectbox("Choose input method:", ("Text", "File"))

if option == "Text":
    message = st.text_area("Enter the message to send:")
elif option == "File":
    uploaded_file = st.file_uploader("Choose a text file to send")
    if uploaded_file is not None:
        message = uploaded_file.read().decode("utf-8")

# Button to send data
if st.button("Send to Server"):
    if message:
        encoded_message, huffman_codes, _ = huffman_encoding(message)
        
        try:
            # Connect to server
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((HOST, PORT))
            
            # Prepare the data to send
            data = {
                "encoded_message": encoded_message,
                "huffman_codes": huffman_codes
            }
            serialized_data = json.dumps(data)  # Convert to JSON string
            data_length = len(serialized_data)  # Length of serialized data

            # Send the length first
            client_socket.sendall(str(data_length).encode('utf-8').ljust(16))  # 16 bytes for length
            
            # Send the actual data
            client_socket.sendall(serialized_data.encode('utf-8'))
            
            # Receive response from server
            response_length = int(client_socket.recv(16).strip())  # Receive the response length
            encoded_response = client_socket.recv(response_length).decode('utf-8')

            # Parse the received data
            response_data = json.loads(encoded_response)
            decoded_response = huffman_decoding(response_data["encoded_response"], response_data["huffman_codes"])
            
            # Display results
            st.success("Message sent successfully!")
            st.write("Original Message:", message)
            st.write("Encoded Message:", encoded_message)
            st.write("Decoded Response from Server:", decoded_response)
            
            # Log details
            with open("client_log.txt", "a") as log_file:
                log_file.write(f"\nMessage Sent: {message}\n")
                log_file.write(f"Encoded Message: {encoded_message}\n")
                log_file.write(f"Decoded Response: {decoded_response}\n")
                
        except Exception as e:
            st.error(f"Error communicating with server: {e}")
        finally:
            client_socket.close()
    else:
        st.warning("Please enter a message or upload a file.")
