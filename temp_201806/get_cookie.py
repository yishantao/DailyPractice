import browsercookie

chrome_cookiejar = browsercookie.chrome()
print(type(chrome_cookiejar))
for cookie in chrome_cookiejar:
    print(cookie)
