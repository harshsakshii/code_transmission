def read_text_file(filename):
  try:
    with open(filename, 'r') as file:
      content = file.read()
      return content
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None

# Example usage:
filename = r'C:\\CODE\\Deadly_Python\\side projects\\test.txt'
content = read_text_file(filename)
print(content)