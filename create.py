from db import sb

def add_member(name, email):
    resp = sb.table("members").insert({"name": name, "email": email}).execute()
    return resp.data

def add_book(title, author, category, stock):
    resp = sb.table("books").insert({
        "title": title, "author": author,
        "category": category, "stock": stock
    }).execute()
    return resp.data
