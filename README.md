# XMLTV-Tools-Python
Outils développés en Python pour faciliter la manipulation et la gestion de fichiers **XMLTV**.

XMLTV est un format standard pour la description des programmes télévisés, utilisé par de nombreux services de télévision et applications de gestion des programmes.

&nbsp;&nbsp;&nbsp;&nbsp;


## epg-filter.py
**epg-filter.py** sert à filtrer et alléger un fichier XMLTV pour ne garder que les chaînes désirées.

#### Fonctionnalités
- Filtrage des chaînes spécifiées dans un fichier XMLTV.
- Création d'un fichier XMLTV allégé contenant uniquement les chaînes sélectionnées.

#### Exemple d'utilisation
```sh
python epg-filter.py "source.xml" "CNN.us|BBCNews.uk|BFMParis.fr" "destination.xml"
```
&nbsp;&nbsp;

## epg-merge.py
**epg-merge.py** sert à joindre deux fichiers XMLTV en un fichier unique.

#### Fonctionnalités
- Fusion de deux fichiers XMLTV.
- Création d'un fichier XMLTV combiné.


#### Exemple d'utilisation
```sh
python epg-merge.py "guide1.xml" "guide2.xml" "guide12.xml"
```
&nbsp;&nbsp;

## epg-pretty.py
**epg-pretty.py** indente et applique une mise en forme aux fichiers XMLTV pour une meilleure lisibilité.

#### Fonctionnalités
- Indentation.
- Mise en forme.


#### Exemples d'utilisation
```sh
python epg-pretty.py "guide.xml" "guide.xml"
python epg-pretty.py "guide.xml" "prettyguide.xml"
```
&nbsp;&nbsp;&nbsp;&nbsp;

## Prérequis
Assurez-vous d'avoir installé et être familiarisé avec **Python**.
