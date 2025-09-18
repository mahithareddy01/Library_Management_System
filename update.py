from db import sb

def update_stock(book_id, new_stock):
    resp = sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    return resp.data

def update_member(member_id, email):
    resp = sb.table("members").update({"email": email}).eq("member_id", member_id).execute()
    return resp.data
