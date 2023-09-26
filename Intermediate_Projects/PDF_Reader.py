import re
from collections import Counter
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file: str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)

        print('Pages', len(reader.pages))
        print('-' * 18)  # Divider!

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text


def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(
            r'\s+|[,;?!.-]\s*', text.lower())  # removing special chars
        # print(split_text)

        all_words += [word for word in split_text if word]
    return Counter(all_words)


def count_letters(char_list: list[str]) -> int:
    all_char: list[str] = []
    for char in char_list:
        split_text: list[str] = re.split(
            r'\s+|[,;?!.-]\s*', char.lower())
        total_characters: int = sum(len(char) for char in char_list)
    return total_characters


def main():
    extracted_text: list[str] = extract_text_from_pdf(
        'sample.pdf')  # Enter file name here!
    counter: Counter = count_words(text_list=extracted_text)
    letter_counter: Counter = count_letters(extracted_text)

    for page in extracted_text:
        print(page)

    for word, mention in counter.most_common(5):
        print(f'{word:10}: {mention} times')

    print(f'Total characters in PDF: {letter_counter}')


if __name__ == '__main__':
    main()
