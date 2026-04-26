import re

def replace_covers(path, is_hindi=False):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace the book-cover-wrap and its contents.
    # We will find where it starts, and where the next major div starts (like book-info or lib-btn or book-license)
    
    # For browse.html renderCard
    new_cover = """<div class="book-cover-wrap" style="position:relative; overflow:hidden; border-radius: 4px 12px 12px 4px; box-shadow: inset -5px 0 15px rgba(0,0,0,0.3), inset 10px 0 20px rgba(255,255,255,0.1), 0 5px 15px rgba(0,0,0,0.2); background: ${getGradient(book.category)}; width:100%; height:260px;">
                <div style="position:absolute; left: 12px; top:0; bottom:0; width:3px; background: rgba(255,255,255,0.15); box-shadow: 2px 0 5px rgba(0,0,0,0.2);"></div>
                <div class="book-cover-placeholder" style="display:flex;width:100%;height:100%;flex-direction:column;align-items:center;justify-content:center;padding:1.5rem 1rem 1.5rem 1.8rem;text-align:center;box-sizing:border-box;">
                    <span style="font-size:2.5rem; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.4));">${book.coverEmoji || '📚'}</span>
                    <span style="font-size:1.15rem;color:#f8f9fa;font-family:'Georgia',serif;font-weight:700;margin-top:0.75rem; line-height:1.3; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">${escHtml((book.title || '').substring(0,40))}</span>
                    <span style="font-size:0.75rem;color:#e2e8f0;text-transform:uppercase;letter-spacing:1.5px;margin-top:0.5rem;font-weight:600;">${escHtml((book.author || '').substring(0,25))}</span>
                </div>"""
                
    # In hindi-books.html, escHtml might not exist, but we can add it or just not use it if it's safe.
    # Actually hindi-books.html doesn't use escHtml. It uses template literal directly.
    new_cover_hindi = """<div class="book-cover-wrap" style="position:relative; overflow:hidden; border-radius: 4px 12px 12px 4px; box-shadow: inset -5px 0 15px rgba(0,0,0,0.3), inset 10px 0 20px rgba(255,255,255,0.1), 0 5px 15px rgba(0,0,0,0.2); background: ${book.coverGradient || getGradient(book.id)}; width:100%; height:220px;">
                <div style="position:absolute; left: 12px; top:0; bottom:0; width:3px; background: rgba(255,255,255,0.15); box-shadow: 2px 0 5px rgba(0,0,0,0.2);"></div>
                <div class="book-cover-placeholder" style="display:flex;width:100%;height:100%;flex-direction:column;align-items:center;justify-content:center;padding:1.5rem 1rem 1.5rem 1.8rem;text-align:center;box-sizing:border-box;">
                    <span style="font-size:2.5rem; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.4));">${book.coverEmoji || '📚'}</span>
                    <span style="font-size:1.0rem;color:#f8f9fa;font-weight:700;margin-top:0.75rem; line-height:1.3; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">${(book.title || '').substring(0,40)}</span>
                    <span style="font-size:0.75rem;color:#e2e8f0;text-transform:uppercase;letter-spacing:1.5px;margin-top:0.5rem;font-weight:600;">${(book.author || '').substring(0,25)}</span>
                </div>
            </div>"""

    # For featured covers
    new_featured = """<div class="featured-cover" style="position:relative; overflow:hidden; border-radius: 4px 12px 12px 4px; box-shadow: inset -5px 0 15px rgba(0,0,0,0.3), inset 10px 0 20px rgba(255,255,255,0.1), 0 5px 15px rgba(0,0,0,0.2); background: ${getGradient(book.category)}; width:160px; height:240px; flex-shrink:0;">
                <div style="position:absolute; left: 12px; top:0; bottom:0; width:3px; background: rgba(255,255,255,0.15); box-shadow: 2px 0 5px rgba(0,0,0,0.2);"></div>
                <div class="book-cover-placeholder" style="display:flex;width:100%;height:100%;flex-direction:column;align-items:center;justify-content:center;padding:1rem 0.5rem 1rem 1.2rem;text-align:center;box-sizing:border-box;">
                    <span style="font-size:3rem; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.4));">${book.coverEmoji || '📚'}</span>
                    <span style="font-size:1rem;color:#f8f9fa;font-family:'Georgia',serif;font-weight:700;margin-top:0.5rem; line-height:1.2; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">${escHtml((book.title || '').substring(0,30))}</span>
                </div>
            </div>"""

    new_featured_hindi = """<div class="featured-cover" style="position:relative; overflow:hidden; border-radius: 4px 12px 12px 4px; box-shadow: inset -5px 0 15px rgba(0,0,0,0.3), inset 10px 0 20px rgba(255,255,255,0.1), 0 5px 15px rgba(0,0,0,0.2); background: ${book.coverGradient || getGradient(book.id)}; width:160px; height:240px; flex-shrink:0; margin-bottom:1rem;">
                <div style="position:absolute; left: 12px; top:0; bottom:0; width:3px; background: rgba(255,255,255,0.15); box-shadow: 2px 0 5px rgba(0,0,0,0.2);"></div>
                <div class="book-cover-placeholder" style="display:flex;width:100%;height:100%;flex-direction:column;align-items:center;justify-content:center;padding:1rem 0.5rem 1rem 1.2rem;text-align:center;box-sizing:border-box;">
                    <span style="font-size:3rem; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.4));">${book.coverEmoji || '📚'}</span>
                    <span style="font-size:0.95rem;color:#f8f9fa;font-weight:700;margin-top:0.5rem; line-height:1.2; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">${(book.title || '').substring(0,30)}</span>
                </div>
            </div>"""
            
    if not is_hindi:
        # replace renderCard cover
        content = re.sub(r'<div class="book-cover-wrap".*?</div>\s*<button class="lib-btn', new_cover + '\n                <button class="lib-btn', content, flags=re.DOTALL)
        # replace renderFeatured cover
        content = re.sub(r'<img class="featured-cover".*?</div>\s*<div class="featured-info">', new_featured + '\n                <div class="featured-info">', content, flags=re.DOTALL)
    else:
        # replace hindi-books renderBooks
        content = re.sub(r'<div class="book-cover-wrap".*?</div>\s*<span class="book-license">', new_cover_hindi + '\n                    <span class="book-license">', content, flags=re.DOTALL)
        # replace hindi-books renderFeatured
        content = re.sub(r'<div class="featured-cover-wrap".*?</div>\s*</div>\s*<h3 class="featured-title">', new_featured_hindi + '\n                <h3 class="featured-title">', content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

replace_covers('C:/Users/admin/Downloads/ReadEra/browse.html', False)
replace_covers('C:/Users/admin/Downloads/ReadEra/hindi-books.html', True)
