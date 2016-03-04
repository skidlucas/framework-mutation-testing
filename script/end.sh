#! /bin/bash

#On insére notre .txt contenant le rapport dans notre .html
./python/dataHTML.py
#On termine le .html
./python/endHTML.py

#On supprime les fichiers temporaires
rm ./script/dependencies.txt ./script/plugins.txt ./script/selector.txt
rm ./python/report/data.txt
rm ./python/count.txt

echo -e "Exécution du framework terminée.\n"
echo -e "Si vous souhaitez consulter les logs de Maven, ils sont disponibles dans le dossier Maven Logs."
echo -e "Rapport créé, une fenetre de votre navigateur par défaut sera ouverte automatiquement.\n"
#On affiche ce rapport avec le browser par défaut
xdg-open ./python/report/rapMutant.html &