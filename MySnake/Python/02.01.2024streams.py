import io

data = io.StringIO('Hello world')
print(data.read(5))
print(data.tell())
print(data.__dir__())