import smtplib
from email.mime.text import MIMEText

correo_origen = '**************'
contraseña = '*************'
correo_destino = '*************'


msg = MIMEText("Hola a todos estamos en el modulo 4 del curso de IOT enviando email con Raspberry Pi")
msg['Subject'] = 'Curso de IOT'
msg['From'] = correo_origen
msg['To'] = correo_destino

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(correo_origen,contraseña)
server.sendmail(correo_origen,correo_destino,msg.as_string())

print("Su Email ha sido enviado.")

server.quit()
