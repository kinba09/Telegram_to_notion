import os 
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv('DATABASE_ID')

notion = Client(auth=NOTION_TOKEN)

def note(res):
    new_page = {
    "title": {"title": [{"text": {"content": res}}]}
    }
    notion.pages.create(parent={"database_id": DATABASE_ID}, properties=new_page)
