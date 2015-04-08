*************************
Présentation: "cx_Freeze"
*************************

"cx_Freeze" est un paquet python qui permet de distribuer facilement de son programme.
Il a les avantages suivante :

    Portabilité : "cx_Freeze" est fait pour fonctionner aussi bien sur Windows que sur Linux ou Mac OS ;

    Compatibilité : "cx_Freeze" fonctionne sur des projets Python de la branche 2.X ou 3.X ;

    Simplicité : créer son programme standalone avec "cx_Freeze" est simple et rapide ;

    Souplesse : vous pouvez aisément personnaliser votre programme standalone avant de le construire.


*******************************************
Comment installer "cx_Freeze" sous Ubuntu ?
*******************************************

On l'installe avec la commande suivante :

$ sudo apt-get install cx-freeze



************************************
Exemple d'utilisation de "cx_Freeze"
************************************

Methode 1 : directement avec la commande "cxfreeze"

$ cxfreeze programme.py

Où "programme.py" est le fichier python contenant notre programme à distribuer.
En executant la commande ci-dessous, si tout se passe bien, vous vous retrouvez avec un sous-dossier "dist" 
qui contient les bibliothèques dont votre programme a besoin pour s'exécuter… et votre programme lui-même

Methode 2 : via un script "setup.py"

$ python setup.py build

Où "setup.py" est un script python faisant appel à notre programme "programme.py".

======================Contenu de setup.py=======================

# -*-coding:Utf-8 -*

"""Fichier d'installation de notre script programme.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "programme",
    version = "0.1",
    description = " ",
    executables = [Executable("programme.py")],
)
================================================================

Une fois avoir lancer la commande "$ python setup.py build", vous aurez dans votre dossier un sous-répertoire build.
Ce répertoire contient un autre sous-répertoire contenant les bibliothèques dont votre programme a besoin pour 
s'exécuter… et votre programme lui-même.


************
Conclusion :
************

L'exécutable que vous trouvez dans les sous-dossiers "dist" et "build" n'ont pas besoin de Python pour s'exécuter : 
il contient lui-même l'interpréteur Python.
Vous pouvez donc distribuer ce programme à vos amis ou le mettre en téléchargement sur votre site, si vous le désirez.
Une chose importante à noter, cependant : veillez à copier, en même temps que votre programme, tout ce qui se trouve
dans le dossier "dist" ou "build". Sans quoi, votre exécutable pourrait ne pas se lancer convenablement.

En résumé :

    cx_Freeze est un outil permettant de créer des programmes Python standalone.

    Un programme standalone signifie qu'il contient lui-même les dépendances dont il peut avoir besoin, ce qui rend sa
    distribution plus simple.

    cx_Freeze installe un script qui permet de créer nos programmes standalone très rapidement.

    On peut arriver à un résultat analogue en créant un fichier appelé traditionnellement setup.py.


