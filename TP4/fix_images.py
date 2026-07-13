import re

with open('readme.MD', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix typo from the user's markdown
text = text.replace('Instalalación', 'Instalación')

# Force double newlines before any image if there is only a single newline
text = re.sub(r'([^\n])\s*\n(\s*!\[.*?\]\(.*?\))', r'\1\n\n\2', text)

# Force double newlines after any image if there is only a single newline
text = re.sub(r'(!\[.*?\]\(.*?\))\n\s*([^\n])', r'\1\n\n\2', text)

with open('readme.MD', 'w', encoding='utf-8') as f:
    f.write(text)
