import re

def check_newlines_in_strings(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
    if not script_match:
        return
    script = script_match.group(1)
    
    lines = script.split('\n')
    for i, line in enumerate(lines):
        # count unescaped quotes
        dq_count = len(re.findall(r'(?<!\\)\"', line))
        if dq_count % 2 != 0:
            print(f'{path} Line {i+1} has unmatched double quote: {line.strip()[:100]}')

check_newlines_in_strings('C:/Users/admin/Downloads/ReadEra/browse.html')
check_newlines_in_strings('C:/Users/admin/Downloads/ReadEra/hindi-books.html')
