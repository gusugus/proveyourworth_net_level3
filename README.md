# proveyourworth_net_level3
https://www.proveyourworth.net/level3/img/thankyou.jpg

Script para pasar la pagina https://www.proveyourworth.net/level3/start y subir los documentos requeridos a la plataforma.
En el script se indican los pasos que se siguieron:
1. Se inicio entrando desde el navegador, y luego se analizò con el Inspector
2. El username es el statefulhash que esta en un input hidden
3. La sgte pagina te dice que debes hacer, y hay datos adicionales en la cabecera.
  3.1 Ir a ./payload que es donde hay una imagen, la cual le tienes q escribir tu nombre
    3.1.1 En el head de la pagina de payload dice los datos que se deben enviar y a q pagina
    3.1.2 Enviar lo requerido a /reaper con el statefulhash
 4. Una vez enviado, sale una pagina de agradecimiento ./thankyou
