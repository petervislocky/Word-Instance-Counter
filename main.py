import nltk
from components.instanceCounter import pdfExtract

nltk.download('punkt')

def main():
    pdf = r'C:\Users\lilv4\OneDrive\Documents\AA-BigBook-4th-Edition.pdf'
    full_book = pdfExtract(pdf)

    print('Will return how many times a given word appears in a pdf')
    word_to_find = input('Enter a word: ')
    word_count = full_book.word_count(word_to_find)
    sentences_list = full_book.return_full_sentences(word_to_find)
    print(word_count)
   
    num = 0
    output_count = 0

    while num < len(sentences_list):
        
        for i in range(20):
            if num < len(sentences_list):
                output_count += 1
                print(f'{output_count}: {sentences_list[num]}\n')
                num += 1
            else:
                break
        
        if num >= len(sentences_list):
            break
        
        see_more = input('See more? (y/n) ')

        if see_more.lower() == 'n':
            break

        if see_more.lower() != 'y' and see_more.lower() != 'n':
            print('Invalid input, defualting to yes\n')
            continue

if __name__ == '__main__':
    main()