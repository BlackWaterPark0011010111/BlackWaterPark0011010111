import sys

# print(sys.path)
# print(sys.platform)
# print(sys.version)
# print(sys.version_info)

print(sys.argv[0])
list = sys.argv[1:]
sum = 0

for x in list:
    sum = sum + int(x)

print(sum)
