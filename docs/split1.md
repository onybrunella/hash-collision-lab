# Split 1 – Birthday attack on truncated hashes (Brunella)

My notes: commands + explanations.

---

## 1. Open the project (every work session)

```bash
cd ~/.../hash-collision-lab
source .venv/bin/activate              # activate the project's Python → (.venv) appears
git checkout feature/birthday-attack   
git pull                              
code .                               
```

---

## 2. Installation (once only - already done)

```bash
python3 -m venv .venv              # create the virtual environment
source .venv/bin/activate
pip install matplotlib pytest      # useful libraries
pip freeze > requirements.txt      # save the list of libraries
echo ".venv/" >> .gitignore        # do not send .venv to GitHub
echo "__pycache__/" >> .gitignore
mkdir -p src tests results figures data
```

---

## 3. Run my code

```bash
python src/birthday.py                          
python src/run_exp1.py --bits 16 20 --trials 5      # quick test of the experiment
python src/run_exp1.py --trials 100                 # full experiment (n = 16 to 32)
python src/run_exp1.py --bits 36 40 --trials 30 --out results/exp1_birthday_large.csv
```

---

## 4. Run the tests

```bash
pytest                 # run all tests in the tests/ folder
pytest -v              # same, showing each test
```

---

## 5. 

- Function: `find_collision(hash_name, n_bits)`
- Hash function names: `md5`, `sha1`, `sha256`, `sha3_256`
- Results file: `results/exp1_birthday.csv`
- Columns: `function, n, trial, attempts, seconds, msg1_hex, msg2_hex`
- Branches: `feature/...` for everyone

---

## 7. Theory to remember

- n bits kept → N = 2^n possible values
- Average number of tries before a collision: √(πN/2) ≈ 1.25 · 2^(n/2)
- Probability of a collision after k tries: P(k) ≈ 1 − e^(−k²/(2N))

---