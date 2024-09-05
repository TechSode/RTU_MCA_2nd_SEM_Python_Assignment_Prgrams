def compute_file_stats(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            # Count characters, words, and lines
            num_chars = len(content)
            num_words = len(content.split())
            num_lines = content.count('\n') + 1

            print("\nFile Statistics:")
            print(f"Number of characters: {num_chars}")
            print(f"Number of words: {num_words}")
            print(f"Number of lines: {num_lines}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

if __name__ == "__main__":
    # Input the file name
    file_name = input("Enter the file name: ")

    # Compute and display file statistics
    compute_file_stats(file_name)
