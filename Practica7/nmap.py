import socket, base64, os, nmap
ip=(socket.gethostbyname(socket.gethostname()))
print("Tu IP local es: \n",ip)
print("Tu IP publica es:")
os.system("curl ifconfig.me")
print("\n \nNmap")

target = input(("Ingresa tu direccion IP: "))
empieza=int(input("Ingresa desde que puerto quieres iniciar a escanear: "))
termina=int(input("Ingresa hasta que puerto vas a escanear: "))
scanner = nmap.PortScanner() 
for i in range(empieza,termina+1): 
    res = scanner.scan(target,str(i)) 
    res = res['scan'][target]['tcp'][i]['state'] 
    print(f'port {i} is {res}.') 