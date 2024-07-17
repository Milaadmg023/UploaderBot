<h1>Telegram Uploader Bot</h1>

This project implements a Telegram bot built using the Pyrogram library. Its primary function is to facilitate file sharing within Telegram chats by generating links that users can share directly.

Features:

File Linking: Uploads files received from users to a chosen storage provider (e.g., cloud storage platform) and generates a shareable link.
Accessibility: Simplifies file sharing for users who prefer links over in-chat media.
<br>

<h1>Installation:</h1>

Prerequisites:
Python 3.6 or later
pip (package installer)
Clone this repository:
```sh
git clone https://github.com/Milaadmg023/UploaderBot
cd telegram-file-linking-bot
```

<h1>Install dependencies:</h1>

```sh
pip install pyrogram
```

<h3>Install additional dependencies for your chosen storage provider (if needed)</h3>


<h1>Configuration:</h1>

Obtain your Telegram bot token from BotFather (https://m.youtube.com/watch?v=UQrcOj63S2o).
Store the token securely in a .env file at the project root:

<h3>
APP_ID ,
BOT_TOKEN ,
TRACK_CHANNEL ,
OWNER_ID 
</h3>

<br>
<h1>Running the Bot:</h1>

<h3>1. Start the Bot:</h3>

```sh
python bot.py
```

<h3>2. Invite the Bot to Your Telegram Chat:</h3>

Open Telegram and search for your bot using its username.
Add the bot to your desired Telegram chat.
Using the Bot:

Send files directly to the bot in your Telegram chat.
The bot will upload the file to the chosen storage provider and generate a shareable link.
Share the generated link with anyone who needs to access the file.
Additional Notes:

Depending on your chosen storage provider, you might need to install additional libraries to handle file uploads and link generation.
Consider implementing error handling and logging for a more robust experience.
Explore advanced features like file size limitations, user authentication, or custom link prefixes (if applicable to your storage provider).
Disclaimer:

This is a basic template to get you started. You may need to modify the code and configuration based on your specific requirements and chosen storage provider.
