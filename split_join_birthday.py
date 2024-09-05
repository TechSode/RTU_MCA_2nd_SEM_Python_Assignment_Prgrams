def trace_birthday():
    # Dictionary to store names and birthdays
    birthdays = {
        "Ronak": "20/08/1995",
        "Bob": "03/23/1985",
        "Charlie": "07/30/1992"
    }
    
    # Asking user for the name
    name = input("Enter the name to find their birthday: ")

    # Searching for the name in the dictionary
    if name in birthdays:
        print(f"{name}'s birthday is on {birthdays[name]}")
    else:
        print(f"Sorry, no birthday information found for {name}")

def demonstrate_split_and_join():
    # Using split to convert a string into a list
    sentence = "This is an example sentence"
    words = sentence.split()  # Splits on spaces by default
    print(f"List of words: {words}")
    
    # Using join to convert a list back into a string
    joined_sentence = " ".join(words)
    print(f"Joined sentence: {joined_sentence}")

if __name__ == "__main__":
    # Demonstrating split and join methods
    demonstrate_split_and_join()

    # Tracing a birthday using dictionary
    trace_birthday()
