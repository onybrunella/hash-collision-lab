import hashlib
functions = ["md5", "sha1", "sha256", "sha3_256"]
message = b"abc"

for name in functions:
    h = hashlib.new(name, message)
    hex_digest = h.hexdigest()
    len_byte = len(h.digest())
    len_bits=len_byte * 8
    print(name, hex_digest, len_bits)

def truncate(hash, nb_bits):
    hash_bits = len(hash) * 8
    number = int.from_bytes(hash, "big")
    return number >> (hash_bits - nb_bits)

d = hashlib.md5(b"abc").digest()
print("\nEtape 2")
print(hex(truncate(d, 16)))  
print(hex(truncate(d, 8)))

# def find_collision(name, n):

import random
rng = random.Random(42) 
print("\nEtape 3")
for i in range(5) : 
    msg = rng.randbytes(16)     # 16 bytes random
    print(msg.hex()) 
    
