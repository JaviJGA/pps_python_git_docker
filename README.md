# pps_python_git_docker

App para sacar frases motivadoras aleatorias al estilo madre cuarentona

## Requisitos

# Primero, crea la red y levanta la base de datos:

docker network create red-bayeta
docker run -d --name mi-mongo --network red-bayeta mongo:latest

# Para buildear

docker build -t thehell:0.0.4 .

# Ejecutar el docker

docker run -p 5000:5000 --network red-bayeta thehell:0.0.4
---

## 5. Docker y Git (Pasos 11, 13, 14, 15)

Ahora que el código y la documentación están listos, reconstruye la imagen y pruébala:

# Construye la nueva imagen (el Dockerfile copiará el nuevo requirements.txt)
docker build -t thehell:0.0.4 .

# Ejecútala conectada a la red
docker run -p 5000:5000 --network red-bayeta thehell:0.0.4
