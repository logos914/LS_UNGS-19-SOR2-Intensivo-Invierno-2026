with open('readme.MD', 'r', encoding='utf-8') as f: text = f.read()
import re
print("Orig:", repr(text[text.find('3.4 Cuarta'):text.find('3.4 Cuarta')+10]))

idx = text.find('# Índice')
if idx != -1: text = text[idx:]

text = text.replace('@todo', '')

def clean_heading(m):
    return f"{m.group(1)} {m.group(2).strip()}"

text2 = re.sub(r'^(#+)\s+(?:SECCIÓN\s+\d+\s*[-—]\s*|\d+(?:\.\d+)*\s+)(.*)', clean_heading, text, flags=re.MULTILINE)
print("After clean_heading:", repr(text2[text2.find('Cuarta Parte')-20:text2.find('Cuarta Parte')+20]))

table_regex = re.compile(r'Tabla de distribución:.*?\| Ignacio Tula \|.*?\|', re.DOTALL)
text3 = table_regex.sub("TABLE", text2)
print("After table sub:", repr(text3[text3.find('Cuarta Parte')-20:text3.find('Cuarta Parte')+20]))

def process_anexos(m): return m.group(0)
text4 = re.sub(r'\[([^\]]*?)\]\((capturas/.*?\.(?:txt|conf|html))\)', process_anexos, text3)
print("After anexos:", repr(text4[text4.find('Cuarta Parte')-20:text4.find('Cuarta Parte')+20]))
