import subprocess

def git_commit_and_push(commit_message):
    try:
        # Aggiungi tutti i file modificati
        subprocess.run(["git", "add", "."], check=True)
        
        # Crea il commit con il messaggio fornito
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Esegui il push sul repository remoto
        subprocess.run(["git", "push"], check=True)
        
        print("Commit e push eseguiti con successo.")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del comando git: {e}")

        import subprocess

def git_pull(branch_name):
    try:
        # Esegui il pull dal branch specificato
        subprocess.run(["git", "pull", "origin", branch_name], check=True)
        print(f"Pull del branch '{branch_name}' eseguito con successo.")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante il pull del branch: {e}")