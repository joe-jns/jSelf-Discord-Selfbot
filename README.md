# jSelf - Votre Selfbot Discord Personnel

Bienvenue sur **jSelf**, votre selfbot Discord personnel. Suivez les instructions ci-dessous pour configurer et exécuter le bot sur votre machine.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Python 3.6+
- pip (installateur de paquets Python)

## Instructions d'installation

### Étape 1 : Exécuter le Script de Configuration

Pour commencer, exécutez le script `setup.bat`. Cela créera un fichier `.env` et installera toutes les dépendances nécessaires.

```bash
setup.bat
```

### Étape 2 : Configurer le Fichier .env

Après avoir exécuté le script de configuration, configurez le fichier `.env` avec votre token de compte Discord et le préfixe de commande préféré. Vous pouvez trouver le fichier `.env` dans le répertoire racine du projet.

```plaintext
DISCORD_TOKEN=Votre_Token
COMMAND_PREFIX=Votre_Préfixe
AUTOJOIN_CHANNEL_ID=ID_De_Votre_Channel_Autojoin (optionel)
```

- `DISCORD_TOKEN` : Votre token de compte Discord. **Important : Il s'agit de votre token personnel et non d'un token de bot.**
- `COMMAND_PREFIX` : Le préfixe que vous souhaitez utiliser pour les commandes de votre bot.
- `AUTOJOIN_CHANNEL_ID` : L'ID du canal vocal que vous souhaitez que le bot rejoigne automatiquement au démarrage (optionnel).

### Étape 3 : Exécuter le Bot

Une fois que vous avez configuré le fichier `.env`, vous pouvez démarrer le bot en exécutant la commande suivante dans votre terminal :

```bash
python main.py
```

## Fonctionnalités

### Commandes Disponibles

- **Commandes Utilitaires :**
  - `ping` : Affiche la latence du bot.
  - `prefix` : Change le préfixe de commande pour le serveur et met à jour le fichier `.env`.
  - `adminservers` : Liste les serveurs où vous avez des permissions administratives et le nombre de membres.

- **Commandes Vocales :**
  - `joinvc` : Rejoint un canal vocal spécifié par son ID.
  - `leavevc` : Quitte le canal vocal actuel.
  - `autojoin` : Définit un canal vocal que le bot doit rejoindre automatiquement au démarrage.

- **Commandes Rich Presence (RPC) :**
  - `setrpc` : Définit le RPC du bot.
    - Utilisation : `setrpc playing <nom_du_jeu>` ou `setrpc streaming <nom_du_stream>`
  - `listrpc` : Affiche la liste des types de RPC disponibles.
    - Utilisation : `listrpc`
  - `remrpc` : Supprime le RPC actuel.
    - Utilisation : `remrpc`

## Contributions

N'hésitez pas à forker ce dépôt et à apporter vos propres modifications. Si vous avez des suggestions ou si vous trouvez des problèmes, veuillez ouvrir une issue sur le [dépôt GitHub](https://github.com/JnsJoe/jSelf).

---

Merci d'utiliser **jSelf**. Profitez de votre expérience Discord améliorée !

---