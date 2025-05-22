# Rosalind Solutions Repository

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg) ![Snakemake](https://img.shields.io/badge/Snakemake-pipelines-green.svg)

> **Brief:** This repository contains my step-by-step solutions to the problems on [Rosalind](http://rosalind.info), complete with explanations, example inputs, and notes on challenges and learnings.

---

## 📚 Table of Contents

1. [Introduction](#-introduction)
2. [Repository Structure](#-repository-structure)
3. [Clone this repository](#-clone-this-repository)
4. [Task List](#-task-list)
5. [Template for Each Problem](#-template-for-each-problem)
6. [Tech Stack](#-tech-stack)
7. [Contributing](#-contributing)

---

## 📖 Introduction

Welcome to my **Rosalind Solutions** repository! Here I document every problem I solve on Rosalind with:

* ✔️ Raw code and Clean, commented code (Python / Bash)
* 📝 Detailed notes on my thought process, challenges, and optimizations
* 🎯 Example inputs and expected outputs

This repository serves as both a learning journal and a public portfolio of bioinformatics problem-solving.

---

## 📁 Repository Structure

```
rosalind-solutions/
├── README.md             # This file
├── 01-dna/               # Problem 1: Counting DNA Nucleotides
│   ├── solution.py
│   ├── input.txt
│   └── notes.md
├── 02-revc/              # Problem 2: Reverse Complement
│   ├── solution.py
│   ├── input.txt
│   └── notes.md
├── utils/                # Helper functions shared across tasks
│   └── helpers.py
└── .github/              # CI workflows, issue templates (optional)
    └── workflows/
```

---

## ⚙️ Clone this repository

   ```bash
   git clone https://github.com/Gierak245/Rosalynd_solutions.git
   cd rosalind-solutions
   ```


---

## 🗒️ Task List

| Nr  | Problem Code | Title                                    | Folder       | Status           |
|-----|--------------|------------------------------------------|--------------|------------------|
| 01  | DNA          | Counting DNA Nucleotides                 | `01-dna`     | ✅ Done          |
| 02  | RNA          | Transcribing DNA into RNA                | `02-rna`     | ✅ Done          |
| 03  | REVC         | Complementing a Strand of DNA            | `03-revc`    | ✅ Done          |
| 04  | FIB          | Rabbits and Recurrence Relations         | `04-fib`     | ✅ Done          |
| 05  | GC           | Computing GC Content                     | `05-gc`      | ✅ Done          |
| 06  | HAMM         | Counting Point Mutations                 | `06-hamm`    | ✅ Done          |
| 07  | IPRB         | Mendel’s First Law                       | `07-iprb`    | ✅ Done          |
| 08  | PROT         | Translating RNA into Protein             | `08-prot`    | ✅ Done          |
| 09  | SUBS         | Finding a Motif in DNA                   | `09-subs`    | ✅ Done          |
| 10  | CONS         | Consensus and Profile                    | `10-cons`    | ✅ Done          |
| 11  | FIBD         | Mortal Fibonacci Rabbits                 | `11-fibd`    | ✅ Done          |
| 12  | GRPH         | Overlap Graphs                           | `12-grph`    | ✅ Done          |
| 13  | IEV          | Calculating Expected Offspring           | `13-iev`     | ✅ Done          |
| 14  | LCSM         | Finding a Shared Motif                   | `14-lcsm`    | ✅ Done          |
| 15  | MPRT         | Finding a Protein Motif                  | `15-mprt`    | ✅ Done          |
| 16  | LIA          | Independent Alleles                      | `16-lia`     |    In Progress   |
| 17  | MRNA         | Inferring mRNA from Protein              | `17-mrna`    | To Do            |
| 18  | ORF          | Open Reading Frames                      | `18-orf`     | To Do            |
| 19  | PERM         | Enumerating Gene Orders                  | `19-perm`    | To Do            |
| 20  | PRTM         | Calculating Protein Mass                 | `20-prtm`    | To Do            |



---

## 📄 Template for Each Problem

Each problem folder follows this template:

```
<problem-number>-<short-name>/
├── final_solution.py            # Your code with comments
├── raw_solution.py            # Your code with comments
├── input.txt              # Example input file
└── notes.md               # Problem description, thought process, challenges, learnings
```

### Example `notes.md`:

```markdown
# Problem: DNA (Counting DNA Nucleotides)

## Description
Count the number of nucleotides (A, C, G, T) in a given DNA string.

## Thought Process
- First implemented a loop with counters.
- Refactored using `collections.Counter` for brevity.

## Challenges
- Forgetting to strip newline characters led to off-by-one errors.

## Learnings
- Importance of data cleaning (.strip()).
- Efficiency gains using built-in libraries.
```

---

## 🛠️ Tech Stack

* **Language:** Python 3.12+, Bash
* **Version Control:** Git, GitHub
* **CI (optional):** GitHub Actions for linting/tests

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

* Open an issue with suggestions or questions
* Submit a pull request for optimizations or new problem solutions

Please ensure code readability and include `notes.md` for each new problem.
