from db import sb
def list_books():
    return sb.table("books").select("*").execute()

def search_books(keyword):
    return sb.table("books").select("*")\
        .ilike("title", f"%{keyword}%").execute()

def member_info(member_id):
    member = sb.table("members").select("*").eq("member_id", member_id).execute()
    borrowed = sb.table("borrow_records").select("book_id, borrow_date")\
        .eq("member_id", member_id).is_("return_date", None).execute()
    return member, borrowed

if __name__ == "__main__":
    print("1. All Books\n2. Search Books\n3. Member Info")
    ch = int(input("Pick: "))

    if ch == 1:
        for b in list_books().data: print(f"{b['title']} ({b['stock']} in stock)")
    elif ch == 2:
        key = input("Keyword: ")
        for b in search_books(key).data: print(b['title'], "-", b['author'])
    elif ch == 3:
        mid = int(input("Member ID: "))
        m, br = member_info(mid)
        print("Member:", m.data[0]['name'])
        for r in br.data: print("Borrowed Book ID:", r['book_id'])
