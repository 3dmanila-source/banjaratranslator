import sqlite3
import sys

# Connect to database
db_path = r"i:\Banjara AI\dictionary_master.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("="*60)
print("BANJARA DICTIONARY DATABASE")
print("="*60)

# Statistics
cursor.execute('''
    SELECT word_type, COUNT(*) as count 
    FROM dictionary 
    GROUP BY word_type 
    ORDER BY count DESC
''')

print("\n📊 Statistics:")
total = 0
for word_type, count in cursor.fetchall():
    print(f"  {word_type:15} : {count:4}")
    total += count
print(f"  {'TOTAL':15} : {total:4}")

# Sample entries by type
print("\n📚 Sample Entries:")
cursor.execute('''
    SELECT english, word_type, transliteration 
    FROM dictionary 
    WHERE word_type = 'verb' 
    LIMIT 5
''')
print("\n  Verbs:")
for eng, wt, trans in cursor.fetchall():
    print(f"    {eng:15} -> {trans}")

cursor.execute('''
    SELECT english, word_type, transliteration 
    FROM dictionary 
    WHERE word_type = 'noun' 
    LIMIT 5
''')
print("\n  Nouns:")
for eng, wt, trans in cursor.fetchall():
    print(f"    {eng:15} -> {trans}")

# Search functionality
if len(sys.argv) > 1:
    search_term = sys.argv[1].lower()
    print(f"\n🔍 Searching for: '{search_term}'")
    
    cursor.execute('''
        SELECT english, word_type, transliteration 
        FROM dictionary 
        WHERE english LIKE ? 
        ORDER BY english
    ''', (f'%{search_term}%',))
    
    results = cursor.fetchall()
    if results:
        print(f"\n  Found {len(results)} matches:")
        for eng, wt, trans in results[:20]:  # Limit to 20 results
            print(f"    {eng:20} ({wt:10}) -> {trans}")
    else:
        print("  No matches found")

conn.close()

print("\n" + "="*60)
print("TIP: Run 'py query_db.py <word>' to search for a word")
print("="*60)
