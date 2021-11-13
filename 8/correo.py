import email, smtplib, ssl, getpass, imghdr, os
from email.message import EmailMessage

def enviarCorreo():
	remitente = "gersonreyes123444@gmail.com"
	asunto = input("Asunto del correo: ")
	cuerpo = input("Mensaje del correo: ")
	destinatario = input("Destinatario: ")
	contrasena = getpass.getpass("Contraseña:")

	mensaje = EmailMessage()
	mensajeaje["De"] = remitente
	mensaje["Para"] = destinatario
	mensaje["Asunto"] = asunto

	with smtplib.SMTP_SSL("marc_rc12@hotmail.com", 465) as server:
	    server.login(remitente, contrasena)
	    server.send_message(mensaje)
	print("Correo enviado con exito a: %s" % (destinatario))

if __name__ =='__main__':
    enviarCorreo()