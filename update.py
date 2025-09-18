from db import sb

def update_stock(book_id, new_stock):
    resp = sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    return resp.data

def update_member(member_id, email):
    resp = sb.table("members").update({"email": email}).eq("member_id", member_id).execute()
    return resp.data

if __name__ == "__main__":
    print("1. Update member\n2. Update stock")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        mid = int(input("Enter member id: ").strip())
        new_email = input("Enter new email: ").strip()
        updated = update_member(mid, new_email)
        print(f"📧 Email updated to {new_email}" if updated else "No member found")
        
    elif ch == 2:
        bid = int(input("Enter book id to update stock: ").strip())
        new_stock = int(input("Enter new stock: ").strip())
        updated = update_stock(bid, new_stock)
        print(f"📚 Stock updated to {new_stock}" if updated else "No book found")
