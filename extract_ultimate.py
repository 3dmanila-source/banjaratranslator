"""
ULTIMATE Dictionary Extractor - Captures EVERY possible entry
Handles all edge cases and formats
"""

import json
import re
import unicodedata

def simplify_phonetic(text):
    """Convert phonetic transliteration to simple English letters"""
    result = ''.join(c for c in unicodedata.normalize('NFD', text) 
                     if unicodedata.category(c) != 'Mn')
    result = re.sub(r'[^a-zA-Z\s]', '', result)
    return result.lower().strip()

def extract_ultimate(text):
    """Extract EVERY English-Banjara pair possible"""
    dictionary = {}
    lines = text.split('\n')
    
    word_types = ['v.', 'n.', 'adj.', 'adv.', 'pron.', 'conj.', 'num.', 'prop.']
    
    for line in lines:
        line = line.strip()
        if len(line) < 3:
            continue
        
        # Skip headers
        if any(skip in line for skip in ['English Section', 'Page', 'Section', 'ఆంగ', '===', '---']):
            continue
        
        # Skip single letters (section markers like "B", "C")
        if len(line) == 1:
            continue
        
        # METHOD 1: Lines with /transliteration/
        if '/' in line:
            # Extract first English word (before any space, Telugu script, or word type)
            english_match = re.match(r'^([a-zA-Z][a-zA-Z\s\-\']*?)\s+', line)
            if english_match:
                english = english_match.group(1).strip().lower()
                
                # Validate English word
                if len(english) > 35:
                    continue
                
                # Extract all transliterations
                trans_matches = re.findall(r'/([^/]+)/', line)
                if trans_matches:
                    # Use longest/best transliteration
                    for trans in trans_matches:
                        simplified = simplify_phonetic(trans)
                        if simplified and len(simplified) > 1:
                            # Keep best (longest) translation
                            if english not in dictionary or len(simplified) > len(dictionary[english]):
                                dictionary[english] = simplified
                            break  # Take first valid one
        
        # METHOD 2: Lines without slashes but with word types
        # Format: "english  word_type. script"
        elif any(wt in line for wt in word_types):
            # Try to extract English word before word type
            for wt in word_types:
                if wt in line:
                    before_wt = line.split(wt)[0].strip()
                    english_match = re.match(r'^([a-zA-Z][a-zA-Z\s\-\']*?)\s*$', before_wt)
                    if english_match:
                        english = english_match.group(1).strip().lower()
                        
                        if len(english) > 1 and len(english) < 35:
                            # Extract Telugu/Banjara script and transliterate
                            after_wt = line.split(wt, 1)[1] if wt in line else ''
                            # Look for word after word type (before any other marker)
                            script_match = re.search(r'([^\s/]+)', after_wt)
                            if script_match:
                                script = script_match.group(1).strip()
                                simplified = simplify_phonetic(script)
                                if simplified and len(simplified) > 1:
                                    if english not in dictionary:
                                        dictionary[english] = simplified
                    break
        
        # METHOD 3: Simple format "english  script" (no word type, no slash)
        # This catches entries like "apple  Ľేపు"
        else:
            # Try to split on multiple spaces or Telugu script
            parts = re.split(r'\s{2,}', line, maxsplit=1)
            if len(parts) == 2:
                english_candidate = parts[0].strip().lower()
                script = parts[1].strip()
                
                # Validate: English on left, non-English on right
                if (len(english_candidate) > 1 and len(english_candidate) < 35 and
                    english_candidate.replace('-', '').replace("'", '').replace(' ', '').isalpha() and
                    not script.isascii()):
                    
                    simplified = simplify_phonetic(script.split()[0])  # Take first word
                    if simplified and len(simplified) > 1:
                        if english_candidate not in dictionary:
                            dictionary[english_candidate] = simplified
    
    return dictionary

def main():
    text_path = r"i:\Banjara AI\extracted_text.txt"
    
    print("Loading extracted text...")
    with open(text_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("Extracting ALL entries (ultimate parser)...")
    dictionary = extract_ultimate(text)
    
    print(f"\nExtracted {len(dictionary)} unique entries")
    
    # Save ultimate version
    output_path = r"i:\Banjara AI\dictionary_ultimate.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=True, indent=2, sort_keys=True)
    
    print(f"Saved to: {output_path}")
    
    # Statistics
    print("\n=== RESULTS ===")
    print(f"  Total entries: {len(dictionary)}")
    print(f"  v1.0 (original): 1,968")
    print(f"  v2.0 (improved): 2,180")
    print(f"  v3.0 (ultimate): {len(dictionary)}")
    print(f"  NEW entries: +{len(dictionary) - 1968}")
    
    # Also update main dictionary
    main_dict_path = r"i:\Banjara AI\dictionary.json"
    with open(main_dict_path, 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=True, indent=2, sort_keys=True)
    
    print(f"\nUpdated main dictionary.json with {len(dictionary)} entries")
    
    # Sample
    print("\n=== Sample (first 10) ===")
    for i, (eng, ban) in enumerate(list(dictionary.items())[:10]):
        print(f"  {eng} -> {ban}")
    
    print("\nDone!")

if __name__ == "__main__":
    main()
