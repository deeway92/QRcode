'''Importation des librairy '''
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pathlib
import os

'''Demande à l'utilisateur d'entrée les informations nécéssaire'''

demande_f1 = str(input("Choisissez un nom de fichier où les QRCODE seront sauvegardés : ") + "\\")
demande_n1 = str(input("Choisissez le nom du QRCODE pour l'extranet de supmeca: ")) + (".png")
path = ("C:\\Users\\bedanin\\Documents\\Projet\\") #On met le chemin où l'on veut créé et sauvegarder nos QRCODE     <------ A modifier en fonction de ton dossier
directory = demande_f1 # Attribution a une variable le nom de notre fichier
parent_dir = path #Attribution du chemin dans une variable 'parent_dir'
paths = os.path.join(parent_dir, directory) #Création d'une variable qui va combiner le chemin et le nom du fichie choisis par l'utilisateur
os.mkdir(paths) # Création du répertoire combiné
a = (paths + demande_n1) # Attribution à une variable 'a' le chemin plus le nom du QRCODE choisis par l'utilisateur


'''Création de la dimension du QRcode'''

qr = qrcode.QRCode(
    version =1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data('https://extranet.supmeca.fr/pages/accueil.aspx') # Ajout du lien 
qr.make(fit=True) # Création ) l'aide de .make
img = qr.make_image(fill_color="blue", back_color="white") # Choix couleur du QRcode et de son font
logo = Image.open(r"C:\Users\bedanin\Documents\Projet\Logo\supmeca.png") #Nom du logo que l'on veut ajouter  <-------------- A modifier en fonction du dossier des logos
logo.thumbnail((100,100)) #Dimension du logo


'''Calcule qui permet de placé le logo au millieu du QRcode'''

pos = ((img.size[0] - logo.size[0]) // 2,
       (img.size[1] - logo.size[1]) // 2)
img.paste(logo, pos) #Implémentation du logo et se sa postion dans le QRcode
img.save(a) #Sauvegarde du QRcode dans un fichier QRCODE


'''Permet de écire un text en haut du QR code une fois généré'''


img = Image.open(a) #Ouvre le QR code générer
draw = ImageDraw.Draw(img) #Permet d'écrire sur l'image choisis
font = ImageFont.truetype(r"C:\Users\bedanin\Documents\Projet\Basic_Light.ttf", 30) #Choisis la taille et la police souhaitée <----------- A modifier en fonction du dossier de la Police
draw.text((185,0),"EXTRANET ",(0,0,0), font=font) #Pemet de définir des 
img.save(a)


'''Demande à l'utilisateur d'entrée les informations nécéssaire'''


demande_n2 = str(input("Choisissez le nom du QRCODE pour la logisitique : ")) + (".png")
a = (paths + demande_n2) # Attribution à une variable 'a' le chemin plus le nom du QRCODE choisis par l'utilisateur

qr = qrcode.QRCode(
    version =1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data('http://logistique.supmeca.eu/ ')
qr.make(fit=True)
img = qr.make_image(fill_color="grey", back_color="white")
logo = Image.open(r"C:\Users\bedanin\Documents\Projet\Logo\glpilogs.jpg")
logo.thumbnail((100,100))
pos = ((img.size[0] - logo.size[0]) // 2,
       (img.size[1] - logo.size[1]) // 2)
img.paste(logo, pos)
img.save(a)

img = Image.open(a) #Ouvre le QR code générer
draw = ImageDraw.Draw(img) #Permet d'écrire sur l'image choisis
font = ImageFont.truetype(r"C:\Users\bedanin\Documents\Projet\Basic_Light.ttf", 30) #Choisis la taille et la police souhaitée
draw.text((140,0),"LOGISTIQUE ",(0,0,0), font=font) #Pemet de définir des 
img.save(a)


demande_n3 = str(input("Choisissez le nom du QRCODE pour le support : ")) + (".png")
a = (paths + demande_n3) # Attribution à une variable 'a' le chemin plus le nom du QRCODE choisis par l'utilisateur

qr = qrcode.QRCode(
    version =1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data('https://supportsi.supmeca.fr/index.php?noAUTO=1')
qr.make(fit=True)
img = qr.make_image(fill_color="grey", back_color="white")
img.save(a)

img = Image.open(a) #Ouvre le QR code générer
draw = ImageDraw.Draw(img) #Permet d'écrire sur l'image choisis
font = ImageFont.truetype(r"C:\Users\bedanin\Documents\Projet\Basic_Light.ttf", 30) #Choisis la taille et la police souhaitée
draw.text((140,0),"SUPPORT",(0,0,0), font=font) #Pemet de définir des 
img.save(a)

demande_n4 = str(input("Choisissez le nom du QRCODE pour la scolarité supméca : ")) + (".png")
a = (paths + demande_n4) # Attribution à une variable 'a' le chemin plus le nom du QRCODE choisis par l'utilisateur

qr = qrcode.QRCode(
    version =1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data('https://scolarite.supmeca.fr/faces/Login.xhtml')
qr.make(fit=True)
img = qr.make_image(fill_color="grey", back_color="white")
logo = Image.open(r"C:\Users\bedanin\Documents\Projet\Logo\scolarite.png")
logo.thumbnail((100,100))
pos = ((img.size[0] - logo.size[0]) // 2,
       (img.size[1] - logo.size[1]) // 2)
img.paste(logo, pos)
img.save(a)

img = Image.open(a) #Ouvre le QR code générer
draw = ImageDraw.Draw(img) #Permet d'écrire sur l'image choisis
font = ImageFont.truetype(r"C:\Users\bedanin\Documents\Projet\Basic_Light.ttf", 30) #Choisis la taille et la police souhaitée
draw.text((140,0),"SCOLARITE",(0,0,0), font=font) #Pemet de définir des 
img.save(a)

demande_n5 = str(input("Choisissez le nom du QRCODE pour moodle : ")) + (".png")
a = (paths + demande_n5) # Attribution à une variable 'a' le chemin plus le nom du QRCODE choisis par l'utilisateur

qr = qrcode.QRCode(
    version =1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data('https://moodle.supmeca.fr/login/index.php')
qr.make(fit=True)
img = qr.make_image(fill_color="grey", back_color="white")
logo = Image.open(r"C:\Users\bedanin\Documents\Projet\Logo\moodle.png")
logo.thumbnail((100,100))
pos = ((img.size[0] - logo.size[0]) // 2,
       (img.size[1] - logo.size[1]) // 2)
img.paste(logo, pos)
img.save(a)

img = Image.open(a) #Ouvre le QR code générer
draw = ImageDraw.Draw(img) #Permet d'écrire sur l'image choisis
font = ImageFont.truetype(r"C:\Users\bedanin\Documents\Projet\Basic_Light.ttf", 30) #Choisis la taille et la police souhaitée
draw.text((140,0),"SCOLARITE",(0,0,0), font=font) #Pemet de définir des 
img.save(a)
