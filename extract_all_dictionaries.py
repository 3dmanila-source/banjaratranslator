"""
Extract Multiple Dictionary PDFs and Merge
Processes English, Hindi, and Telugu dictionaries
"""

import PyPDF2
import json
import re
from collections import defaultdict

def extract_text_from_pdf(pdf_path):
    """Extract all text from PDF file"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            print(f"  Pages: {len(pdf_reader.pages)}")
            
            for page_num, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                text += page_text + "\n"
                if (page_num + 1) % 10 == 0:
                    print(f"  Extracted {page_num + 1} pages...")
                    
        return text
    except Exception as e:
        print(f"  Error: {e}")
        return None

def simplify_phonetic(text):
    """Convert phonetic transliteration to simple English letters"""
    import unicodedata
    
    # Remove diacritical marks
    result = ''.join(c for c in unicodedata.normalize('NFD', text) 
                     if unicodedata.category(c) != 'Mn')
    
    # Remove special characters, keep only letters
    result = re.sub(r'[^a-zA-Z\s]', '', result)
    
    return result.lower().strip()

def parse_english_dictionary(text):
    """Parse English-Banjara dictionary entries"""
    dictionary = {}
    lines = text.split('\n')
    word_types = ['v.', 'n.', 'adj.', 'adv.', 'pron.', 'conj.', 'num.', 'prop.']
    
    for line in lines:
        line = line.strip()
        if len(line) < 3:
            continue
        
        # Skip headers
        if any(skip in line for skip in ['English Section', 'Page', 'Section']):
            continue
        
        # Look for word type markers
        if any(wt in line for wt in word_types):
            parts = line.split(maxsplit=1)
            
            if len(parts) >= 1:
                english = parts[0].strip().lower()
                
                if len(english) > 30 or not english.replace('-', '').replace(' ', '').isalpha():
                    continue
                
                # Extract transliteration
                if '/' in line:
                    trans_parts = line.split('/')
                    if len(trans_parts) >= 2:
                        transliteration = trans_parts[1].strip().split()[0]
                        transliteration = simplify_phonetic(transliteration)
                        
                        if english and transliteration:
                            dictionary[english] = transliteration
    
    return dictionary

def parse_hindi_dictionary(text):
    """Parse Hindi-Banjara dictionary entries"""
    # Similar logic but adapted for Hindi script
    dictionary = {}
    # TODO: Implement Hindi-specific parsing
    # For now, return empty dict
    return dictionary

def parse_telugu_dictionary(text):
    """Parse Telugu-Banjara dictionary entries"""
    # Similar logic but adapted for Telugu script
    dictionary = {}
    # TODO: Implement Telugu-specific parsing
    # For now, return empty dict
    return dictionary

def merge_dictionaries(*dicts):
    """Merge multiple dictionaries, keeping longest translation for duplicates"""
    merged = {}
    sources = defaultdict(list)
    
    for idx, d in enumerate(dicts):
        for key, value in d.items():
            if key not in merged:
                merged[key] = value
                sources[key].append(f"dict{idx+1}")
            else:
                # Keep longer/better translation
                if len(value) > len(merged[key]):
                    merged[key] = value
                sources[key].append(f"dict{idx+1}")
    
    return merged, sources

def main():
    base_path = r"i:\Banjara AI\Resources"
    
    dictionaries = []
    labels = []
    
    # English dictionary
    print("\n1. Extracting English-Banjara dictionary...")
    english_path = f"{base_path}\\banjara dictionary_english.pdf"
    text = extract_text_from_pdf(english_path)
    if text:
        eng_dict = parse_english_dictionary(text)
        dictionaries.append(eng_dict)
        labels.append("English")
        print(f"  ✓ Extracted {len(eng_dict)} entries")
    
    # Hindi dictionary
    print("\n2. Extracting Hindi-Banjara dictionary...")
    hindi_path = f"{base_path}\\banjara dictionary_hindi.pdf"
    try:
        text = extract_text_from_pdf(hindi_path)
        if text:
            hindi_dict = parse_hindi_dictionary(text)
            dictionaries.append(hindi_dict)
            labels.append("Hindi")
            print(f"  ✓ Extracted {len(hindi_dict)} entries")
    except:
        print("  ! Hindi dictionary not found or cannot be processed")
    
    # Telugu dictionary
    print("\n3. Extracting Telugu-Banjara dictionary...")
    telugu_path = f"{base_path}\\banjara dictionary_telugu.pdf"
    try:
        text = extract_text_from_pdf(telugu_path)
        if text:
            telugu_dict = parse_telugu_dictionary(text)
            dictionaries.append(telugu_dict)
            labels.append("Telugu")
            print(f"  ✓ Extracted {len(telugu_dict)} entries")
    except:
        print("  ! Telugu dictionary not found or cannot be processed")
    
    # Merge all dictionaries
    print("\n4. Merging dictionaries...")
    if dictionaries:
        merged, sources = merge_dictionaries(*dictionaries)
        print(f"  ✓ Total unique entries: {len(merged)}")
        
        # Save merged dictionary
        output_path = r"i:\Banjara AI\dictionary_merged.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(merged, f, ensure_ascii=True, indent=2)
        
        print(f"\n✓ Saved merged dictionary: {output_path}")
        
        # Show statistics
        print("\n📊 Statistics:")
        for label, d in zip(labels, dictionaries):
            print(f"  {label}: {len(d)} entries")
        print(f"  Merged: {len(merged)} unique entries")
        
        # Show sample
        print("\n📝 Sample entries:")
        for i, (eng, ban) in enumerate(list(merged.items())[:5]):
            print(f"  {eng} → {ban}")

if __name__ == "__main__":
    main()
