import re
import os
import requests
import concurrent.futures

os.makedirs('covers', exist_ok=True)

def fetch_cover(title, author, file_prefix, book_id):
    query = f'intitle:{title}'
    if author and author != 'Unknown':
        query += f' inauthor:{author}'
    
    url = f'https://www.googleapis.com/books/v1/volumes?q={requests.utils.quote(query)}'
    try:
        res = requests.get(url, timeout=5)
        data = res.json()
        if 'items' in data:
            for item in data['items']:
                if 'imageLinks' in item.get('volumeInfo', {}):
                    img_url = item['volumeInfo']['imageLinks'].get('thumbnail', '')
                    if img_url:
                        # try to get higher res
                        img_url = img_url.replace('zoom=1', 'zoom=2').replace('&edge=curl', '')
                        if img_url.startswith('http:'):
                            img_url = img_url.replace('http:', 'https:')
                        
                        # download image
                        img_data = requests.get(img_url, timeout=5).content
                        filepath = f'covers/{file_prefix}-{book_id}.jpg'
                        with open(filepath, 'wb') as f:
                            f.write(img_data)
                        print(f'✅ Downloaded cover for {title}')
                        return filepath
    except Exception as e:
        print(f'❌ Failed for {title}: {e}')
    return None

def process_html(filename, prefix):
    if not os.path.exists(filename):
        return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # find all books
    books_blocks = re.findall(r'\{(?:[^{}]*?|\{[^{}]*\})*?\}', content)
    
    tasks = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for block in books_blocks:
            if 'title:' in block and 'id:' in block:
                try:
                    title_match = re.search(r'title:\s*[\'"](.*?)[\'"]', block)
                    author_match = re.search(r'author:\s*[\'"](.*?)[\'"]', block)
                    id_match = re.search(r'id:\s*(\d+)', block)
                    if title_match and id_match:
                        title = title_match.group(1)
                        author = author_match.group(1) if author_match else ''
                        book_id = id_match.group(1)
                        tasks.append(executor.submit(fetch_cover, title, author, prefix, book_id))
                except Exception as e:
                    pass

    concurrent.futures.wait(tasks)

print('Starting cover downloads...')
process_html('hindi-books.html', 'hindi')
process_html('browse.html', 'eng')
print('Finished!')
