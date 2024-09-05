def count_characters(input_string):
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

if __name__ == "__main__":
    # Take input from the user
    input_string = input("Enter a string: ")

    # Call the function to count characters
    result = count_characters(input_string)

    # Display the result
    print("Character count in the string:")
    for char, count in result.items():
        print(f"'{char}': {count}")
