import os
from supabase import Client,create_client
from dotenv import load_dotenv

load_dotenv()

url=os.getenv("supabase_url")
key=os.getenv("supabase_key")

sb: Client = create_client(url, key)