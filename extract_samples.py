"""
Extract raw text from Hindi and Telugu PDFs to analyze format
"""

import PyPDF2

def extract_sample(pdf_path, output_path, max_pages=5):
    """Extract first few pages to analyze format"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            total_pages = len(pdf_reader.pages)
            print(f"PDF: {pdf_path}")
            print(f"Total pages: {total_pages}")
            
            text = ""
            for page_num in range(min(max_pages, total_pages)):
                page_text = pdf_reader.pages[page_num].extract_text()
                text += f"\n=== PAGE {page_num + 1} ===\n{page_text}\n"
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            
            print(f"Saved sample: {output_path}")
            return True
            
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    # Extract Hindi sample
    print("\n1. Hindi Dictionary:")
    extract_sample(
        r"i:\Banjara AI\Resources\banjara dictionary_hindi.pdf",
        r"i:\Banjara AI\hindi_sample.txt",
        max_pages=3
    )
    
    # Extract Telugu sample
    print("\n2. Telugu Dictionary:")
    extract_sample(
        r"i:\Banjara AI\Resources\banjara dictionary_Telugu Section.pdf",
        r"i:\Banjara AI\telugu_sample.txt",
        max_pages=3
    )
    
    # Extract Semantic Category
    print("\n3. Semantic Category Dictionary:")
    extract_sample(
        r"i:\Banjara AI\Resources\banjara dictionary_Semantic Category Section.pdf",
        r"i:\Banjara AI\semantic_sample.txt",
        max_pages=3
    )
    
    print("\nDone! Review the sample files to see the format.")
