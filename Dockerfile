# Utiliser une image de base Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le script Python dans le conteneur
COPY monitor_switch.py .

# Définir la commande par défaut pour exécuter le script Python
CMD ["python", "monitor_switch.py"]
