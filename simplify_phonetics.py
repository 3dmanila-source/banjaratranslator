"""
Simplify Phonetic Transliterations
Converts special characters and diacritical marks to plain English letters
"""

import json
import re

def simplify_phonetic(text):
    """
    Convert phonetic transliteration to simple English letters
    Removes all diacritical marks and special characters
    """
    # Define character mappings
    mappings = {
        # Vowels with diacritics
        'ā': 'a', 'á': 'a', 'à': 'a', 'ă': 'a', 'ą': 'a',
        'ē': 'e', 'é': 'e', 'è': 'e', 'ě': 'e', 'ę': 'e',
        'ī': 'i', 'í': 'i', 'ì': 'i', 'î': 'i',
        'ō': 'o', 'ó': 'o', 'ò': 'o', 'ô': 'o', 'ǭ': 'o',
        'ū': 'u', 'ú': 'u', 'ù': 'u', 'û': 'u',
        
        # Consonants with diacritics
        'ḍ': 'd', 'ḍ': 'd', 'đ': 'd',
        'ṭ': 't', 'ț': 't',
        'ṇ': 'n', 'ñ': 'n', 'ń': 'n',
        'ṣ': 's', 'ś': 's', 'š': 's',
        'ṛ': 'r', 'ř': 'r',
        'ḷ': 'l', 'ĺ': 'l',
        'ṁ': 'm', 'ṃ': 'm',
        'ṅ': 'ng',
        'ñ': 'ny',
        'ḥ': 'h',
        'ǘ': 'u',
        'ǯ': 'j',
        'ǳ': 'ti',
        'ǵ': 'ni',
        'Ǭ': 'ch',
        'ǽ': 'mi',
        'Ǯ': 'j',
        'Ƕ': 'n',
        'Ƿ': 'p',
        'Ĳ': 'n',
        'ĵ': 'bh',
        'ķ': 'y',
        'Ĺ': 'l',
        'Ľ': 's',
        'ĭ': 'dh',
        'İ': 'd',
        'ı': 'dh',
        'Ĩ': 'ch',
        'ĩ': 'ch',
        'Ħ': 'g',
        'ȇ': 'vi',
        'Ȁ': 'm',
        'Ȃ': 'y',
        'ȃ': 'l',
        'Ȅ': 'l',
        'ȅ': 'l',
        'Ȇ': 'l',
        'ȏ': 'h',
        'Ȏ': 's',
        'ț': 'h',
        'Ț': 't',
        'Ĵ': 'ph',
        'ǹ': 'bh',
        'Ǹ': 'ph',
        'ǻ': 'bh',
        'Ǻ': 'b',
        'Ǽ': 'bh',
        'Ǿ': 'm',
        'ǿ': 'm',
        'Ȉ': 'v',
        'Ȋ': 'sh',
        'ȋ': 'sh',
        'Ȍ': 'sh',
        'Ȉ': 'v',
        
        # Special characters
        'ṁ': 'm', 'm̐': 'm', 'ṅ': 'ng', 'n̄': 'n',
        'ḍ': 'd', 'ṭ': 't', 'ḷ': 'l', 'ṛ': 'r',
        'ś': 'sh', 'ṣ': 'sh',
    }
    
    result = text
    
    # Apply mappings
    for old_char, new_char in mappings.items():
        result = result.replace(old_char, new_char)
    
    # Remove any remaining diacritical marks using Unicode normalization
    import unicodedata
    result = ''.join(c for c in unicodedata.normalize('NFD', result) 
                     if unicodedata.category(c) != 'Mn')
    
    # Remove any remaining special characters, keep only letters and spaces
    result = re.sub(r'[^a-zA-Z\s]', '', result)
    
    # Convert to lowercase and clean up spaces
    result = result.lower().strip()
    
    return result

def simplify_dictionary(input_file, output_file):
    """Convert entire dictionary to simplified phonetics"""
    
    print(f"Loading dictionary from {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        dictionary = json.load(f)
    
    print(f"Original entries: {len(dictionary)}")
    
    # Simplify all values
    simplified = {}
    for english, phonetic in dictionary.items():
        simple = simplify_phonetic(phonetic)
        if simple:  # Only add if not empty after simplification
            simplified[english] = simple
    
    print(f"Simplified entries: {len(simplified)}")
    
    # Save simplified dictionary
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(simplified, f, ensure_ascii=True, indent=2)
    
    print(f"\n✅ Saved simplified dictionary to {output_file}")
    
    # Show some examples
    print("\n📝 Sample conversions:")
    count = 0
    for eng, orig in list(dictionary.items())[:10]:
        simp = simplified.get(eng, '')
        if simp:
            print(f"  {eng}: '{orig}' → '{simp}'")
            count += 1
    
    return simplified

if __name__ == "__main__":
    input_path = r"i:\Banjara AI\dictionary.json"
    output_path = r"i:\Banjara AI\dictionary_simplified.json"
    
    simplified_dict = simplify_dictionary(input_path, output_path)
    
    print(f"\n✨ Done! Created simplified dictionary with {len(simplified_dict)} entries")
