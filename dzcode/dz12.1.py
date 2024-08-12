import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = re.sub(r'<[^>]*>', '', html)

    cleaned_lines = [line for line in cleaned_text.split('\n') if line.strip()]

    cleaned_text = '\n'.join(cleaned_lines)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)

    print(f"Cleaned text has been written to {result_file}")


delete_html_tags('draft.html')
