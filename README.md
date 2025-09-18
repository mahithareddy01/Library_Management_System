A command-line Python app to manage a library using Supabase (Postgres) as the backend.
Handles real-life operations: register members, manage books, track borrow/return transactions, and generate reports.

⚡ Features:

👩‍🎓 Register new members
📖 Add, update, or remove books
🔁 Borrow & return books (with date tracking)
📊 Generate reports: overdue books, most borrowed books
💾 Persistent storage using Supabase (Postgres)

💻 How to Run
# clone this repo
git clone https://github.com/mahithareddy01/Library-Management-System.git

# go inside project folder
cd library-management-system

# install dependencies (if any)
pip install supabase

# run the scripts
python create.py

python read.py

python update.py

python delete.py
