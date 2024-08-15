# XMLTV-Tools-Python
Outils développés en Python pour faciliter la manipulation et la gestion de fichiers **XMLTV** et **M3U8**.

**XMLTV** est un format standard pour la description des programmes télévisés, utilisé par de nombreux services de télévision et applications de gestion des programmes.
Un fichier de type **M3U8** représente une liste de lecture au format M3U, mais codée en UTF-8.

&nbsp;&nbsp;&nbsp;&nbsp;


## validate-m3u8.py
Script validant la forme d'un fichier m3u8. Il ne s'assure pas que les liens sont bons.

#### Fonctionnalités
- Valide le format d'un fichier m3u8 avec ces règles:
   - Ignore les lignes débutant  par la balise '#EXTREM:'
   - S'assure qu'il n'y a pas 2 lignes consécutives débutant par la balise '#EXTINF'
   - Vérifier la présence d'attributs obligatoires comme 'tvg-id', 'tvg-logo' et 'group-name'
   - Vérifier la présence de 'group-title'
   - Vérifier qu'il y a des valeurs pour les attributs 'tvg-id', 'tvg-logo' et 'group-name'
   - Vérifier qu'il y a toujours un titre pour la chaîne télé
- Produit un fichier 'validate-m3u8.py-err.txt' avec les avertissements sur chacune des lignes qui ne respectent pas les règles.

#### Exemple d'utilisation
```sh
python validate-m3u8.py "playlist.m3u8"
```
&nbsp;&nbsp;

## filter-epg.py
Script servant à filtrer et alléger un fichier XMLTV pour ne garder que les chaînes désirées.

#### Fonctionnalités
- Filtrage des chaînes spécifiées dans un fichier XMLTV.
- Création d'un fichier XMLTV allégé contenant uniquement les chaînes sélectionnées.

#### Exemple d'utilisation
```sh
python filter-epg.py "source.xml" "CNN.us|BBCNews.uk|BFMParis.fr" "destination.xml"
```
&nbsp;&nbsp;

## merge-epg.py
Script servant à joindre deux fichiers XMLTV en un fichier unique.

#### Fonctionnalités
- Fusion de deux fichiers XMLTV.
- Création d'un fichier XMLTV combiné.


#### Exemple d'utilisation
```sh
python merge-epg.py "guide1.xml" "guide2.xml" "guide12.xml"
```
&nbsp;&nbsp;

## pretty-epg.py
Script indentant et appliquant une mise en forme aux fichiers XMLTV pour une meilleure lisibilité.

#### Fonctionnalités
- Indentation.
- Mise en forme.


#### Exemples d'utilisation
```sh
python pretty-epg.py "guide.xml" "guide.xml"
python pretty-epg.py "guide.xml" "prettyguide.xml"
```
&nbsp;&nbsp;&nbsp;&nbsp;

## Prérequis
Assurez-vous d'avoir installé et être familiarisé avec **Python**.
