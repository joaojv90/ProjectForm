import mysql.connector as mariadb
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
import time
import subprocess

# Establecer conexión con la base de datos
mariadb_conexion = mariadb.connect(
    host='localhost', 
    port='3309',
    user='root', 
    password='Sup3r', 
    database='blog')

# Crear el cursor y ejecutar la consulta
cursor = mariadb_conexion.cursor()
try:
    cursor.execute("SELECT * FROM blog")
    resultados = cursor.fetchall()
except mariadb.Error as error:
    print("Error: {}".format(error))

# Cerrar la conexión con la base de datos
mariadb_conexion.close()

# Definir estilos de párrafo
styles = getSampleStyleSheet()
style_normal = styles["Normal"]
style_bold = ParagraphStyle(name="Bold", parent=styles["Normal"], fontName="Helvetica-Bold")
style_heading = styles["Heading1"]

# Crear lista de elementos para agregar al PDF
content = []

# Agregar encabezado
heading = Paragraph("Resultado de la consulta", style_heading)
content.append(heading)
content.append(Paragraph("<br/>", style_normal))  # Espacio en blanco

# Crear el archivo PDF y escribir los resultados de la consulta
pdf_filename = "resultado_consulta.pdf"
pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)

data = [["ID", "Blog Id", "Título", "Nombre del autor", "Fecha de Inicio", "Fecha de Fin"]]  # Cabecera de la tabla

for fila in resultados:
    data.append(fila)  # Agregar cada fila de resultados

table = Table(data)

# Establecer estilos de la tabla
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Color de fondo de la cabecera
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Color de texto de la cabecera
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinear al centro todas las celdas
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fuente y estilo de la cabecera
    ('FONTSIZE', (0, 0), (-1, 0), 12),  # Tamaño de fuente de la cabecera
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espacio inferior de la cabecera
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Color de fondo del contenido
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Líneas de la cuadrícula
])

table.setStyle(style)

# Agregar la tabla a la lista de elementos
content.append(table)

# Generar el PDF con la lista de elementos
pdf.build(content)

print("PDF creado exitosamente.")

time.sleep(5)
subprocess.call(["python", "C:/Users/jpjar/Documents/Instituto/5toSemestre/Integracion_SI/ConsultaPythonBD/attach.py"])

