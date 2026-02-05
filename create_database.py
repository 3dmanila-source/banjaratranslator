import re
import json
import csv
import sqlite3
from pathlib import Path

def parse_entry(line):
    """Parse a dictionary entry line into structured data"""
    entries = []
    line = line.strip()
    
    if not line or len(line) < 5:
        return entries
    
    # Skip headers and page markers
    if any(skip in line for skip in ['English Section', 'Page', 'Section', 'abide appreciate', ' A ']):
        return entries
    
    # Word type mappings (using abbreviated format from source)
    word_type_map = {
        'v.': 'verb',
        'n.': 'noun',
        'adj.': 'adjective',
        'adv.': 'adverb',
        'pron.': 'pronoun',
        'conj.': 'conjunction',
        'num.': 'numeral',
        'prop.': 'proper noun'
    }
    
    # Pattern: english  word_type  script  /transliteration/
    # Can have multiple entries separated by semicolons or word types
    
    # Split by transliterations to handle multiple entries
    trans_pattern = r'/([^/]+)/'
    transliterations = re.findall(trans_pattern, line)
    
    if not transliterations:
        return entries
    
    # Find all word type matches
    word_type_positions = []
    for wt_key, wt_value in word_type_map.items():
        for match in re.finditer(re.escape(wt_key), line):
            word_type_positions.append((match.start(), wt_key, wt_value))
    
    word_type_positions.sort()
    
    # If no word types found, treat as simple format
    if not word_type_positions:
        # Simple format: "english script /transliteration/"
        parts = line.split('/')
        if len(parts) >= 2:
            english_part = parts[0].strip().split()[0]
            script_part = ' '.join(parts[0].strip().split()[1:])
            
            entries.append({
                'english': english_part.lower(),
                'word_type': 'unknown',
                'script': script_part.strip(),
                'transliteration': transliterations[0].strip()
            })
    else:
        # Has word types - extract each entry
        for i, trans in enumerate(transliterations):
            # Find the word type for this transliteration
            trans_pos = line.find(f'/{trans}/')
            
            # Find the closest word type before this transliteration
            word_type = 'unknown'
            english = ''
            
            for pos, wt_key, wt_value in reversed(word_type_positions):
                if pos < trans_pos:
                    word_type = wt_value
                    # Extract English word (before word type)
                    before_wt = line[:pos].strip()
                    # Get the last word before word type
                    words = before_wt.split()
                    if words:
                        # Handle multi-word entries
                        english = words[-1] if i > 0 or ';' in before_wt else words[0]
                    break
            
            # Extract script (between word type and transliteration)
            script_start = trans_pos
            for pos, wt_key, wt_value in word_type_positions:
                if pos < trans_pos:
                    script_start = pos + len(wt_key)
            
            script = line[script_start:trans_pos].strip()
            # Remove word type markers from script
            for wt_key in word_type_map.keys():
                script = script.replace(wt_key, '').strip()
            
            if english and trans:
                entries.append({
                    'english': english.lower().strip(),
                    'word_type': word_type,
                    'script': script,
                    'transliteration': trans.strip()
                })
    
    return entries

def create_database(text_file, db_file, csv_file):
    """Create SQLite database and CSV from text file"""
    
    print(f"Reading {text_file}...")
    with open(text_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Parse all entries
    all_entries = []
    for line_num, line in enumerate(lines, 1):
        entries = parse_entry(line)
        for entry in entries:
            entry['line_number'] = line_num
            all_entries.append(entry)
    
    print(f"Parsed {len(all_entries)} entries")
    
    # Create SQLite database
    print(f"Creating database {db_file}...")
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dictionary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            english TEXT NOT NULL,
            word_type TEXT,
            script TEXT,
            transliteration TEXT NOT NULL,
            line_number INTEGER,
            UNIQUE(english, word_type, transliteration)
        )
    ''')
    
    # Create indexes for faster lookups
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_english ON dictionary(english)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_word_type ON dictionary(word_type)')
    
    # Insert entries
    inserted = 0
    for entry in all_entries:
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO dictionary 
                (english, word_type, script, transliteration, line_number)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                entry['english'],
                entry['word_type'],
                entry['script'],
                entry['transliteration'],
                entry['line_number']
            ))
            if cursor.rowcount > 0:
                inserted += 1
        except Exception as e:
            print(f"Error inserting {entry}: {e}")
    
    conn.commit()
    print(f"Inserted {inserted} unique entries into database")
    
    # Create CSV export
    print(f"Creating CSV {csv_file}...")
    cursor.execute('SELECT english, word_type, script, transliteration FROM dictionary ORDER BY english')
    rows = cursor.fetchall()
    
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['English', 'Word Type', 'Telugu Script', 'Transliteration'])
        writer.writerows(rows)
    
    print(f"Exported {len(rows)} entries to CSV")
    
    # Statistics
    cursor.execute('SELECT word_type, COUNT(*) FROM dictionary GROUP BY word_type ORDER BY COUNT(*) DESC')
    stats = cursor.fetchall()
    
    print("\n=== Statistics ===")
    print(f"Total unique entries: {len(rows)}")
    print("\nBy word type:")
    for word_type, count in stats:
        print(f"  {word_type}: {count}")
    
    conn.close()
    return len(rows)

def main():
    text_file = r"i:\Banjara AI\extracted_text.txt"
    db_file = r"i:\Banjara AI\dictionary_master.db"
    csv_file = r"i:\Banjara AI\dictionary_master.csv"
    
    total = create_database(text_file, db_file, csv_file)
    
    print(f"\n=== SUCCESS ===")
    print(f"Created master database with {total} entries")
    print(f"Database file: {db_file}")
    print(f"CSV file: {csv_file}")
    print("\nYou can now query the database using SQL!")

if __name__ == "__main__":
    main()
