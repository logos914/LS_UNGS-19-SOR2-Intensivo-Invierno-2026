import re
import os

with open('readme.MD', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Strip top metadata
idx = text.find('# Índice')
if idx != -1:
    text = text[idx:]

# Remove @todo
text = text.replace('@todo', '')

# 2. Fix headings (remove explicit numbering)
def clean_heading(m):
    hashes = m.group(1)
    title = m.group(2).strip()
    res = f"{hashes} {title}"
    # Si es un título de nivel 1 y no es la "Introducción", forzamos un \newpage
    if len(hashes) == 1 and "Introducci" not in title:
        return f"\\newpage\n\n{res}"
    return res

text = re.sub(r'^(#+)\s+(?:SECCIÓN\s+\d+\s*[-—]\s*|\d+(?:\.\d+)*\s+)(.*)', clean_heading, text, flags=re.MULTILINE)

# 3. Replace the entire table with a clean LaTeX longtable
table_regex = re.compile(r'Tabla de distribución:.*?\| Ignacio Tula \|.*?\|', re.DOTALL)

latex_table = r'''
Tabla de distribución:

\begin{longtable}{p{3.5cm} p{11.5cm}}
\toprule
\textbf{Integrante} & \textbf{Tarea a Cargo} \\
\midrule
\endfirsthead
\toprule
\textbf{Integrante} & \textbf{Tarea a Cargo} \\
\midrule
\endhead
\bottomrule
\endfoot
\bottomrule
\endlastfoot

David Cañete &
\vspace{-0.3cm}
\begin{itemize}[leftmargin=*, noitemsep, topsep=0pt]
    \item Configuración inicial del entorno y redacción de Secciones 1 y 2.
    \item Instalación de pila LAMP, configuración de Virtual Hosts y MySQL (Sec. 3.1 y 3.2).
    \item Despliegue del CMS WordPress (Sec. 3.3).
    \item Configuración del cliente web (Firefox) para autenticación PKCS12 (Sec 4.5).
    \item Consolidación del informe final y revisión de formato.
\end{itemize} \\
\midrule

Ignacio Tula &
\vspace{-0.3cm}
\begin{itemize}[leftmargin=*, noitemsep, topsep=0pt]
    \item Configuración de HTTPS, cifrado y módulos de seguridad en Apache (Sec. 3.4).
    \item Creación y gestión de la Autoridad Certificadora (CA) local (Sec 4.1 y 4.2).
    \item Generación y firma de CSR para autenticación asimétrica (Sec 4.3 y 4.4).
    \item Gestión de Listas de Revocación (CRL) y endurecimiento del servidor (Sec 4.6).
    \item Revisión técnica cruzada de comandos y logs del sistema.
\end{itemize} \\
\end{longtable}
'''

text = table_regex.sub(lambda m: latex_table, text)

# Sanitize unicode drawing chars from logs
text = text.replace('●', '*')
text = text.replace('├', '+')
text = text.replace('─', '-')
text = text.replace('└', '+')
text = text.replace('│', '|')

# 4. Handle Anexos
anexos = []
anexo_counter = 1

def process_anexos(m):
    global anexo_counter
    link_text = m.group(1)
    file_path = m.group(2)
    
    full_path = file_path # relative to current dir
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        anexos.append((anexo_counter, file_path, link_text, content))
        res = f"**Anexo {anexo_counter}** ({link_text})"
        anexo_counter += 1
        return res
    except Exception as e:
        print(f"File not found: {full_path} - Error: {e}")
        return m.group(0)

# Links look like [text](capturas/.../*.txt)
text = re.sub(r'\[([^\]]*?)\]\((capturas/.*?\.(?:txt|conf|html))\)', process_anexos, text)

# 5. Append Anexos section if there are any
if anexos:
    text += "\n\n\\newpage\n# Anexos\n\n"
    for num, path, link_text, content in anexos:
        text += f"## Anexo {num}: {os.path.basename(path)}\n\n"
        text += f"*(Referenciado desde: {link_text})*\n\n"
        text += "```text\n"
        text += content
        text += "\n```\n\n"

with open('template_informe/readme_stripped.md', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Processed markdown. Extracted {len(anexos)} anexos.")
