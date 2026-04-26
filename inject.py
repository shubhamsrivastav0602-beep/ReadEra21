import sys

def inject(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    inject_str = """try { renderBooks(true); } catch(e) { document.body.innerHTML += '<h1 style=\"color:red;z-index:9999;position:fixed;top:0;\">' + e.message + '<br>' + e.stack + '</h1>'; }"""
    content = content.replace('renderBooks(true);', inject_str)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

inject('C:/Users/admin/Downloads/ReadEra/browse.html')
inject('C:/Users/admin/Downloads/ReadEra/hindi-books.html')
