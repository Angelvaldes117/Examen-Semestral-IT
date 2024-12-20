Proyecto Semestral: Gestion de Reservas con Flask
Este proyecto consiste en crear una aplicación web para la gestión de reservas en una sala de eventos, la cual permita 
a los clientes realizar operaciones de creación, lectura, actualización y eliminación (CRUD) sobre sus reservas.
Pasos: 

crear antes su entorno virtual que se debe llamar env 
python3 -m venv env

siempre activar el entorno virtual para crear todo y instalar todo
una vez creado el entorno virtual importante descargar todas sus dependencias

pip install -r requirements.txt

comandos si sale que el puerto esta en uso 
lsof -i :5000

kill -9

y volver a poner
lsof -i :5000

**configurar el gcloud
instalar 

sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates gnupg curl
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
 sudo apt-get update && sudo apt-get install google-cloud-cli

**pasos para verificar que se intalo el gcloud
gcloud init
which gcloud

**añade el id del proyecto en el firebase
gcloud auth application-default login --no-launch-browser
gcloud auth application-default set-quota-project proyecto-441322
gcloud config set project proyecto-441322
gcloud auth login --no-launch-browser

**verificamos que este el proyecto
gcloud config list


**pasos para activar el flask
export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=developments

flask run


Instalar Nginx:

sudo apt update
sudo apt install nginx

Iniciar y habilitar Nginx:

sudo systemctl start nginx
sudo systemctl enable nginx

Configurar un servidor virtual:

Abre el archivo de configuración:
sudo nano /etc/nginx/sites-available/default

Añade la configuración básica:
server {
    listen 80;
    server_name tu_dominio.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

Probar la configuración:
sudo nginx -t

Reiniciar Nginx para aplicar los cambios:
sudo systemctl restart nginx

Solución de Problemas Comunes
Nginx no se inicia:

Verifica el estado del servicio:
sudo systemctl status nginx

Revisa los logs de errores:
sudo tail -f /var/log/nginx/error.log

Errores de configuración:
Si nginx -t muestra errores, revisa y corrige la configuración en /etc/nginx/nginx.conf o en los archivos de configuración de los sitios en /etc/nginx/sites-available/.
Problemas de permisos:

Asegúrate de que Nginx tenga los permisos adecuados para acceder a los archivos y directorios necesarios:
sudo chown -R www-data:www-data /var/www/HTML

Problemas de redirección:

Si tienes problemas con redirecciones, asegúrate de que las reglas de redirección estén correctamente configuradas en el bloque server o location.
Comandos Adicionales Útiles

Recargar la configuración sin reiniciar:
sudo systemctl reload nginx

Verificar la versión de Nginx:
nginx -v

Detener Nginx:
sudo systemctl stop nginx

Deshabilitar Nginx:
sudo systemctl disable nginx
