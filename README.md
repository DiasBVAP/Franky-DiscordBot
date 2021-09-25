# Franky-DiscordBot

## Who's Franky?

Franky is a barebones pseudo-bot that runs localy on your machine.
You'll need a second Discord account running on your web browser.

## Windows Installation

### Requirements

You'll need [Python](https://www.python.org/downloads/) (any Python 3.x should be fine). 
You'll also need [VB-Audio's Virtual Cable](https://vb-audio.com/Cable/).
And most likely an [additional Discord account](https://discord.com/register).

### Setup

1. Clone the repository.
2. Open Command Prompt as administrator and navigate to the project's folder.
3. Run ```pip install -r requirements.txt``` to install the necessary Python packages.
4. In *.env*, write your **secondary account's** [Discord user token](https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs#how-to-get-a-user-token) between the quotation marks.

### Deploying the Bot

- In the browser of your choice, open discord and login with your secondary account.
- Go to **User Settings > Voice and Video**.
- Change *Input Device* to *CABLE Input (VB-Audio Virtual Cable)*.
- Should probrably mute output audio.

Now simpy run ```main.py```.