def count_char_frequency(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            char_count = {}

            for char in content:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

            return char_count
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return {}

def guess_file_type(file_name):
    char_count = count_char_frequency(file_name)

    # Guess file type based on character frequency
    if '.py' in file_name:
        print("This is a Python file.")
    elif '.c' in file_name:
        print("This is a C program file.")
    else:
        print("This is a text file.")

if __name__ == "__main__":
    # Input the file name
    file_name = input("Enter the file name: ")

    # Count character frequency
    char_count = count_char_frequency(file_name)

    # Display the character frequency
    if char_count:
        print("\nCharacter Frequency in the file:")
        for char, count in char_count.items():
            print(f"'{char}': {count}")

        # Guess file type
        guess_file_type(file_name)
