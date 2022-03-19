import base64
def codifi():
  menscod = str(input("Ingresa tu mensaje a codificar: "))
  byt = menscod.encode('ascii')
  bas64 = base64.b64encode(byt)
  mens64 = bas64.decode('ascii')
  print(mens64)
def decof():
  mensCif=str(input("Ingresa tu mensaje cifrado: "))
  bas64 = mensCif.encode('ascii')
  mensbt = base64.b64decode(bas64)
  menOrig = mensbt.decode('ascii')
  print(menOrig)
def codImagen ():
  rut=(str(input("Ingresa la ruta de la imagen a cifrar: ")))
  with open(rut, 'rb') as imgbin:
      Imdats =  imgbin.read()
      encod = base64.b64encode(Imdats)
      bas64 = encod.decode('utf-8')
      print(bas64)
    
def descodImg():
  img64 = str(input("Ingresa el valor de tu imagen cifrada: "))

  imgby = img64.encode('utf-8')
  nom=str(input("Ingresa el nombre a guardar tu imagen: "))
  nom=nom+".png"
  with open(nom, 'wb') as   guardado:
      dat = base64.decodebytes(imgby)
      guardado.write(dat)
print("Menu:\n1)Codificar Texto \n2)Decodificar texto codificado \n3)Codificar Imagen \n4)Decodificar Imagen")
val=int(input("R: "))
if (val==1):
  codifi()
elif (val==2):
  decof()
elif (val==3):
  codImagen ()
elif (val==4):
  descodImg()
else:
  print("Valor incorrecto, por favor verificalo y vuelve a correr el script")