'''
Columns:
    Book Id, Title, Author,	Author l-f,	Additional Authors,	ISBN, ISBN13	My Rating	Publisher	Binding	Number of Pages	Year Published	Original Publication Year	Date Read	Date Added	Bookshelves	Bookshelves with positions	Exclusive Shelf	My Review	Spoiler	Private Notes	Read Count	Owned Copies

- Filter by books with 'My Review'
- Sort by date
- Extract Title, Author and Review
'''
import csv
import string

HEADINGS = ['Book Id', 'Title', 'Author', 'Author l-f', 'Additional Authors', 'ISBN', 'ISBN13', 'My Rating', 'Publisher', 'Binding', 'Number of Pages', 'Year Published', 'Original Publication Year', 'Date Read', 'Date Added', 'Bookshelves', 'Bookshelves with positions', 'Exclusive Shelf', 'My Review', 'Spoiler', 'Private Notes', 'Read Count', 'Owned Copies']

REVIEW = 'My Review'
TITLE = 'Title'
AUTHOR = 'Author'
DATE = 'Date Read'


def extract_info():
    with open('goodreads_library_export.csv') as file:
        reader = csv.DictReader(file)
        read_books = []
        formatted_result = []
        for row in reader:
            # Filter by books with a review (not just read books)
            if not row[REVIEW]:
                continue
            read_books.append(row)
        # Sort by date I read the book
        for book in sorted(read_books, key=lambda book: book[DATE], reverse=True):
            formatted_result.append({
                'title': clean_title(book[TITLE]),
                'author': book[AUTHOR],
                'publish_date': book[DATE],
                'review': book[REVIEW]
            })
    return formatted_result

def clean_title(title: str):
    # Goodreads uses this format title (series - number_in_series) but we only want series, so we remove anything after opening brackets
    open_bracket = title.find('(')
    if open_bracket != -1:
        title = title[:open_bracket]
    title = title.rstrip()
    title = ''.join([char for char in title if char.isalnum() or char in (' ', '-', '&', ',', '.', '\'')])
    return title



def create_file(result):
    file_lines = ['---']
    file_lines.append(f'title: {result['title']}')
    file_lines.append(f'author: {result['author']}')
    file_lines.append(f'pubDate: {result['publish_date']}')
    file_lines.append('---')
    file_lines.append(result['review'])
    file_lines = [line + '\n' for line in file_lines]
    with open(f'src/content/book/{result['title']}.md', 'w') as file:
        file.writelines(file_lines)

def create_files(extracted_info):
    for info in extracted_info:
        create_file(info)

if __name__ == '__main__':
    extracted_info = extract_info()
    create_files(extracted_info)
