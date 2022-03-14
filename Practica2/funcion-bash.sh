#!/bin/bash
echo "Escribe 3 nombres a saludar"
function saludar {
	echo "Hola $1"
	echo "Hola $2"
	echo "Hola $3"
}
read par per pir
saludar $par $per $pir
sleep 5