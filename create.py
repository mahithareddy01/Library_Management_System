from db import sb
def add_member(name,email):
    data={"name":name,"email":email}
    resp=sb.table("members").insert(data).execute()
    return resp
def add_book(title,author,category,stock):
    data={"title":title,"author":author,"category":category,"stock":stock}
    resp=sb.table("books").insert(data).execute()
    return resp
if __name__=="__main__":
    print("1.Add a Member\n2.Add a book")
    ch=int(input("enter your choice: "))
    if ch==1:
        n=input("Enter name of the member: ")
        e=input("Enter email of the member: ")
        added=add_member(n,e)
        if(added):
            print(f"new member {n} is added to the library")
    elif ch==2:
        t=input("Enter title of the book: ")
        a=input("Enter author name for book: ")
        c=input("Enter category the book belongs to: ")
        s=int(input("Enter stock: "))
        added_book=add_book(t,a,c,s)
        if(added_book):
            print(f"{t} is added to the library")
