import nltk
from components.instanceCounter import pdfExtract

nltk.download('punkt')


DEFAULT_PATH = r'C:\Users\lilv4\OneDrive\Documents\AA-BigBook-4th-Edition.pdf'


def get_user_pdf_path():
    user_pdf = input('Enter the path of the pdf file you would like to search: ')
    return   rf'{user_pdf}' if user_pdf else DEFAULT_PATH

def analyze_pdf(pdf_path):
    full_book = pdfExtract(pdf_path)
    word_to_find = input('Enter a word: ')
    word_count = full_book.word_count(word_to_find)
    sentences_list = full_book.return_full_sentences(word_to_find)
    return word_to_find, word_count, sentences_list

def display_sentences(sentences_list):
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
            
            print(f'Showing {output_count} out of {len(sentences_list)} results')
            see_more = input('See more? (y/n) ')

            if see_more.lower() == 'n':
                break

            if see_more.lower() != 'y' and see_more.lower() != 'n':
                print('Invalid input, defualting to yes')
                continue
        
        print(f'Showing {output_count} out of {len(sentences_list)} results')

def main():
    while True:
        print('Will return how many times a given word appears in a pdf\n'
              'Press Enter to default to the Big Book of AA')
        pdf_path = get_user_pdf_path()
        word_to_find, word_count, sentences_list = analyze_pdf(pdf_path)
        print(f'{word_to_find} appears {word_count} times in this PDF\n')
        display_sentences(sentences_list)
        
        run_again = input('Run the program again? (y/n) ')
        
        if run_again.lower() == 'n':
            break
        if run_again.lower() != 'n' and run_again.lower() != 'y':
            print('Invalid input, defaulting to yes')
            continue

if __name__ == '__main__':
    main()