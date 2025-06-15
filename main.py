import sys
from stats import count_words, count_characters, sort_charachter_counts

# Validate arguments
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

# # Path to the book
# book_path = "books/frankenstein.txt"

# Read the book
try:
    with open(book_path, "r") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Error: Could not find the file at {book_path}")
    sys.exit(1)

# Count words and characters
num_words = count_words(contents)
char_counts = count_characters(contents)
sorted_chars = sort_charachter_counts(char_counts)

# Print report
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")

for item in sorted_chars:
    print(f"{item['char']}: {item['num']}")

print("============= END ===============")
