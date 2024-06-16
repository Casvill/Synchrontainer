# imagen base
FROM python:3

# establece el directorio de trabajo
WORKDIR /usr/src/app

# Copiar la carpeta myapp a /usr/src/app
COPY ./myapp/ .

# Copiar la carpeta sync_files
COPY ./sync_files ./sync_files

# instalación de requerimientos y dependencias
RUN pip3 install -r requirements.txt

# Copiar los scripts generate_file.py y generate_file_private.py
COPY ./generate_file.py .
COPY ./generate_file_private.py .

# Crear directorios public y private
#RUN mkdir -p /usr/src/app/sync_files/public
#RUN mkdir -p /usr/src/app/sync_files/private

# Apertura el puerto 5000 del contenedor
EXPOSE 5000

# Ejecutar los scripts generate_file.py y generate_file_private.py en segundo plano y luego iniciar Flask
CMD ["sh", "-c", "CONTAINER_NAME=$(hostname) python3 ./generate_file.py & python3 ./generate_file_private.py & python3 ./app.py"]