# code_transmission
This project implements a lossless data compression system using Huffman coding to efficiently transmit data over a network. The system compresses input data (text, images, etc.), transmits the compressed bitstream, and decompresses it back to its original format at the destination. By reducing redundancy and utilizing shorter codes for frequent symbols, Huffman coding ensures minimal data size without loss of information.

Features
- Lossless Compression – Ensures complete reconstruction of original data.
-Efficient Data Transmission – Reduces data size to optimize network transfer.
- Huffman Coding Algorithm – Implements greedy-based symbol frequency encoding.
  - Modular Design – Separate components for encoding, server-side handling, and client-side decompression.
- Adaptive Compression – Adjusts to different data types for optimized performance.
  -Error Handling – Implements error detection for reliable data transmission.

How Huffman Coding Works
Frequency Analysis – Determines symbol occurrence in input data.

Huffman Tree Construction – Uses a priority queue (min-heap) to construct an optimal binary tree.

Code Assignment – Generates variable-length binary codes for symbols (shorter for frequent ones).

Encoding – Replaces original data symbols with compressed Huffman codes.

Decoding – Uses the Huffman tree to reconstruct the original data from the compressed bitstream.

Project Structure
bash
Copy
Edit
/data-transmission-optimizer
│── src/
│   │── huffman.py         # Huffman encoding and decoding implementation
│   │── server.py          # Server-side compression and transmission
│   │── client.py          # Client-side reception and decompression
│── assets/                # Sample input files (text, images)
│── README.md              # Project documentation
│── requirements.txt       # Dependencies
Installation & Setup
Prerequisites
Ensure you have Python 3.x installed along with necessary dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Running the Project
Start the Server

bash
Copy
Edit
python server.py
Run the Client

bash
Copy
Edit
python client.py
How the System Works
1. Huffman Encoding & Decoding
Handles data compression and decompression:
-Reads input files (text, images, etc.).
- Constructs Huffman tree & assigns codes.
- Encodes input data to a compressed bitstream.
- Decodes received bitstream to restore original data.

2. Server-Side Processing
-Accepts client connections.
--Compresses incoming data using Huffman encoding.
- Transmits compressed data over the network.
- Implements error handling to ensure data integrity.

4. Client-Side Processing
- Requests data from the server.
-Receives compressed bitstream.
-Decodes the bitstream to retrieve original data.


Performance Metrics
To evaluate system efficiency, we measure:
- Compression Ratio – Reduction in data size after encoding.
- Transmission Time – Speed of compressed data transfer over the network.
  - Decompression Time – Time required to restore original data.
