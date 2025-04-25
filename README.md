# Indexation_Contenu_Multim-dia
# 📄🔍 Système d'Indexation de Documents par SIFT + dHash

Ce projet présente une application permettant de rechercher automatiquement un document à partir d’une vidéo contenant une portion de texte de ce document(image).  
L’approche repose sur la combinaison des descripteurs SIFT (pour la robustesse aux transformations) et d’un hachage perceptuel (dHash) pour un filtrage rapide.

## 🎯 Objectif
Ce système permet de :
- Extraire une frame d’une vidéo contenant un document.
- Identifier automatiquement le document correspondant dans une base d’images.
- Localiser précisément la zone du texte détecté dans l’image reconnue.

## 🧠 Technologies utilisées

- **Python** : Comme  langage de programmation pour coder le système.
- **OpenCV** : pour le traitement d’images et l’extraction des keypoints/descripteurs SIFT.
- **dHash (difference hashing)** : pour l’indexation rapide des images par similarité visuelle.
- **Streamlit** : pour une interface web interactive, simple et efficace.
- **Matplotlib, NumPy, PIL** : pour la visualisation et manipulation d’images.

## 🛠️ Fonctionnalités principales

1. **Téléversement d’une vidéo de requête** (.mp4)
2. **Extraction automatique de la frame centrale**
3. **Calcul du hash dHash de la frame et affichage des keypoints SIFT**
4. **Filtrage des 30 images les plus proches via comparaison des hash**
5. **Matching SIFT entre la frame et les 30 images filtrées**
6. **Identification du meilleur document par nombre de bons matchs**
7. **Localisation de la zone de texte dans l’image via estimation d’homographie**
8. **Affichage des résultats avec les hash et visualisation encadrée**


## ⚙️ Structure des données


```bash
indexation-sift-dhash/
├── images/              # Base d'images (documents)
├── requetes/            # Vidéos de test .mp4
├── captures/            # Captures d'écran pour README
├── TpIndexation_Groupe3.py   # Code Streamlit principal
├── requirements.txt
└── README.md
```


## ⚙️ Installation et exécution

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/votre_utilisateur/indexation-sift-dhash.git
cd indexation-sift-dhash
```

### 2️⃣ Créer un environnement virtuel (recommandé)
```bash
python -m venv env
```
# Pour Windows
```bash
env\Scripts\activate
```
# Pour Linux/macOS
```bash
source env/bin/activate
```
### 3️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```
### 4️⃣ Lancer l'application sur Streamlit
```bash
streamlit run TpIndexation_Groupe3.py
```

## 🔍 Exemple d’utilisation

![Frame extraite](./images/frame_extrait.png)
*Frame extraite de la vidéo avec détection SIFT*

![Document reconnu](./images/document_reconnu.png)
*Document correspondant reconnu*

![Localisation du texte](./images/zone_localisee.png)
*Zone de texte localisée dans l’image document*


🧪 Auteurs
👨‍💻 LUTALA LUSHULI David, davidlutala0@gmail.com

👨‍💻 NZAZI NGABILA Boaz, nzaziboaz@gmail.com
