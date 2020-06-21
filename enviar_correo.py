import smtplib

message = 'Hola, un mensaje desde Python!'
subject = 'Prueba de Correo'

message = 'Subject: {}\n\n{}'.format(subject, message)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('restrepojuanjo@gmail.com', 'Juanjito1234')

server.sendmail('restrepojuanjo@gmail.com', 'restrepojuanjo@gmail.com', message)

server.quit()
print("Correo enviando exitosamente!")