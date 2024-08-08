@echo off
cls

:: Afficher un message d'accueil
echo.
echo Setup de jSelf
echo.

:: Créer le fichier .env avec les informations fournies
echo DISCORD_TOKEN=Ton Token > .env
echo COMMAND_PREFIX=Ton Prefix >> .env
echo AUTOJOIN_CHANNEL_ID= >> .env

:: Installer les dépendances depuis requirements.txt
pip install -r requirements.txt

echo.
echo Setup complet! Le fichier .env a été créé et les dépendances ont été installées.
pause
