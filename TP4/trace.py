import re

with open('readme.MD', 'r', encoding='utf-8') as f:
    text = f.read()

print("Original:", repr(text[text.find("3.4 Cuarta Parte")-10:text.find("3.4 Cuarta Parte")+20]))

text = text.replace('@todo', '')

def clean_heading(m):
    hashes = m.group(1)
    title = m.group(2)
    return f"{hashes} {title.strip()}"

text2 = re.sub(r'^(#+)\s+(?:SECCIÓN\s+\d+\s*[-—]\s*|\d+(?:\.\d+)*\s+)(.*)', clean_heading, text, flags=re.MULTILINE)

print("After regex:", repr(text2[text2.find("3.4 Cuarta Parte")-10:text2.find("3.4 Cuarta Parte")+20]))
