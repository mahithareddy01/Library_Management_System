from create import add_member, add_book
from read import list_books, search_books
from update import update_stock, update_member
from delete import delete_book, delete_member

def main():
    while True:
        print("\n📚-----Library Management System Menu----")
        print("1. Add Member")
        print("2. Add Book")
        print("3. List/Search Books")
        print("4. Update Member/Book")
        print("5. Delete Member/Book")
        print("0. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            name = input("Member Name: ")
            email = input("Member Email: ")
            resp = add_member(name, email)
            print(f"Member '{name}' added" if resp else "⚠️Error adding member")
        
        elif choice == "2":
            title = input("Book Title: ")
            author = input("Author: ")
            category = input("Category: ")
            stock = int(input("Stock: "))
            resp = add_book(title, author, category, stock)
            print(f"Book '{title}' added" if resp else "⚠️Error adding book")
        
        elif choice == "3":
            print("\n📖 Books Menu: 1-List all, 2-Search")
            sub = input("Choice: ").strip()
    
            response = list_books() if sub == "1" else search_books(input("Keyword: ").strip()) if sub == "2" else None
            if not response:
                print("⚠️ Invalid choice."); continue
    
            books = response.data
            if not books:
                print("⚠️ No books found.")
            else:
                for b in books:
                    print(f"{b['book_id']}. {b['title']} | {b['author']} | {b.get('category','N/A')} | Stock: {b['stock']}")

        
        elif choice == "4":
            sub = input("Update (1) Member or (2) Book? ")
            if sub == "1":
                mid = int(input("Member ID: "))
                email = input("New Email: ")
                resp = update_member(mid, email)
                print("Email updated" if resp else "Member not found")
            else:
                bid = int(input("Book ID: "))
                stock = int(input("New Stock: "))
                resp = update_stock(bid, stock)
                print("Stock updated" if resp else "Book not found")
        
        elif choice == "5":
            sub = input("Delete (1) Member or (2) Book? ")
            if sub == "1":
                mid = int(input("Member ID: "))
                print(delete_member(mid))
            else:
                bid = int(input("Book ID: "))
                print(delete_book(bid))
        
        elif choice == "0":
            print("Exiting Library Management System. Bye!")
            break
        
        else:
            print("⚠️Invalid choice. Try again.")

if __name__ == "__main__":
    main()
