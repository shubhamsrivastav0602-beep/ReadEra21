import os

def update_file(filename, prefix):
    if not os.path.exists(filename):
        return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # In book-detail.html and hindi-book-detail.html:
    content = content.replace(
        'return `https://archive.org/services/img/${book.identifier||book.id}`;',
        f'return `covers/{prefix}-${{book.id}}.jpg`;'
    )
    
    # In the renderCard / renderBooks
    content = content.replace(
        'onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'"',
        'onerror="this.onerror=null; this.src=\\\'https://archive.org/services/img/\\\' + (typeof book !== \\\'undefined\\\' ? book.identifier : \\\'\\\'); setTimeout(()=>{if(!this.complete||this.naturalHeight===0){this.style.display=\\\'none\\\';this.nextElementSibling.style.display=\\\'flex\\\';}}, 1500);"'
    )
    
    # In browse.html, getCoverUrl(identifier)
    content = content.replace(
        'function getCoverUrl(identifier) {',
        'function getCoverUrl(identifier, id) { return `covers/eng-${id}.jpg`; }\n    function getCoverUrlOld(identifier) {'
    )
    content = content.replace('getCoverUrl(book.identifier)', 'getCoverUrl(book.identifier, book.id)')
    
    # In hindi-books.html
    content = content.replace(
        'const cover = `https://archive.org/services/img/${book.identifier}`;',
        f'const cover = `covers/{prefix}-${{book.id}}.jpg`;'
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('browse.html', 'eng')
update_file('hindi-books.html', 'hindi')
update_file('book-detail.html', 'eng')
update_file('hindi-book-detail.html', 'hindi')
print('Updated HTML files.')
