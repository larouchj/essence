# Plein futé — app web de prix d'essence (Québec)

> Lu automatiquement par Claude Code. Répondre en **français québécois simple**, réponses courtes,
> schémas plutôt que longs textes. L'utilisateur (JF) est maker, pas développeur professionnel :
> code lisible, commenté en français.

## But
Savoir **sans chercher** où aller faire le plein : la station la plus proche, la moins chère dans un rayon,
et surtout **le meilleur choix** (économie nette, détour compris). Utilisé surtout sur iPhone (en auto),
ajouté à l'écran d'accueil. Région de JF : Estrie (Sherbrooke, Magog…).

## Architecture (un seul fichier, aucun serveur à nous)
- `index.html` : toute l'app (HTML + CSS + JS). `manifest.json` + `icone-*.png` : installation sur iPhone.
- `outils/icones.py` : regénère les icônes (Pillow).
- Hébergement prévu : **GitHub Pages** (dépôt public `larouchj/essence`, branche `main`, dossier racine).
  Le GPS exige https. Pas encore en ligne au 2026-11-26.
- Test local : `python3 -m http.server 8000` → http://localhost:8000 (localhost accepté pour le GPS).

## Sources de données (toutes publiques, sans clé, CORS ouvert)
| Quoi | URL | Notes |
|---|---|---|
| Prix | `https://regieessencequebec.ca/stations.geojson.gz` | Officiel, Régie de l'énergie. ~2 480 stations, regénéré aux 5 min. Champs : Name, brand, Address, Region, PostalCode, Status, Prices[{GasType: Régulier/Super/Diesel, Price: "166.4¢" ou null, IsAvailable}]. Pas d'heure par station, pas d'heures d'ouverture. Prix **déclarés par les stations** (La Presse a vu des écarts). |
| Distances/temps en auto | `https://router.project-osrm.org` (table + route) | Serveur **démo** : max 100 points par requête, pas pour usage commercial. Secours si en panne : vol d'oiseau × 1,3 marqué « ≈ ». |
| Adresses (destination) | `https://nominatim.openstreetmap.org/search` | Seulement si la destination n'est ni récente ni une ville du fichier. |
| Carte | Leaflet 1.9.4 (cdnjs) + tuiles `tile.openstreetmap.org` | CARTO abandonné (exige une clé). Mode sombre = filtre CSS. |

Le site tiers map.essencequebec.com (qui a motivé le projet) affiche les mêmes prix de la Régie ;
on ne l'utilise pas (son API interne exige un jeton).

## Fonctions (v3)
- **Autour de moi** (rayon 2/5/10/25/50 km **en auto**) ou **Sur ma route** (destination ; stations à < 2 km
  du tracé ; détour = moi→station→destination − moi→destination ; référence = station au plus petit détour).
- **Meilleur choix** : économie nette = (prix net réf. − prix net station) × litres − km en plus × L/100 km × prix.
  « Autour de moi » : réf. = la plus proche, km en plus × 2 (aller-retour).
- **Mes rabais** (¢/L par bannière) : défaut RBC 3 ¢ Petro-Canada, CIBC 3 ¢ Ultramar (Journie ; pas de
  Pioneer/Chevron au Québec dans le fichier). Le plus gros rabais applicable compte. Tout en prix net.
- **Bon prix ?** : prix net vs prix affiché moyen de la région (calculé sur le fichier).
- **Il me reste** Vide/¼/½/¾ × capacité réservoir (défaut 60 L) = litres à mettre. Consommation défaut 9 L/100 km.
- **Y aller** : app préférée (défaut **Waze** `https://waze.com/ul?ll=LAT%2CLON&navigate=yes`), + Apple Plans, Google.
- Exclure Costco (membres), position manuelle (ville) si GPS refusé.
- Réglages dans `localStorage` (clé `pleinfute`).

## Décisions de JF
- Pas de distances à vol d'oiseau : **distances réelles en auto**.
- Waze doit pouvoir être lancé directement (pas de plugin Waze possible : Waze n'en accepte pas).
- Pas une page Claude/artifact (pas de GPS ni de fetch externe possibles là).

## Idées pour plus tard (version App Store / Play Store, avec pub)
- Capacitor pour emballer l'app ; Apple refuse un simple site emballé → ajouter du natif (alertes de prix,
  widget, carte native). CarPlay / Android Auto ont une catégorie « essence ».
- Remplacer OSRM démo (serveur OSRM à soi ou API payante) et les tuiles OSM (Apple Maps / Google Maps SDK).
- **Vérifier les conditions d'utilisation des données de la Régie** pour un usage commercial (pas encore fait).
- AdMob ; Loi 25 + ATT d'Apple + politique de confidentialité.
- Serveur pour : alertes de baisse, historique, bouton « prix différent à la pompe », carnet de pleins.

## Prochaines étapes
1. Créer le dépôt GitHub public `essence`, pousser, activer Pages (`main` / root).
2. Tester sur l'iPhone de JF (GPS, Waze, écran d'accueil).
