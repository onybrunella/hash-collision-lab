# Systematic literature review

Protocol: *Protocol for systematic literature review* (SRSI course). Searches run on **2 November 2026**.

## Research questions

- **GQ:** To what extent is the collision resistance of a cryptographic hash function determined by its output size, and to what extent by its internal design?
- **FQ1:** Which attacks broke the collision resistance of MD5 and SHA-1, and what did they cost?
- **FQ2:** What are the best known collision attacks against SHA-256 and SHA-3, and how many rounds do they reach?
- **FQ3:** How large is the gap between the generic birthday bound and the best known attack for each function?
- **SQ:** How many publications on collision attacks against these hash functions appeared per year?

## Search strings

| Database | Query | Results |
| --- | --- | --- |
| IEEE Xplore | `("Abstract":"MD5" OR "Abstract":"SHA-1" OR "Abstract":"SHA-256" OR "Abstract":"SHA-3" OR "Abstract":"Keccak" OR "Abstract":"hash function") AND ("Abstract":"collision")` — filters: conferences and journals, 2004–2026 | 266 |
| Scopus | `ABS("MD5" OR "SHA-1" OR "SHA-256" OR "SHA-3" OR "Keccak" OR "hash function") AND ABS("collision") AND PUBYEAR > 2003 AND PUBYEAR < 2027 AND (DOCTYPE(ar) OR DOCTYPE(cp)) AND LANGUAGE(english)` | 1,873 |

**Secondary search** (protocol, step 5): the same string `AND ("systematic literature" OR "systematic review" OR "literature review")`, applied to the records of both databases: **0 results**.

## Criteria

- **Include (I1):** presents or analyses a collision attack on MD5, SHA-1, SHA-2 or SHA-3 (full or reduced), compares these functions, or shows the practical impact of such collisions.
- **Exclude:** E1 not about the security of cryptographic hash functions · E2 only uses hash functions in an application · E3 another hash function or a new design · E4 another security property (e.g. preimage) · E5 retracted.

## Selection

| Step | Records |
| --- | --- |
| Identified (IEEE Xplore 266 + Scopus 1,873) | 2,139 |
| Duplicates removed | 316 |
| Unique records screened (title and abstract) | 1,823 |
| Excluded (E1–E5) | 1,647 |
| Kept for a closer look (112 included + 64 maybe) | 176 |
| **Primary studies selected (from titles, abstracts and main results)** | **12** |

Files: `screening.xlsx` / `screening.csv` give, for every record, the database, title, year, venue, DOI, decision and criterion. The raw RIS exports are not published here because they contain the abstracts, which are copyrighted by the publishers.

## Primary studies

| # | Study | Year | Function | Why it was selected |
| --- | --- | --- | --- | --- |
| 1 | Wang and Yu, *How to break MD5 and other hash functions* (EUROCRYPT) — doi:10.1007/11426639_2 | 2005 | MD5 | First practical MD5 collision (FQ1) |
| 2 | Black, Cochran and Highland, *A study of the MD5 attacks* (FSE) — doi:10.1007/11799313_17 | 2006 | MD5 | Attack reproduced on ordinary hardware (FQ1) |
| 3 | Stevens, Lenstra and de Weger, *Target collisions for MD5 and colliding X.509 certificates for different identities* (ePrint 2006/360) | 2007 | MD5 | First chosen-prefix collisions (FQ1) |
| 4 | Stevens et al., *Short chosen-prefix collisions for MD5 and the creation of a rogue CA certificate* (ePrint 2009/111) | 2009 | MD5 | Rogue CA, best MD5 cost 2^16 (FQ1, FQ3) |
| 5 | Stevens, *Counter-cryptanalysis* (ePrint 2013/358) | 2013 | MD5 | Analysis of the Flame attack (FQ1) |
| 6 | Stevens et al., *The first collision for full SHA-1* (ePrint 2017/190) | 2017 | SHA-1 | SHAttered, first real SHA-1 collision (FQ1) |
| 7 | Leurent and Peyrin, *SHA-1 is a shambles* (USENIX Security) | 2020 | SHA-1 | Best SHA-1 cost 2^61.2, chosen-prefix (FQ1, FQ3) |
| 8 | Guo et al., *Practical collision attacks against round-reduced SHA-3* (J. Cryptology) — doi:10.1007/s00145-019-09313-3 | 2020 | SHA-3 | Best practical SHA-3 collisions, 5 of 24 rounds (FQ2) |
| 9 | Goldberg et al., *RADIUS/UDP considered harmful* (USENIX Security) | 2024 | MD5 | Real-world MD5 attack in 2024 (FQ1) |
| 10 | Li, Liu and Wang, *New records in collision attacks on SHA-2* (EUROCRYPT) — doi:10.1007/978-3-031-58716-0_6 | 2024 | SHA-2 | 39-step semi-free-start collision (FQ2) |
| 11 | Li et al., *The first practical collision for 31-step SHA-256* (ASIACRYPT) — doi:10.1007/978-981-96-0941-3_8 | 2024 | SHA-256 | Best practical SHA-256 collision (FQ2) |
| 12 | Zhang et al., *Collision attacks on SHA-256 up to 37 steps with improved trail search* (ePrint 2026/232) | 2026 | SHA-256 | Best theoretical SHA-256 collision (FQ2) |


The full reading of the primary studies with the three-pass method is planned for the next phase of the project.
