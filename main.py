from components.instanceCounter import pdfExtract

def main():
    pdf = input('Enter the file path of a pdf document \
(if none press enter and program will default to the book Alcoholics Anonymous): ')
    if pdf == '':
        pdf = r'C:\Users\lilv4\OneDrive\Documents\AA-BigBook-4th-Edition.pdf'
    full_book = pdfExtract(pdf)
    print('Will return how many times a given word appears in a pdf')
    word_to_find = input('Enter a word: ')
    wordCount = full_book.word_count(word_to_find)
    print(wordCount)
    

if __name__ == '__main__':
    main()