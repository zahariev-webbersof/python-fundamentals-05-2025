# 📚 **Digital Book Collection Manager**
<img width="1076" alt="Screenshot 2025-05-28 at 17 54 38" src="https://github.com/user-attachments/assets/eb2275ec-7f18-423c-8bf3-e337dfee17f7" />

### 🔰 For Beginners Learning:

* Lists
* Indexing
* String manipulation
* Functions
* Input/output
* Loops & conditionals

---

## 🎯 **Project Goal**

Build a simple Python app to help users manage a digital collection of books.
Books are represented using **parallel lists**: one list for titles, one for authors, and one for read/unread status.

---

## ✅ **Key Features**

| Task           | Description                                     |
| -------------- | ----------------------------------------------- |
| Add Book       | Add a book's title and author to the collection |
| Mark as Read   | Change a book's status to “Read”                |
| Mark as Unread | Change a book's status to “Unread”              |
| Search Book    | Find a book by keyword in title or author       |
| List Books     | View all books with status                      |
| Suggest Book   | Recommend an unread book                        |
| Delete Book    | Remove a book from the collection               |

---

## 🧠 **Code Skeleton (With Comments Only)**

```python
# Lists to store book information
titles = []      # List of book titles
authors = []     # List of book authors
statuses = []    # List of read statuses: "Read" or "Unread"

def add_book(title, author):
    # Append the title to titles list
    # Append the author to authors list
    # Append "Unread" to statuses list
    # Print a message confirming the addition

def mark_as_read(title):
    # Loop through the titles list
    # If the title is found, update the corresponding status to "Read"
    # Print confirmation or error if not found

def mark_as_unread(title):
    # Same logic as mark_as_read, but set status to "Unread"

def search_book(keyword):
    # Loop through the titles and authors
    # If keyword is found in title or author (case-insensitive), print book info
    # If no matches, print "No books found."

def list_books():
    # Loop through all books
    # Print each title, author, and status with numbering

def suggest_book():
    # Find all books where status is "Unread"
    # If at least one unread book exists, pick one at random and suggest it
    # If all books are read, print "No unread books left."

def delete_book(title):
    # Loop through titles
    # If match found, remove the title, author, and status at the same index
    # Print confirmation or "Book not found."

def main():
    print("📚 Welcome to the Digital Book Collection Manager 📚\n")

    while True:
        print("\nPlease choose an option:")
        print("1. Add a new book")
        print("2. Mark a book as read")
        print("3. Mark a book as unread")
        print("4. Search for a book")
        print("5. List all books")
        print("6. Suggest a book to read")
        print("7. Delete a book")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            add_book(title, author)

        elif choice == '2':
            title = input("Enter the title of the book to mark as read: ")
            mark_as_read(title)

        elif choice == '3':
            title = input("Enter the title of the book to mark as unread: ")
            mark_as_unread(title)

        elif choice == '4':
            keyword = input("Enter a keyword to search: ")
            search_book(keyword)

        elif choice == '5':
            list_books()

        elif choice == '6':
            suggest_book()

        elif choice == '7':
            title = input("Enter the title of the book to delete: ")
            delete_book(title)

        elif choice == '8':
            print("Goodbye! Happy reading! 📖")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 8.")

if __name__ == "__main__":
    main()
```

---

## 🔧 **Advanced Ideas (Optional)**

* Store books in a `.txt` file for persistence
* Allow rating (another list)
* Sort books alphabetically
* Add page count and track total pages read

---

## 📘 **Learning Resources**

* [Python Lists](https://www.w3schools.com/python/python_lists.asp)
* [String Functions](https://www.w3schools.com/python/python_strings.asp)
* [Random Library](https://docs.python.org/3/library/random.html)
* [Basic File Handling](https://realpython.com/read-write-files-python/)

---

## ✅ **How to Upload to GitHub**

Same steps as before using GitHub Desktop:

1. Create a new repository
2. Name it something like `book-manager-no-dictionaries`
3. Add your Python file
4. Commit & push to GitHub

---

## 🎓 **Student Checklist**

* [ ] Used only lists and strings (no dictionaries!)
* [ ] Added meaningful comments
* [ ] Tested add, mark, search, and delete features
* [ ] Handled invalid inputs
* [ ] Program is easy to read and navigate
