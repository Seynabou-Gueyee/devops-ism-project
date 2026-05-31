# Utilise une version légère de Python
FROM python:3.9-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Installe les dépendances nécessaires
RUN pip install flask

# Copie ton code actuel dans le conteneur
COPY app.py .

# Expose le port 5000 pour que le site soit accessible
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python3", "app.py"]
