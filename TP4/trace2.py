import re

with open('readme.MD', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('# Índice')
if idx != -1:
    text = text[idx:]

text = text.replace('@todo', '')

def clean_heading(m):
    hashes = m.group(1)
    title = m.group(2)
    return f"{hashes} {title.strip()}"

text = re.sub(r'^(#+)\s+(?:SECCIÓN\s+\d+\s*[-—]\s*|\d+(?:\.\d+)*\s+)(.*)', clean_heading, text, flags=re.MULTILINE)

table_regex = re.compile(r'Tabla de distribución:.*?\| Ignacio Tula \|.*?\|', re.DOTALL)
text = table_regex.sub(lambda m: "TABLE", text)

print(repr(text[text.find("3.4 Cuarta Parte")-20:text.find("3.4 Cuarta Parte")+20]))
