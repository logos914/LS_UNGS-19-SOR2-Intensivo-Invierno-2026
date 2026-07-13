import re

with open('template_informe/readme_stripped.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace box drawing characters and bullet points that latex doesn't understand easily
text = text.replace('●', '*')
text = text.replace('├', '+')
text = text.replace('─', '-')
text = text.replace('└', '+')
text = text.replace('', '')

with open('template_informe/readme_stripped.md', 'w', encoding='utf-8') as f:
    f.write(text)

