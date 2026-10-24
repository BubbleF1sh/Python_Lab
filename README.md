# Python Diary

A small command-line diary program written in Python, built in two versions to practice file handling and databases.

## Files

| File | Storage | Description |
|------|---------|-------------|
| `diary.py` | Text file | Saves each entry (date, what I learned, mood) by appending to a `.txt` file |
| `diary_db.py` | SQLite database | Saves the same entries into a `.db` file and prints them all back |

## Requirements

- Python 3 (tested on 3.14)
- No extra packages needed: `sqlite3` is part of the Python standard library

## Usage

### Text file version

```
py diary.py diary.txt
```

### SQLite version

```
py diary_db.py 
```
*The database file is created automatically in the same folder on the first run.*

Both programs ask three questions (date, what you learned, mood), save the answers, and then show your diary.

## What I practiced

- Command-line arguments with `argv`
- Reading and writing files, and the `with` statement
- SQL basics with `sqlite3`: `CREATE TABLE`, `INSERT`, `SELECT`, parameterized queries, `commit`

## Privacy

Diary data files (`*.txt` and `*.db`) are excluded by `.gitignore`, so personal entries are never uploaded.