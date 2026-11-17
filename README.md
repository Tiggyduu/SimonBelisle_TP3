# SimonBelisle_TP3

Travail pratique #3 (20%) - Animation aléatoire

OBJECTIF

Développer un outil Python pour Maya. Cet outil servira à créer une animation aléatoire sur les objets sélectionnés. L'objectif de ce travail est de réaliser un outil destiné aux animateurs travaillant dans l'industrie du jeu vidéo ou du cinéma.

CONSIGNES

● Implémenter l'outil en Python et utiliser PySide6 pour concevoir l'interface utilisateur.

● Implémenter les fonctionnalités suivantes :

    -> Créer une animation aléatoire s'appliquant uniquement aux objets sélectionnés.

    -> Permettre de configurer la durée de l'animation ainsi que le nombre d'images entre chaque clé d'animation.

    -> Pour chacun des paramètres de base (translation, rotation et échelle), permettre de définir les valeurs minimales et maximales pour chaque axe (X, Y, Z).

    -> Permettre de régénérer l'animation afin de créer une nouvelle variation.

    -> Prendre en charge la commande CTRL+Z (Undo).

● L'animation doit être seamless. Les clefs d'animation du début doivent être répété à la fin pour créer une boucle fluide

● Séparer le code en plusieurs fichiers afin d'alléger la structure du projet. Les fichiers suivants devront être présents :

    -> main.py : fichier de démarrage de l'outil.

    -> ui.py : définit l'interface utilisateur (à l'aide d'une classe).

    -> animator.py : génère l'animation à l'aide de maya.cmds.

REMISE

Le lien GitHub du projet devra être remis sur Moodle avant la date limite indiquée dans les consignes de remise. Une vidéo d'une animation réalisée à l'aide de votre outil sera également à remettre sur Moodle