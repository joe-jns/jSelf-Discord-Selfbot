# jSelf - Your Personal Discord Selfbot

Welcome to **jSelf**, your personal Discord selfbot. Follow the instructions below to set up and run the bot on your machine.

## Prerequisites

Ensure you have the following installed on your machine:
- Python 3.6+
- pip (Python package installer)

## Setup Instructions

### Step 1: Run the Setup Script

To get started, run the `setup.bat` script. This will create a `.env` file and install all necessary dependencies.

```bash
setup.bat
```

### Step 2: Configure the .env File

After running the setup script, configure the `.env` file with your Discord account token and preferred command prefix. You can find the `.env` file in the root directory of the project.

```plaintext
DISCORD_TOKEN=Your_Discord_Account_Token_Here
COMMAND_PREFIX=Your_Command_Prefix_Here
AUTOJOIN_CHANNEL_ID=Your_Autojoin_Channel_ID_Here (optional)
```

- `DISCORD_TOKEN`: Your Discord account token. **Important: This is your personal token and not a bot token.**
- `COMMAND_PREFIX`: The prefix you want to use for your bot commands.
- `AUTOJOIN_CHANNEL_ID`: The ID of the voice channel you want the bot to join automatically upon startup (optional).

### Step 3: Run the Bot

Once you have configured the `.env` file, you can start the bot by running the following command in your terminal:

```bash
python main.py
```

## Features

### Available Commands

- **Utility Commands:**
  - `ping`: Displays the bot's latency.
  - `prefix`: Changes the command prefix for the server and updates the `.env` file.
  - `adminservers`: Lists the servers where you have administrative permissions and the number of members.

- **Vocal Commands:**
  - `joinvc`: Joins a specified voice channel by ID.
  - `leavevc`: Leaves the current voice channel.
  - `autojoin`: Sets a voice channel for the bot to join automatically on startup.

## Contributions

Feel free to fork this repository and make your own modifications. If you have any suggestions or find any issues, please open an issue on the [GitHub repository](https://github.com/JnsJoe/jSelf).

---

Thank you for using **jSelf**. Enjoy your enhanced Discord experience!

---