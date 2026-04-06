import zipfile
from io import BytesIO

# Create a new ZIP file in-memory
stream = BytesIO()
with zipfile.ZipFile(stream, "w") as zip_file:
    zip_file.writestr("file.txt", "Hello, this is a zipped content!")

# Reset the BytesIO object's position to the beginning
stream.seek(0)

try:
    with zipfile.ZipFile(stream, "r") as zip_file:
        # Read and display contents. Use zip_file.namelist() to see a list of files
        contents = zip_file.read("file.txt").decode("utf-8")
        print(contents)

except Exception as e:
    print("An error occurred:", e)
