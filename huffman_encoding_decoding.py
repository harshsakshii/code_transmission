import heapq
from collections import Counter

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    # Override comparison operators to compare nodes based on their frequency
    def __lt__(self, other):
        return self.freq < other.freq

def generate_codes(root, current_code, huffman_codes):
    if root is None:
        return
    
    if root.char is not None:
        huffman_codes[root.char] = current_code
        return
    
    generate_codes(root.left, current_code + '0', huffman_codes)
    generate_codes(root.right, current_code + '1', huffman_codes)

def huffman_encoding(text):
    freq = Counter(text)
    
    heap = []
    for char, frequency in freq.items():
        heapq.heappush(heap, Node(char, frequency))
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq, node1, node2)
        heapq.heappush(heap, merged)
    
    root = heapq.heappop(heap)
    
    huffman_codes = {}
    generate_codes(root, "", huffman_codes)
    
    encoded_text = ''.join([huffman_codes[char] for char in text])
    
    return encoded_text, huffman_codes, root

def huffman_decoding(encoded_text, huffman_codes):
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""
    
    return decoded_text

def print_huffman_tree(node, indent=""):
    if node is None:
        return
    
    if node.char is not None:
        print(f"{indent}Leaf: '{node.char}' (freq: {node.freq})")
    else:
        print(f"{indent}Internal Node (freq: {node.freq})")

    print(f"{indent}├─ Left:")
    print_huffman_tree(node.left, indent + "│  ")
    print(f"{indent}└─ Right:")
    print_huffman_tree(node.right, indent + "   ")

if __name__ == "__main__":
    text = input("Enter text to encode: ")

    print(f"Original text: {text}\n")
    
    # Encoding
    encoded_text, huffman_codes, root = huffman_encoding(text)
    print(f"Encoded text: {encoded_text}\n")
    print(f"Huffman Codes: {huffman_codes}\n")
    
    # Decoding
    decoded_text = huffman_decoding(encoded_text, huffman_codes)
    print(f"Decoded text: {decoded_text}\n")

    # Print the Huffman Tree
    # print("Huffman Tree:")
    # print_huffman_tree(root)



