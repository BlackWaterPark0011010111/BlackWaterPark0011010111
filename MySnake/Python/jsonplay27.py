import json
import time

with open('./myjson.json') as file:
    # print(file.read()) #serialized 
    obj=file.read() #serialized 
    print(obj)

with open('./myjson.json') as file:
    dict= json.loads(file.read()) #deserialized
    # print(type(dict))



# data= json.loads(myjson)
# print(data)


# #DESERIALISATION
# json_string = '{"key":"value", "heee":"valueee", "123":[123,124,454445454], "val":"null"}'
# #print(content[8:13])

# dict = json.loads(json_string)#use  loads to convers string to dictionary
# print(dict["123"][2])

# #SERIALISATION
# mydict = {
#     'name':'Ana',
#     'anothername':'Robert',
#     'mylist':[12,3,4,5,6]
# }



# dikt = {123:6526514541541}
# print(dikt[123])
# jsonContent = json.dumps(mydict, indent = 4)
# #indent изменяет формат печати разных типов данных,
# #indent = intentification, то есть индентификация только
# #разных типов данных


# print(type(mydict))
# print('The contants of mydict is: ', mydict)
# print(type(jsonContent))
# print("The contants of the jsonContent is: ",jsonContent)


# print(dir(json))



# python_dictionary = json.loads(json_string)
# print(python_dictionary)
# print(python_dictionary["val"])





# with open("myjson.json") as f:
#     temple = json.load(f)
# print(temple)

# for section, commands in temple.items():
#     print(section)
#     print('\n'.join(commands))