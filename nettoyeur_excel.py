import pandas as pd

def nettoyer_excel(fichier_entree, fichier_sortie):
    # Lire le fichier
    df = pd.read_excel(fichier_entree)
    
    # Supprimer les doublons
    df = df.drop_duplicates()
    
    # Supprimer les lignes vides
    df = df.dropna()
    
    # Sauvegarder
    df.to_excel(fichier_sortie, index=False)
    print(f"Fichier nettoyé : {fichier_sortie}")

# Exemple d'utilisation
nettoyer_excel("donnees_sales.xlsx", "donnees_propres.xlsx")