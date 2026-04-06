# Bytes representing the ASCII values of characters
byte_data = b'Hello, World!'

# Decoding bytes into a string using decode()
text_data = byte_data.decode('utf-8')

print(text_data)



from io import BytesIO

# Simulating in-memory data
data = b"Hello, Binary World!"
print("Binary data representation: ", data)

# Using BytesIO to treat in-memory data as a file
# Files give access to more methods like seek()
with BytesIO(data) as stream:
    content = stream.read()

# Now 'content' contains the data as if it was read from a file
print("Decoded stream content:", content.decode())  
