import re
import os

# 1. hindi-books.html
content = open('hindi-books.html', 'r', encoding='utf-8').read()
content = re.sub(r'const ADDITIONAL_BOOKS\s*=\s*\[.*?\];\s*const BOOKS\s*=\s*\[.*?\];\s*const ALL_BOOKS = \[\.\.\.BOOKS, \.\.\.ADDITIONAL_BOOKS\];', 'const ALL_BOOKS = window.ALL_HINDI_BOOKS;\nconst FEATURED_BOOKS = ALL_BOOKS.filter(b => b.featured).slice(0, 10);', content, flags=re.DOTALL)
if '<script src=\"js/hindi-books-data.js\"></script>' not in content:
    content = content.replace('<script src=\"js/theme.js\"></script>', '<script src=\"js/theme.js\"></script>\n    <script src=\"js/hindi-books-data.js\"></script>')
open('hindi-books.html', 'w', encoding='utf-8').write(content)

# 2. hindi-book-detail.html
content = open('hindi-book-detail.html', 'r', encoding='utf-8').read()
content = re.sub(r'// Fetch hindi-books\.html.*?\}\)\(\);', '''
  const book = window.ALL_HINDI_BOOKS.find(b => b.id === bookId);
  if(book) renderBook(book);
  else document.getElementById('bookContent').innerHTML = `<p style="text-align:center;padding:3rem;color:#ef4444">Book #${bookId} not found. <a href="hindi-books.html">Browse books</a></p>`;
})();
''', content, flags=re.DOTALL)
if '<script src=\"js/hindi-books-data.js\"></script>' not in content:
    content = content.replace('<script src=\"js/theme.js\"></script>', '<script src=\"js/theme.js\"></script>\n<script src=\"js/hindi-books-data.js\"></script>')
open('hindi-book-detail.html', 'w', encoding='utf-8').write(content)

# 3. browse.html
content = open('browse.html', 'r', encoding='utf-8').read()
content = re.sub(r'const BOOKS\s*=\s*\[.*?\];', 'const BOOKS = window.ENGLISH_BOOKS_DATA;', content, flags=re.DOTALL)
if '<script src=\"js/english-books-data.js\"></script>' not in content:
    content = content.replace('<script src=\"js/theme.js\"></script>', '<script src=\"js/theme.js\"></script>\n    <script src=\"js/english-books-data.js\"></script>')
open('browse.html', 'w', encoding='utf-8').write(content)

# 4. book-detail.html
content = open('book-detail.html', 'r', encoding='utf-8').read()
content = re.sub(r'// Fetch browse\.html.*?\}\)\(\);', '''
  const book = window.ENGLISH_BOOKS_DATA.find(b => b.id === bookId);
  if(book) renderBook(book);
  else document.getElementById('bookContent').innerHTML = `<p style="text-align:center;padding:3rem;color:#ef4444">Book #${bookId} not found. <a href="browse.html">Browse books</a></p>`;
})();
''', content, flags=re.DOTALL)
if '<script src=\"js/english-books-data.js\"></script>' not in content:
    content = content.replace('<script src=\"js/theme.js\"></script>', '<script src=\"js/theme.js\"></script>\n<script src=\"js/english-books-data.js\"></script>')
open('book-detail.html', 'w', encoding='utf-8').write(content)

print('Patched successfully!')
