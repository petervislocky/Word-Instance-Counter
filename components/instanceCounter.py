import fitz


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