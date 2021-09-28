# Franky-DiscordBot

## Who's Franky?

Franky is a barebones pseudo-bot that runs localy on your machine.
You'll need a second Discord account running on your web browser.

## What can Franky do?

Franky is able to respond to the following commands:
- ```!!play <youtube-link>```: Franky will download the video refered by the link, convert it to audio and play it.
- ```!!play <search-term>```: Franky will search for the term in youtube and download the first video it finds. Then it will convert it to audio and play it.
- ```!!play```: If a song is paused it will unpause it, otherwise do nothing.
- ```!!pause```: If a song is playing it will pause it, otherwise do nothing.
- ```!!stop```: It will stop the current song so you can request a new one.
- ```!!loop```: Starts looping the song currently playing. To stop looping simply stop the song.

## Windows Installation

### Requirements

You'll need:
- [Python](https://www.python.org/downloads/) (any Python 3.x should be fine). 
- [VB-Audio's Virtual Cable](https://vb-audio.com/Cable/).
- An additional [Discord account](https://discord.com/register).

### Setup

1. Clone the repository.
2. Open Command Prompt as administrator and navigate to the project's folder.
3. Run ```pip install -r requirements.txt``` to install the necessary Python packages.
4. In *.env*, write your **secondary account's** [Discord user token](https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs#how-to-get-a-user-token) between the quotation marks in the first line.
5. Also in *.env*, write the [channel ID](https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs#how-to-get-a-server-id-or-a-server-channel-id) of the channel you want the bot to send confirmation messages on. 

### Deploying the Bot

1. With the browser of your choice, open discord and login with your secondary account.
2. Go to **User Settings > Voice and Video**.
3. Change *Input Device* to *CABLE Input (VB-Audio Virtual Cable)*.
- Should probrably mute your output audio.

Now simpy join a voice call with your secondary account and run ```main.py```.