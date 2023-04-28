x = 8**2020 + 4**2017 + 26 - 1
s = ''
while x != 0: 
    s += str(x % 2)
    x //= 2
s = s[::-1]
print(s.count("1"))
#answer:5