from db import sb

def delete_member(mid):
    active = sb.table("borrow_records").select("*")\
        .eq("member_id", mid).is_("return_date", None).execute()
    if active.data:
        return "Member still has borrowed books"
    sb.table("members").delete().eq("member_id", mid).execute()
    return "Member deleted"

def delete_book(bid):
    active = sb.table("borrow_records").select("*")\
        .eq("book_id", bid).is_("return_date", None).execute()
    if active.data:
        return "Book is still borrowed"
    sb.table("books").delete().eq("book_id", bid).execute()
    return "Book deleted"
