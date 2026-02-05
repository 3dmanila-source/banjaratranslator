"""
Improved Dictionary Extraction - Captures ALL entries
Handles multiple edge cases and formats
"""

import PyPDF2
import json
import re
import unicodedata

def simplify_phonetic(text):
    """Convert phonetic transliteration to simple English letters"""
    # Remove diacritical marks
    result = ''.join(c for c in unicodedata.normalize('NFD', text) 
                     if unicodedata.category(c) != 'Mn')
    
    # Remove special characters, keep only letters
    result = re.sub(r'[^a-zA-Z\s]', '', result)
    
    return result.lower().strip()

def extract_all_entries(text):
    """
    Extract ALL English-Banjara pairs from dictionary text
    Handles multiple formats and edge cases
    """
    dictionary = {}
    lines = text.split('\n')
    
    word_types = ['v.', 'n.', 'adj.', 'adv.', 'pron.', 'conj.', 'num.', 'prop.']
    
    for line in lines:
        line = line.strip()
        if len(line) < 3:
            continue
        
        # Skip headers and page numbers
        if any(skip in line for skip in ['English Section', 'Page', 'Section', 'ఆంగ']):
            continue
        
        # Pattern: "english  word_type. script /transliteration/"
        # Look for /transliteration/ pattern
        if '/' in line:
            # Split by first space to get English word
            parts = line.split(maxsplit=1)
            
            if len(parts) >= 1:
                english = parts[0].strip().lower()
                
                # Validate English word
                if len(english) > 30 or not english.replace('-', '').replace("'", '').isalpha():
                    continue
                
                # Extract ALL transliterations (there might be multiple)
                transliterations = []
                trans_matches = re.findall(r'/([^/]+)/', line)
                
                for trans in trans_matches:
                    simplified = simplify_phonetic(trans)
                    if simplified:
                        transliterations.append(simplified)
                
                # Use first transliteration, or join if multiple
                if transliterations:
                    # If there are multiple, use the longer/more complete one
                    best_trans = max(transliterations, key=len)
                    
                    # Only add if we don't already have this word, or if new trans is better
                    if english not in dictionary or len(best_trans) > len(dictionary[english]):
                        dictionary[english] = best_trans
    
    return dictionary

def main():
    # Load extracted text
    text_path = r"i:\Banjara AI\extracted_text.txt"
    
    print("Loading extracted text...")
    with open(text_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("Parsing ALL dictionary entries...")
    dictionary = extract_all_entries(text)
    
    print(f"\nExtracted {len(dictionary)} unique entries")
    
    # Save complete dictionary
    output_path = r"i:\Banjara AI\dictionary_complete.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=True, indent=2, sort_keys=True)
    
    print(f"Saved to: {output_path}")
    
    # Show statistics
    print("\n=== Statistics ===")
    print(f"Total entries: {len(dictionary)}")
    print(f"Previously extracted: 1968")
    print(f"New entries captured: {len(dictionary) - 1968}")
    
    # Show sample of new entries
    print("\n=== Sample entries ===")
    for i, (eng, ban) in enumerate(list(dictionary.items())[:10]):
        print(f"  {eng} -> {ban}")
    
    print("\nDone!")

if __name__ == "__main__":
    main()
