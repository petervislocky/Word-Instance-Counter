from components.instanceCounter import pdfExtract

def main():
    pdf = r'C:\Users\lilv4\OneDrive\Documents\AA-BigBook-4th-Edition.pdf'
    full_book = pdfExtract(pdf)
    print('Will return how many times a given word appears in a pdf')
    word_to_find = input('Enter a word: ')
    word_count = full_book.word_count(word_to_find)
    sentences_list = full_book.return_full_sentences(word_to_find)
    print(word_count)
    num = 0
    for sentence in sentences_list:
        num += 1
        print(num, sentence) # TODO format this better
    

if __name__ == '__main__':
    main()