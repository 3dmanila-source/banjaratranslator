"""
Dictionary Extraction Script
Extracts English-Banjara word pairs from PDF dictionary
"""

import PyPDF2
import re
import json

def extract_text_from_pdf(pdf_path):
    """Extract all text from PDF file"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            print(f"Total pages: {len(pdf_reader.pages)}")
            
            for page_num, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                text += page_text + "\n"
                print(f"Extracted page {page_num + 1}")
                
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def parse_dictionary_entries(text):
    """
    Parse dictionary text to extract English-Banjara word pairs
    Format: "english  word_type. బంజార_స్క్రిప్ట్  /transliteration/"
    """
    dictionary = {}
    
    # Split into lines
    lines = text.split('\n')
    
    # Word type markers
    word_types = ['v.', 'n.', 'adj.', 'adv.', 'pron.', 'conj.', 'num.', 'prop.']
    
    for line in lines:
        line = line.strip()
        if not line or len(line) < 3:
            continue
        
        # Skip headers and page numbers
        if any(skip in line for skip in ['English Section', 'ఆంగ', 'Page', 'Section']):
            continue
        
        # Look for word type markers
        has_word_type = any(wt in line for wt in word_types)
        
        if has_word_type:
            # Try to extract english word and transliteration
            # Pattern: "english  word_type. script /transliteration/"
            parts = line.split(maxsplit=1)
            
            if len(parts) >= 1:
                english = parts[0].strip().lower()
                
                # Skip if english word is too long or has weird characters
                if len(english) > 30 or not english.replace('-', '').replace(' ', '').isalpha():
                    continue
                
                # Extract transliteration if available (between / /)
                if '/' in line:
                    trans_parts = line.split('/')
                    if len(trans_parts) >= 2:
                        transliteration = trans_parts[1].strip()
                        
                        # Clean the transliteration
                        transliteration = transliteration.split()[0] if transliteration else ""
                        
                        if english and transliteration:
                            dictionary[english] = transliteration
    
    return dictionary

def save_to_json(dictionary, output_path):
    """Save dictionary to JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(dictionary)} entries to {output_path}")

def main():
    # PDF path
    pdf_path = r"i:\Banjara AI\Resources\banjara dictionary_english.pdf"
    
    print("Starting dictionary extraction...")
    print(f"Reading: {pdf_path}")
    
    # Extract text
    text = extract_text_from_pdf(pdf_path)
    
    if text:
        # Save raw text for inspection
        with open(r"i:\Banjara AI\extracted_text.txt", 'w', encoding='utf-8') as f:
            f.write(text)
        print("Raw text saved to extracted_text.txt")
        
        # Parse dictionary
        dictionary = parse_dictionary_entries(text)
        
        # Save to JSON
        save_to_json(dictionary, r"i:\Banjara AI\dictionary.json")
        
        # Print sample entries
        print("\nSample entries:")
        for i, (eng, ban) in enumerate(list(dictionary.items())[:10]):
            print(f"{eng} → {ban}")
            if i >= 9:
                break
        
        print(f"\nTotal entries extracted: {len(dictionary)}")
    else:
        print("Failed to extract text from PDF")

if __name__ == "__main__":
    main()
