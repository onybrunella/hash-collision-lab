import hashlib
HASH_FUNCTIONS = ["md5", "sha1", "sha256", "sha3_256"]

"""Returns the hash of a file as hex text."""
def hash_file(path, algorithm):
    with open (path, "rb") as f:
        data = f.read()
    return hashlib.new(algorithm, data).hexdigest()

def compare_pair(name, path_a, path_b):
    """Compare two files with every hash function. Returns one row per function."""
    with open(path_a, "rb") as f:
        file_a = f.read()
    with open(path_b, "rb") as f:
        file_b = f.read()
    if file_a == file_b:
        raise ValueError("The two files are identical: not a real collision.")

    rows = []
    for algorithm in HASH_FUNCTIONS:
        hash_a = hash_file(path_a, algorithm)
        hash_b = hash_file(path_b, algorithm)
        rows.append([name, algorithm, hash_a, hash_b, hash_a == hash_b])
    
    return rows

    
for row in compare_pair("fastcoll", "data/shattered-1.pdf", "data/shattered-2.pdf"):
    print(row)
