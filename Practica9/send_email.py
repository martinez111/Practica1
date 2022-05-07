import smtplib
import os
from ftplib import FTP, FTP_PORT, FTP_TLS, ftpcp
import ftplib
from typing import List
fromaddr = str(input("Ingresa tu correo electronico: "))
toaddrs  = str(input("Ingresa el correo electronico destinatario: "))
#msg = str(input("Introduce el mensaje a enviar"))
msg="En espera de una respuesta "
username = fromaddr
password = str(input("Ingresa tu contraseña super secreta: "))
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
#server.sendmail(fromaddr, toaddrs, msg)
#server.quit()
def connect_ftp(
    host: str, port: int = FTP_PORT, usr: str = "", pwd: str = "", save_path: str = ""
):  
    
    try:
        connection = FTP()
        connection.connect(host=host, port=port, timeout=3)
        connection.login(usr, pwd)
        msg="Coneccion Exitosa"
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

    except Exception as e:
        msg="Coneccion erronea"
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
if __name__ == "__main__":
    # http://www.ftp-sites.org/
    # connect_ftp('192.168.11.3', 8022)
    # connect_ftp(host="ftp.mirror.nl", save_path="/home/jhernandez/txt")
    connect_ftp(host="ftp.heanet.ie", save_path="/home/jhernandez/txt")