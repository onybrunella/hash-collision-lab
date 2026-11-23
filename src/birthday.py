import hashlib
import random

functions = ["md5", "sha1", "sha256", "sha3_256"]
message = b"abc"

for name in functions:
    h = hashlib.new(name, message)
    hex_digest = h.hexdigest()
    len_byte = len(h.digest())
    len_bits=len_byte*8
    print(name, hex_digest, len_bits)

def truncate(hash, nb_bits):
    hash_bits= len(hash)*8
    number = int.from_bytes(hash, "big")
    return number >> (hash_bits - nb_bits)

d = hashlib.md5(b"abc").digest()
print("\step 2")
print(hex(truncate(d, 16)))  
print(hex(truncate(d, 8)))

rng = random.Random(42) 
print("\nstep 3")
for i in range(5): 
    msg = rng.randbytes(16)     # 16 bytes random
    print(msg.hex(), hex(truncate(hashlib.new("md5", msg).digest(),16))) 
    
print("\nstep 4")
def find_collision(hash_name, nb_bits, seed):
    rng = random.Random(seed) 
    seen = {}
    attempts=0

    while True:
        msg = rng.randbytes(16)  
        attempts+=1
        value=truncate(hashlib.new(hash_name, msg).digest(),nb_bits)

        if(value in seen and seen[value] != msg):
            return attempts, seen[value], msg

        seen[value]=msg

attempts, m1, m2 = find_collision("md5", 16, 42)
print(attempts, m1.hex(), m2.hex())
print(hex(truncate(hashlib.new("md5", m1).digest(), 16)))
print(hex(truncate(hashlib.new("md5", m2).digest(), 16)))
