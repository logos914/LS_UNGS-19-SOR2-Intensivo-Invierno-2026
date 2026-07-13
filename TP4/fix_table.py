with open('template_informe/readme_stripped.md', 'r') as f:
    text = f.read()

text = text.replace('Tabla de distribución:\n| Integrante', 'Tabla de distribución:\n\n| Integrante')
with open('template_informe/readme_stripped.md', 'w') as f:
    f.write(text)
