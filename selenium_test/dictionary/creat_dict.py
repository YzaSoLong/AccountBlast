#编写一个由数字组成的数字字典

chars = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
]
f = open("dict.txt", 'w')
base = len(chars)
end = len(chars) ** 6
for i in range(0, end):
    n = i
    ch0 = chars[n % base]
    n //= base
    ch1 = chars[n % base]
    n //= base
    ch2 = chars[n % base]
    n //= base
    ch3 = chars[n % base]
    n //= base
    ch4 = chars[n % base]
    n //= base
    ch5 = chars[n % base]
    n //= base
    f.write(ch5 + ch4 + ch3 + ch2 + ch1 + ch0 + '\n')
f.close()
