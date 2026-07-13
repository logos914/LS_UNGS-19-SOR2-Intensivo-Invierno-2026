import re

text = """
## 3.4 Cuarta Parte: Configuración de Certificados y Seguridad en HTTPS

### 3.4.1 Habilitación de módulos de Apache para SSL
"""

def clean_heading(m):
    hashes = m.group(1)
    title = m.group(2)
    return f"{hashes} {title.strip()}"

print(re.sub(r'^(#+)\s+(?:SECCIÓN\s+\d+\s*[-—]\s*|\d+(?:\.\d+)*\s+)(.*)', clean_heading, text, flags=re.MULTILINE))
