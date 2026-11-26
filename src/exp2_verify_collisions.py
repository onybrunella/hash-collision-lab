import hashlib
HASH_FUNCTIONS = ["md5", "sha1", "sha256", "sha3_256"]

"""Returns the hash of a file as hex text."""
def hash_file(path, algorithm):
    with open (path, "rb") as f:
        data = f.read()
    return hashlib.new(algorithm, data).hexdigest()
