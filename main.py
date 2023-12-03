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
    #this while loop is busted I just am too tired to fix it now
    outputCount = 0
    while outputCount < 20:
        outputCount += 1    
        for sentence in sentences_list:
            num += 1
            print(f'{num}: {sentence}\n')
        seeMore = input('See more? (y/n)')
        if seeMore.lower() == 'y':
            outputCount = 0
        else:
            break

if __name__ == '__main__':
    main()