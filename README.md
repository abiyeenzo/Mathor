# Mathor
Mathor est un interpréteur de calcul en Python, capable de gérer des opérations arithmétiques de base et de résoudre des équations à une seule inconnue. Il prend en charge les fichiers .mth pour automatiser la résolution d'expressions mathématiques. Développé par Æ Corp et fondé par Abiye Enzo.

## Fonctionnalités

- Résolution des opérations arithmétiques de base : addition, soustraction, multiplication, division.
- Résolution d'équations avec une seule inconnue.
- Lecture et interprétation des fichiers `.mth` pour traiter des expressions mathématiques.

## Installation

Clonez le dépôt GitHub et accédez au répertoire du projet :

```bash
git clone https://github.com/abiyeenzo/Mathor
cd Mathor
```

Assurez-vous d'avoir Python installé sur votre système. Si `sympy` n'est pas déjà installé, vous pouvez l'ajouter avec la commande suivante :

```bash
pip install sympy
```

## Utilisation

Pour utiliser Mathor en mode interactif, exécutez simplement le fichier `main.py` :

```bash
python3 main.py
```

Pour exécuter un fichier `.mth`, passez le nom du fichier en argument :

```bash
python3 main.py votre-fichier.mth
```

## Création d'un exécutable

Si vous souhaitez créer un fichier exécutable pour Mathor sur Linux, suivez ces étapes :

1. Installez PyInstaller :

```bash
pip install pyinstaller
```

2. Créez l'exécutable :

```bash
pyinstaller --onefile --name Mathor main.py
```

3. L'exécutable `Mathor` sera généré dans le dossier `dist`.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez contribuer, veuillez soumettre un pull request ou signaler des problèmes via la section "Issues" du dépôt.

## Licence

Ce projet est sous double licence MIT et GNU GPLv3. Vous pouvez choisir d'utiliser, de distribuer et de modifier le code sous l'une de ces licences.

## Crédits

Mathor est un projet développé par **Æ Corp.**, fondé par **Abiye Enzo**.
