import requests
import re
from PIL import Image, ImageDraw
from os import getcwd
from pathlib import Path

str_url_padre = "https://www.proveyourworth.net/level3"
ruta_actual = getcwd()
directorio = Path(ruta_actual.replace("\\","/"))

#Comenzamos con una sesion
with requests.session() as s:
    str_url_start = str_url_padre+"/start"
    #Entramos a la pagina y extraemos el "password"
    req_start = s.get(str_url_start)
    #print(req_start.text) #Observamos la pagina
    str_html_page = req_start.text
    obj_res = re.search('"statefulhash" value="(.*)" />',str_html_page) #Extraemos la cadena que hay que enviar
    str_password = obj_res.group(1)
    #print("*"+str_password+"*")

    str_url_activate = str_url_padre+"/activate"
    data = {
        'statefulhash':str_password,
        'username':str_password
    }
    req_activate = s.post(str_url_activate, data)
    #print(req_activate.text)
    #Vemos que en la pagina nos da una referencia a la url: href="https://addons.mozilla.org/en-US/firefox/addon/3829"
    #La buscamos y no existe en este momento. Buscamos en google y encontramos que se la addon es Live HTTP Header
    #Comenzamos a ver los headers, a ver que encontramos
    #print(req_activate.headers)
    #vemos que en el header de activate hay una referencia a otra url
    #'X-Payload-URL': 'http://www.proveyourworth.net/level3/payload', el cual es una foto (cambia al azar*)
    str_url_payload=str_url_padre+"/payload"
    req_payload=s.get(str_url_payload)
    #print(req_payload.text) #Verificamos la pagina, y es una foto...
    print(req_payload.headers) #En este header nos dice donde enviar el resume
    str_url_reaper=str_url_padre+"/reaper"
    #req_reaper=s.get(str_url_reaper)
    #print(req_reaper) #solo responde con response 200....
    
    #Las instrucciones son 
    '''
    Download the payload. Sign it with your name. (and the hash for extra credit)
    Upload the modified image, your code, and your resume.
    Do it all with code. Curl, Snoopy, Pear, Sockets... all good. Good luck.
    '''
    #Escribimos el nombre y el hash en la imagen
    obj_img_raw = s.get(str_url_payload, stream=True).raw
    obj_imagen = Image.open(obj_img_raw)
    obj_img_tmp = ImageDraw.Draw(obj_imagen)
    str_incrustacion = "Gustavo Narea. Hash: {str_password}".format(str_password=str_password)
    obj_img_tmp.text((0,0),str_incrustacion)
    obj_imagen.save('imagen.jpg','JPEG')
    
    #Creamos los datos que desean recibir en el reaper
    dic_datos = {
        "email":"nareagustavo@yahoo.com",
        "name":"Gustavo Narea",
        "aboutme": "Soy un desarrollador backend, mas de mi trabajo es en php y java. Suelo usar python para hacer scripts y resolver problemas mas rapido en el trabajo."
    }
    
    dic_archivos = {
        "code":open(directorio / "resolucion_proveyourworth.py","rb"),
        "resume":open(directorio / "resume_gustavo_narea.pdf","rb"),
        "image":open(directorio / "imagen.jpg","rb")
    }
    #Enviamos los datos y los archivos al reaper
    print("Enviando archivo a {url}".format(url=str_url_reaper))
    req_reaper=s.post(str_url_reaper, data=dic_datos, files=dic_archivos)
    print(req_reaper.text)
    #La pagina retorna una imagen. https://www.proveyourworth.net/level3/img/thankyou.jpg
print("Finalizamos el script.")
