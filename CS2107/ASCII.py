w = ('0' * 36).encode()

z = '0721cdab'

print((w + bytes.fromhex(z)).decode())

x = '20'
print(bytes.fromhex(x).decode())


