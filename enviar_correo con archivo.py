from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

mensaje = MIMEMultipart("plain")
mensaje["From"]="restrepojuanjo@gmail.com"
mensaje["To"]="restrepojuanjo@gmail.com"
mensaje["Subject"]="Hey Juanjo"

adjunto = MIMEBase("application", "octect-stream")
adjunto.set_payload(open("hola.txt", "rb").read())
adjunto.add_header("content-Disposition", 'attachment; filename="mensaje.txt"')
mensaje.attach(adjunto)
smtp = SMTP("smtp.gmail.com")
smtp.starttls()
smtp.login("restrepojuanjo@gmail.com", "Juanjito1234")
smtp.sendmail("restrepojuanjo@gmail.com","restrepojuanjo@gmail.com", mensaje.as_string())
print("Correo Enviado Exitosamente")
smtp.quit()
