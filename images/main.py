from cbir import rechercher_image
import os

# Exemple d'image requête
base_path = "coil-100"
image_test = os.path.join(base_path, "obj1__0.png")

# Recherche
resultats = rechercher_image(image_test, base_path, N=5)

# Affichage des résultats
print("Image\t\tDistance")
for nom, dist in resultats:
    print(f"{nom}\t{dist:.4f}")