import hashlib
import csv
import os

HASH_FUNCTIONS = ["md5", "sha1", "sha256", "sha3_256"]

def hash_file(path, algorithm):
    """Returns the hash of a file as hex text."""
    with open (path, "rb") as f:
        data = f.read()
    
    # run the hash function on the file's bytes, then convert the result to hex text
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

def add_suffix(path, suffix, new_path):
    """Copy a file and add the same bytes at the end."""
    with open(path, "rb") as f:
        data = f.read()                 
    with open(new_path, "wb") as f:     
        f.write(data + suffix)         
   
def save_csv(rows, path):
    """Write the results table to a CSV file."""
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["pair", "algorithm", "hash_a", "hash_b", "same"])
        writer.writerows(rows)

def main():
    os.makedirs("results", exist_ok=True)

    suffix = b"SRSI group project"

    # MD5 collision pair (made by us with fastcoll)
    add_suffix("data/md5_a.bin", suffix, "data/md5_a_suffix.bin")
    add_suffix("data/md5_b.bin", suffix, "data/md5_b_suffix.bin")

    # SHA-1 collision pair (SHAttered PDFs, Stevens et al. 2017)
    add_suffix("data/shattered-1.pdf", suffix, "data/shattered-1_suffix.pdf")
    add_suffix("data/shattered-2.pdf", suffix, "data/shattered-2_suffix.pdf")   

    # Compare each pair with all 4 hash functions (4 pairs x 4 functions = 16 rows)
    rows = []
    rows += compare_pair("shattered", "data/shattered-1.pdf", "data/shattered-2.pdf")
    rows += compare_pair("fastcoll", "data/md5_a.bin", "data/md5_b.bin")
    rows += compare_pair("shattered + suffix", "data/shattered-1_suffix.pdf", "data/shattered-2_suffix.pdf")
    rows += compare_pair("fastcoll + suffix", "data/md5_a_suffix.bin", "data/md5_b_suffix.bin")

    # Show the results: pair name, hash function, same hash (True/False)
    for row in rows:
        print(row[0], row[1], row[4])

    # Save the full results table (with the hashes)
    save_csv(rows, "results/exp2_collisions.csv")
    print("CSV saved in results/exp2_collisions.csv")

if __name__ == "__main__":
    main()