# Franky-DiscordBot

## Who's Franky?

Franky is a music Discord selfbot/userbot (it automates an user account to act as a bot and play music).

## What can Franky do?

Franky is able to respond to the following commands:
- ```!!play <youtube-link>```: Franky will download the video refered by the link, convert it to audio and play it.
- ```!!play <search-term>```: Franky will search for the term in youtube and download the first video it finds. Then it will convert it to audio and play it.
- ```!!play```: If a song is paused it will unpause it, otherwise do nothing.
- ```!!pause```: If a song is playing it will pause it, otherwise do nothing.
- ```!!stop```: It will stop the current song so you can request a new one.
- ```!!loop```: Starts looping the song currently playing. To stop looping simply stop the song or start a new one.

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
4. In **.env**:
   1. On the first line, write your **secondary account's** [Discord user token](https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs#how-to-get-a-user-token) between the quotation marks.
   2. On the second line, write the [channel ID](https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs#how-to-get-a-server-id-or-a-server-channel-id) of the channel you want the bot to send confirmation messages on. 
   3. On the third line, write the maximum size (MB) you want the cache to be (Franky will delete the oldest song when the cache folder reaches the limit). 

### Deploying the Bot

1. With the browser of your choice, open discord and login with your secondary account.
2. Mute your output audio (:headphones:).
3. Go to **User Settings > Voice and Video**.
4. Change *Input Device* to *CABLE Input (VB-Audio Virtual Cable)*.
5. Disable all of Discord's audio processing options.
6. Disable automatic input sensibility and make the sensibility -99dB.

Now simpy join a voice call with your secondary account and run ```main.py```.