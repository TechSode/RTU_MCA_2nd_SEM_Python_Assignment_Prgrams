def sequential_search(lst, target):
    # Iterate through each element in the list
    for index, element in enumerate(lst):
        # Check if the current element matches the target
        if element == target:
            return index  # Return the index of the found element
    return -1  # Return -1 if the target is not found in the list

# Example usage
lst = [10, 25, 30, 45, 50, 65]
target = 45

# Call the function and store the result
result = sequential_search(lst, target)

# Display the result
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
