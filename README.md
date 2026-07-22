# Book Analyzer

This project generates a report from a `.txt` archive. It shows the total word count, total character count, and letter frequency.

## Features
- Reads `.txt` files.
- Counts total words.
- Counts total characters.
- Shows letter frequency and orders the results.

## Technologies
- Python
- Git
- Linux

## Installation
You can clone this repository from a Linux environment and run it using Python via the Command Line Interface (CLI):

```bash
git clone https://github.com/ntorresland-dev/book-analyzer.git
cd book-analyzer
```
## Usage
Run the main script and pass the text file you want to analyze as an argument:
```bash
python3 src/main.py books/frankenstein.txt
```

## Project Structure
```text
.
├── README.md
├── requirements.txt
├── books/
├── src
│   ├── file_management.py
│   ├── main.py
│   ├── stats.py
│   └── text_manipulation.py
└── tests
```

## What I Learned
- Working with modules.
- Separation of concerns.
- Using Git in a natural workflow.
- Working with branches.
- Making small, atomic commits.
- Putting Python programming fundamentals into practice.
- Organizing a project structure.
- Applying the "divide and conquer" concept to solve problems.
- Basic Linux command-line navigation to create, move, and edit files and directories.
