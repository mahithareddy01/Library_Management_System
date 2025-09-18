from db import sb

def list_books():
    return sb.table("books").select("*").execute()

def search_books(keyword):
    return sb.table("books").select("*")\
        .or_(f"title.ilike.%{keyword}%," 
             f"author.ilike.%{keyword}%," 
             f"category.ilike.%{keyword}%").execute()

def list_members():
    return sb.table("members").select("*").execute()
