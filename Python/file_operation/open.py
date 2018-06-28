# with open('text.txt') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print('read line is:', line)


# import fileinput
#
# for line in fileinput.input('text.txt'):
#     print(line)

# for line in open('text.txt'):
#     print(line)

import pickle

# d = {'name': 'zhangsan'}
# file = open('text.txt', 'wb')
# pickle.dump(d, file)

# file = open('text.txt', 'rb')
# print('load resust:', pickle.load(file))

import json

# data = {'num': 100, 'name': 'zhangsan'}
# refactor = json.dumps(data)
# print(refactor)
# data2 = json.loads(refactor)
# print(data2)

# data = {'num': 100, 'name': {'one': 'first', 'two': 'second'}}
# with open('text.txt', 'w') as f:
#     json.dump(data, f)

# with open('text.txt', 'r') as f:
#     data = json.load(f)
#     print(data)

string = '1\t45\n67'
print(string)
print(repr(string))
