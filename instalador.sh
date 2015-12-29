echo "Este es el instalador de WhatsappKILLER, pulsa INTRO para continuar"
echo "Asegurate de poder ejecutar comandos como super usuario, y de tener"
echo "el programa WhatsappKILLER.py en la misma carpeta"
read

echo "Instalando python2.7"
sudo apt-get install python2.7
echo "...Instalado"


echo "Instalando selenium"
sudo pip install selenium
echo "...Instalado"

echo "Ejecutando WhatsappKILLER"
python WhatsappKILLER.py