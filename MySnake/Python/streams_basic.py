import io
data = io.StringIO("Hello World!")
print(data.read(5))
print(data.read(5))
# print(data.read(5))
print(data.tell())
print(data.seekable())
print(data.readable())
