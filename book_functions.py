def get_book_text(filepath):
    """Read a file and return its contents as a string."""
    with open(filepath, 'r') as file:
        return file.read()

def main():
    # Use the function with the relative path to frankenstein.txt
    book_text = get_book_text("books/frankenstein.txt")
    
    # Print the entire contents of the book to the console
    print(book_text)

# Call main() at the bottom to execute your program
if __name__ == "__main__":
    main()


def get_book_text(filepath):
    """Read a file and return its contents as a string."""
    with open(filepath, 'r') as file:
        return file.read()

def count_words(text):
    """Accept text as a string and return the number of words."""
    words = text.split()
    return len(words)

def main():
    # Get the book text
    book_text = get_book_text("bookbot/books/frankenstein.txt")
    
    # Count the words using the new function
    num_words = count_words(book_text)
    
    # Print the required message
    print(f"Found {num_words} total words")

# Call main() at the bottom to execute your program
if __name__ == "__main__":
    main()