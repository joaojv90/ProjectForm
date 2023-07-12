import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Iniciamos los parámetros del script
remitente = 'joao.jaramillo@gmail.com'
destinatarios = ['jojaramillo@itsqmet.edu.ec', 'mpaula_12@live.com', 'abrylmusic@hotmail.com', 'lyulan@itsqmet.edu.ec']
asunto = 'Reporte de Base de Datos'
cuerpo = 'Adjunto reporte con los registros de la Base de Datos'
ruta_adjunto = 'C:\\Users\\jpjar\\Documents\\Instituto\\5toSemestre\\Integracion_SI\\ConsultaPythonBD\\resultado_consulta.pdf'
nombre_adjunto = 'resultado_consulta.pdf'

# Creamos el objeto mensaje
mensaje = MIMEMultipart()

# Establecemos los atributos del mensaje
mensaje['From'] = remitente
mensaje['To'] = ", ".join(destinatarios)
mensaje['Subject'] = asunto

# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Abrimos el archivo que vamos a adjuntar
archivo_adjunto = open(ruta_adjunto, 'rb')

# Creamos un objeto MIME base
adjunto_MIME = MIMEBase('application', 'octet-stream')
# Y le cargamos el archivo adjunto
adjunto_MIME.set_payload((archivo_adjunto).read())
# Codificamos el objeto en BASE64
encoders.encode_base64(adjunto_MIME)
# Agregamos una cabecera al objeto
adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
# Y finalmente lo agregamos al mensaje
mensaje.attach(adjunto_MIME)

# Creamos la conexión con el servidor
sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)

# Ciframos la conexión
sesion_smtp.starttls()

# Iniciamos sesión en el servidor
sesion_smtp.login('joao.jaramillo@gmail.com','ickfyojynfmohwyr')

# Convertimos el objeto mensaje a texto
texto = mensaje.as_string()

# Enviamos el mensaje
sesion_smtp.sendmail(remitente, destinatarios, texto)

# Cerramos la conexión
sesion_smtp.quit()