# a = [1, 2]
# print(repr(a))
# print(str(a))
#

# symbols = 'hello'
# print(tuple(symbol for symbol in symbols))
#
# import array
# print(array.array('I', (ord(symbol) for symbol in symbols)))

# a = [('hello', 1), ('world', 2), ('ok', 3)]
# for word, _ in a:
#     print(word)

# a, b = (1, 2)
# print(a, b)
#
# a = (1, 2)
# print(divmod(*a))
#
# *a, b = (1, 2, 3, 4)
# print(b)
#
# a, *b = (1, 2, 3, 4)
# print(a)
#
# a, *b, c = (1, 2, 3, 4)
# print(a, b, c)

# from collections import namedtuple
#
# City = namedtuple('City', 'name country')
# tokyo = City('tokyo', (1, 2))
# print(tokyo)
# print(tokyo[1])
# print(tokyo.country)

# s = 'apple'
# print(s[::2])
# print(s[::-1])

# l = list(range(5))
# print(l)
# l[1:3] = [1]
# print(l)

# l = [1, 2, 3]
# print(l * 5)
# print('abc' * 5)

# board = [['_'] * 3 for i in range(3)]
# board[0][1] = [1]
# print(board)

# ok = [['_'] * 3] * 3
# print(ok)
# ok[0][1] = 1
# print(ok)

# a = [1, 3]
# print(id(a))
# a *= 2
# print(id(a))

# a = (1, 3)
# print(id(a))
# a *= 2
# print(id(a))

# from array import array
#
# a = array('d', (i for i in range(5)))
# print(a)

# from collections import deque
#
# data = deque(range(5), maxlen=5)
# print(data)
# data.rotate(3)
# print(data)
# data.appendleft(-2)
# print(data)

# a = [('china', 1), ('japan', 2), ('american', 3)]
# b = {country: code for country, code in a}
# print(b)

# a = {'hello': 1, 'world': 2}
# b = a.setdefault('love', 3)
# print(b)
# print(a)

# a = {1, 2, 3}
# b = {1, 4, 3}
# print(a | b)
# a = {i for i in range(5)}
# print(a)

# a = ['apple', 'banana','peel']
# print(sorted(a, key=len))

# a = ['apple', 'banana', 'peel']
# print(sorted(a, key=lambda word: word[::-1]))

# def f(a: int = 2, b: int = 2) -> int:
#     return a + b
#
#
# print(f())
# print(f(1, 2))

a = 1
# print(format(a, '0.4f'))
print('apple{symbol:0.2f}'.format(symbol=a))
print('apple{symbol}'.format(symbol=a))
