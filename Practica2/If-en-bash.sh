#!/bin/bash
edad=0
echo "Ingrese su edad: "
read edad
if [ $edad -ge 18 ];then
	echo "Eres mayor de edad"
else 
	echo "Eres menor de edad"
fi
sleep 5