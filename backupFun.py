import os
import shutil
from datetime import datetime

def create_backup(source_dir, destination_dir):
    # Ottenere la data e l'ora corrente in formato stringa
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Creare la directory di backup nel livello superiore
    backup_dir = os.path.join(destination_dir, f"{current_time}")
    os.makedirs(backup_dir, exist_ok=True)
    
    # Copiare i file .txt dalla directory di origine alla directory di backup
    for file_name in os.listdir(source_dir):
        if file_name.endswith(".txt"):
            full_file_name = os.path.join(source_dir, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, backup_dir)
    
    print(f"Backup completato: {backup_dir}")