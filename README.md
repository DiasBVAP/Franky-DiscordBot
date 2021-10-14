# Franky-DiscordBot

## Who's Franky?

Franky is a music Discord selfbot/userbot (it automates an user account to act as a bot and play music).

**Selfbots are against Discord's TOS, use at your own risk.**

## How does it work?

Franky has a queue that you can add songs to with ```!!add```. You can also play separate songs from the queue with ```!!play```.

## What can Franky do?

Franky is able to respond to the following commands:
- ```!!play <youtube-link>```: Download the video from *youtube-link* and play it.
- ```!!play <search-term>```: Download the first video it finds by searching *search-term* on YouTube, then play it.
- ```!!play <song-index>```: Play the song at *song-index* on queue.
- ```!!play```: If a song is paused it will unpause it, otherwise do nothing.
- ```!!add <youtube-link>```: Download video from *youtube-link*, and add it to the queue.
- ```!!add <search-term>```: Download the first video it finds by searching *search-term* on YouTube, then add it to the queue. 
- ```!!pause```: Pause the current song.
- ```!!stop```: Stop the current song and clear the queue.
- ```!!loop```: Start looping the current song.
- ```!!lq```: Toggle looping whole queue (default off).
- ```!!next```: Play next song on queue.
- ```!!last```: Play previous song on queue.
- ```!!queue```: Return the current queue.
- ```!!rm <song-index>```: Remove the song at *song-index* from queue.
- ```!!help```: Show help message containing these commands.

## Windows Installation

### Requirements

- [Python](https://www.python.org/downloads/) (v3.8 or superior). 
- [FFmpeg](https://ffmpeg.org/download.html). You'll need to add it to Windows's PATH enviroment variable.
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
   4. On the last line, write your secondary account's username. 

### Deploying the Bot

1. On your browser, open discord and login with your secondary account.
2. Mute your output audio (:headphones:).
3. Go to **User Settings > Voice and Video**.
4. Change *Input Device* to *CABLE Input (VB-Audio Virtual Cable)*.
5. Disable all of Discord's audio processing options.
6. Disable automatic input sensibility and make the sensibility -99dB.

Now simpy join a voice call with your secondary account and run ```main.py```.

# Donations

<img src="https://github.com/AsaiOgawa/Donations/blob/main/bitcoin.png?raw=true" height=16> Bitcoin | <img src="https://github.com/AsaiOgawa/Donations/blob/main/monero.png?raw=true" height=16> Monero
:------:|:------:
<img href="https://github.com/AsaiOgawa/Donations/blob/main/Bitcoin" src="https://github.com/AsaiOgawa/Donations/blob/main/bitcoin-qrcode.png?raw=true" width=200> | <img href="https://github.com/AsaiOgawa/Donations/blob/main/Monero" src="https://github.com/AsaiOgawa/Donations/blob/main/monero-qrcode.png?raw=true" width=200>
