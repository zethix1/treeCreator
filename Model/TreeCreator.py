from pathlib import Path

class TreeCreator():
    
    def build_path_from_home(self, path_parts: list) -> Path:
        """construit le chemin de dossier a partir du dossier utilisateur

        Args:
            path_parts (list): tableau de sous dossiers

        Returns:
            Path: chemin complet construit a partir du dossier utilisateur et des sous dossiers
        """        
        return Path.home().joinpath(*path_parts)
    
    def folder_init(self, folder_path: Path) -> bool:  
        """Vérifie si le dossier existe, sinon le crée

        Args:
            folder_path (Path) : Chemin du dossier a vérifier

        Returns:
            bool: Vraie si le dossier existe ou a été initialisé sinon retourne faux si le dossier n'existe pas et n'a pas pu etre initialisé
        """      
        try:
            if not folder_path.exists():
                folder_path.mkdir(parents=True, exist_ok=True)
            return True
        except Exception:
            return False

    def is_valid_folder_name(self, folder_name: str) -> bool:
        """valide le nom d'un dossier

        Args:
            folder_name (str): nom du dossier a valider

        Returns:
            bool: renvoie vraie si le dossier ne contient aucun des caractères interdit ou n'est pas vide
        """        
        # Liste des caractères interdits dans les noms de dossiers
        invalid_chars = ['\\', ':', '*', '?', '"', '<', '>', '|']
        # Vérifier si le nom contient un des caractères interdits
        if any(char in folder_name for char in invalid_chars):
            return False
        # Vérifier que le chemin n'est pas vide ou constitué uniquement d'espaces
        if folder_name.strip() == "":
            return False
        return True

    def start_terminal_interface(self):
        """Ouvre un terminal et permet à l'utilisateur de saisir un chemin de dossier.
        """        
        print("Bienvenue dans l'interface de création de dossiers.")
        print("Entrez un chemin de dossier (par exemple: Documents/jeux) ou tapez 'exit' pour quitter.")
        
        while True:
            user_input = input("Chemin du dossier: ").strip()
            
            if user_input.lower() == "exit":
                print("Fermeture de l'interface.")
                break

            # Vérifier si le chemin contient des caractères interdits ou est vide
            if not self.is_valid_folder_name(user_input):
                print(f"Erreur : Le chemin '{user_input}' contient des caractères interdits ou est vide.")
                print("Caractères interdits : \\ : * ? \" < > |")
                continue
            
            # Convertir l'entrée en chemin relatif à partir de Path.home()
            folder_path = self.build_path_from_home(user_input.split("/"))
            
            # Appeler la fonction folder_init pour vérifier ou créer le dossier
            if self.folder_init(folder_path):
                print(f"Dossier '{folder_path}' vérifié ou créé avec succès.")
            else:
                print(f"Erreur lors de la création ou de la vérification du dossier '{folder_path}'.")

    def on_created(self):
        """Méthode appelée lors du démarrage pour créer les dossiers par défaut et lancer l'interface terminal."""
        # création des dossiers principaux
        self.folder_init(self.build_path_from_home(["Documents", "jeux"])) # exemple de dossier le chemin serait donc /Users/nomUtilisateur/Documents/jeux
        
        # Lancement de l'interface terminal pour les chemins personnalisés
        self.start_terminal_interface()
        