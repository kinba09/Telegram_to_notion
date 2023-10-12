
# Telegram to Notion BOT

This bot takes input from you and sends it to Notion's API, which then adds a new page with that data to a Notion database. This way, you can easily keep track of all your important information in one place.




# Tech Stack

**Notion-client:** Improved: I used the Notion client library to create a new page in the Notion database.


**python-telegram-bot:** Improved: I used the Python Telegram Bot library to get input from users in Telegram.




# Run Locally
## Prerequisites
Before diving into the project, ensure you have Python installed. You can download the latest version from python.org.

## installation
Clone the project

```bash
  git clone https://github.com/kinba09/Telegram_to_notion.git
```


Install the required dependencies:


```bash
  pip install -r requirements.txt
```
## Telgeram BOT setup
To create a Telegram bot, follow these steps:

* Search for BotFather in Telegram and press /start.
* Press /newbot and follow the given instructions.
* Save the API key in a safe place.

## Notion setup
To create the notion API, follow this link
- [Notion integration](https://developers.notion.com/docs/create-a-notion-integration#getting-started)
- [Notion database ID](https://developers.notion.com/reference/retrieve-a-database#:~:text=To%20find%20a%20database%20ID,a%2032%20characters%20alphanumeric%20string.)
* Then save these keys

## Usage
- Save those three keys in an ```.env``` file
- Then run the ```telegram_back_again.py```
- Now you can send any message in that telegram bot which will be added to the notion's database
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DATABASE_ID` `NOTION_TOKEN` `TELEGRAM_TOKEN`


# Note

- Make sure to use the correct names which are used in the database's title 

