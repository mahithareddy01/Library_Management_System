from db import sb

def delete_member(member_id):
    borrowed = sb.table("borrow_records").select("*")\
        .eq("member_id", member_id).is_("return_date", None).execute()
    if borrowed.data: return False
    return sb.table("members").delete().eq("member_id", member_id).execute()

def delete_book(book_id):
    borrowed = sb.table("borrow_records").select("*")\
        .eq("book_id", book_id).is_("return_date", None).execute()
    if borrowed.data: return False
    return sb.table("books").delete().eq("book_id", book_id).execute()

if __name__ == "__main__":
    print("1. Delete Member\n2. Delete Book")
    ch = int(input("Pick: "))

    if ch == 1:
        mid = int(input("Member ID: "))
        print("Deleted" if delete_member(mid) else "Can't delete: still borrowed!")
    else:
        bid = int(input("Book ID: "))
        print("Deleted" if delete_book(bid) else "Can't delete: book is borrowed!")