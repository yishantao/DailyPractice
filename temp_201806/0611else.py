# for i in range(3):
#     print('hello')
# else:
#     print('world')

# try:
#     hello()
# except OSError:
#     log('OSError')
# else:
#     ok()

with open('hello.py') as fp:
    src = fp.read(20)

print(fp.closed, fp.encoding)
