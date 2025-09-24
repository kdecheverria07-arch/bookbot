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