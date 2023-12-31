import fitz
from nltk.tokenize import sent_tokenize

class pdfExtract:

    def __init__(self, pdf_path) -> None:
        self.pdf_path = pdf_path
        
    def extract_text(self):
        """Extracts readable text from fitz object"""
        book = fitz.open(self.pdf_path)
        text = ''
        
        for page_number in range(book.page_count):
            page = book[page_number]
            text += page.get_text()
        book.close()
        return text
    
    def get_text_from_page(self, page_number):
        """Returns readable text from a specific page number only"""
        book = fitz.open(self.pdf_path)
        
        if 1 <= page_number < book.page_count:
            page = book[page_number]
            text = page.get_text()
            book.close()
            return text
        else:
            print('Page number does not exist')
            book.close()
            return None

    def word_count(self, target_word):
        """Returns number of instances of target_word in PDF"""
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
    
    def return_full_sentences(self, target_word):
        """ Returns each sentence containing target_word in PDF.
            Uses nltk as a dependency, 'punkt' must be downloaded 
            at beginning of script """
        full_text = self.extract_text()
        sentences = sent_tokenize(full_text)
        target_sentences = []
        
        for sentence in sentences:
            if target_word.lower() in sentence.lower():
                # replacing target_word with itself in bold text, using the ANSI escape code for bold
                # and underlined
                highlighted_sentence = sentence.replace(target_word, f'\033[1;4m{target_word}\033[0m')
                target_sentences.append(highlighted_sentence)
        return target_sentences
