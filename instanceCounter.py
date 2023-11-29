import fitz
import re


class pdfExtract:

    def __init__(self, pdf_path) -> None:
        self.pdf_path = pdf_path
        
    def extract_text(self):
        book = fitz.open(self.pdf_path)
        text = ''
        for page_number in range(book.page_count):
            page = book[page_number]
            text += page.get_text()
        book.close()
        return text
    
    def get_text_from_page(self, page_number):
        book = fitz.open(self.pdf_path)
        if 1 <= page_number < book.page_count:
            page = book[page_number]
            text = page.get_text()
            book.close()
            return text
        else:
            book.close()
            return None

    def word_count(self, target_word):
        full_text = self.extract_text()
        # converting to lowercase to find all instances regardless of case
        full_text_lower = full_text.lower()
        target_word_lower = target_word.lower()
        count = 0
        index = full_text_lower.find(target_word_lower)
        while index != -1:
            count += 1
            index = full_text_lower.find(target_word_lower, index + 1)
        return count

        #pattern = re.compile(r'\b' + re.escape(target_word_lower) + r'\b|\b' + re.escape(target_word_lower)+ r'[-,;:".?!\'(\\/)]?\w+\b')
        #count = len(pattern.findall(full_text_lower))
        #return count
            

def test():
    pdf = r'C:\Users\lilv4\OneDrive\Documents\AA-BigBook-4th-Edition.pdf'
    full_book = pdfExtract(pdf)
    word = 'faith'
    print(full_book.word_count(word))
    
    

if __name__ == '__main__':
    test()