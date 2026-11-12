# hash-collision-lab

**Collision Resistance in Cryptographic Hash Functions: Theory vs. Practice**

Group project for *Network and Information Systems Security* (SRSI), Master in Computer Engineering, Iscte – University Institute of Lisbon, 2026/2027.
Teacher: José André Moura.

## Goal

We study whether the collision resistance of a cryptographic hash function depends on its **output size** or on its **internal design**, by comparing MD5, SHA-1, SHA-256 and SHA3-256.

- **Part 1 (report):** a systematic literature review of collision attacks, a comparison of related works, and the security gap between the generic birthday bound and the best known attack.
- **Part 2 (practice):** three Python experiments: brute-force collisions on truncated outputs, verification of real collisions (SHAttered, MD5), and performance measurements.

## Repository structure

| Folder | Content |
| --- | --- |
| `report/` | Report of Part 1 (PDF) |
| `docs/literature-review/` | Search queries, screening of the 2,139 records (decision and criterion for each), list of the 12 primary studies |

## Main results (Part 1)

| Function | Generic bound | Best known collision attack (full function) | Security gap |
| --- | --- | --- | --- |
| MD5 | 2^64 | ≈ 2^16 | ≈ 48 bits |
| SHA-1 | 2^80 | ≈ 2^61.2 | ≈ 19 bits |
| SHA-256 | 2^128 | none known | 0 |
| SHA3-256 | 2^128 | none known | 0 |

## Resources

- Report (PDF): [`report/Collision_Resistance_Hash_Functions_Report.pdf`](report/Collision_Resistance_Hash_Functions_Report.pdf)
- Literature review (search strings, screening, 12 primary studies): [`docs/literature-review/`](docs/literature-review/)
- NIST FIPS 180-4, *Secure Hash Standard* (SHA-1, SHA-256): https://doi.org/10.6028/NIST.FIPS.180-4
- NIST FIPS 202, *SHA-3 Standard*: https://doi.org/10.6028/NIST.FIPS.202
- RFC 1321, *The MD5 Message-Digest Algorithm*: https://www.rfc-editor.org/rfc/rfc1321
- SHAttered, first SHA-1 collision (Stevens et al., 2017): https://shattered.io
- SHA-1 is a Shambles, chosen-prefix collision (Leurent and Peyrin, 2020): https://sha-mbles.github.io
- Python `hashlib` documentation (used in Part 2): https://docs.python.org/3/library/hashlib.html

## Authors

- Anthonin Bleuse (145881)
- Sandra Amurao (146859)
- Brunella Andriatsahavojaona (145880)
- Youssef Malki (146347)
