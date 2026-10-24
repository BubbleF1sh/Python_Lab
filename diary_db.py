import sqlite3

DB_NAME="db_file.db"

conn = sqlite3.connect(DB_NAME)
print(f"Connected to {DB_NAME}")

conn.execute("""
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    learned TEXT,
    mood TEXT
)
""")

date=input("Whats today date? ")
learned=input("What have you learn today? ")
mood=input("Hows going on today? ")

with conn:
    conn.execute("INSERT INTO entries (date, learned, mood) VALUES (?, ?, ?)", (date, learned, mood))

print("Entry saved")

print("Here's your diary:")
rows = conn.execute("SELECT id, date, learned, mood FROM entries")

for id, date, learned, mood in rows:
    print(f"{id:<4}|\t{date}\t|{learned:^15}|\t{mood}")

conn.close()