# Plein futé

Page web (installable sur l'écran d'accueil de l'iPhone) qui dit **où aller faire le plein** :
la station la plus proche, la moins chère dans un rayon choisi, et le **meilleur choix**
(économie nette, détour compris).

## Données
Fichier public de la Régie de l'énergie du Québec : `https://regieessencequebec.ca/stations.geojson.gz`
(≈ 2 500 stations, regénéré aux 5 minutes, accessible directement depuis un navigateur).
Aucun serveur à nous : la page télécharge le fichier et fait tous les calculs dans le téléphone.

## Distances réelles en auto
Calculées par le serveur public OSRM (`router.project-osrm.org`, données OpenStreetMap, sans clé) :
distance et temps de route vers jusqu'à 99 stations en une requête. Le trajet vers le meilleur choix
est tracé sur la carte. Si OSRM ne répond pas : vol d'oiseau × 1,3, affiché avec « ≈ ».

## Calcul du « meilleur choix »
économie nette = (prix de la plus proche − prix de la station) × litres
               − (km de route en plus × 2 (aller-retour) × L/100 km × prix)
Réglages (app de navigation, litres, consommation, Costco) gardés dans le téléphone.

## Navigation
Bouton « Y aller » : Waze (par défaut, `waze.com/ul?ll=…&navigate=yes`), Apple Plans ou Google Maps.
Carte : Leaflet + tuiles OpenStreetMap.

## Fichiers
- `index.html` — toute l'app (HTML + CSS + JavaScript commenté en français)
- `manifest.json`, `icone-*.png` — pour l'installer comme une app
- `outils/icones.py` — regénère les icônes (Pillow)

## Mise en ligne (GitHub Pages)
Le GPS exige une adresse **https** : GitHub Pages convient.
1. Pousser ce dossier dans un dépôt GitHub (ex. `essence`).
2. Settings → Pages → Source : « Deploy from a branch », branche `main`, dossier `/ (root)`.
3. Ouvrir `https://<utilisateur>.github.io/essence/` dans Safari → Partager → « Sur l'écran d'accueil ».

## Tester sur l'ordi
`python3 -m http.server 8000` puis http://localhost:8000 (localhost est accepté pour le GPS).
