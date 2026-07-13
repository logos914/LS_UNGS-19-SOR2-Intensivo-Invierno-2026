import re

with open('template_informe/main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Inject titlesec fix for subsubsection right before \begin{document}
fix = r'''
\usepackage{titlesec}
\titleformat{\subsubsection}{\color{black}\large\bfseries}{\thesubsubsection}{1em}{}
\titlespacing*{\subsubsection}{0pt}{10pt}{8pt}
'''

# Only inject if not already there
if r'\titleformat{\subsubsection}' not in text:
    text = text.replace(r'\begin{document}', fix + '\n' + r'\begin{document}')

    with open('template_informe/main.tex', 'w', encoding='utf-8') as f:
        f.write(text)
        print("Fixed main.tex")
