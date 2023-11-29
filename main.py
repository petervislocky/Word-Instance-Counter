from components.instanceCounter import pdfExtract

def main():
    pdf = input('Enter the file path of a pdf document (if none '
    'press enter and program will default to the book Alcoholics Anonymous): ')
    raw_pdf = rf'{pdf}'
    if pdf == '':
        raw_pdf = r'C:\Users\lilv4\OneDrive\Documents\AA-BigBook-4th-Edition.pdf'
    full_book = pdfExtract(raw_pdf)
    print('Will return how many times a given word appears in a pdf')
    word_to_find = input('Enter a word: ')
    word_count = full_book.word_count(word_to_find)
    sentences_list = full_book.return_full_sentences(word_to_find)
    print(word_count)
    for sentences in sentences_list:
        print(sentences, sep='\n')
    
    

if __name__ == '__main__':
    main()