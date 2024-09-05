def demonstrate_list_and_tuple():
    # List demonstration
    fruits_list = ["Apple", "Banana", "Cherry", "Mango"]
    print("List Example:")
    print(fruits_list)

    # Adding an item to the list
    fruits_list.append("Orange")
    print("List after appending 'Orange':")
    print(fruits_list)

    # Tuple demonstration
    Vehicle_tuple = ("Car", "Bike", "Bus", "Train")
    print("\nTuple Example:")
    print(Vehicle_tuple)

    # Looping through list
    print("\nLooping through the list:")
    for fruit in fruits_list:
        print(fruit)

    # Looping through tuple
    print("\nLooping through the tuple:")
    for vehicle in Vehicle_tuple:
        print(vehicle)

if __name__ == "__main__":
    demonstrate_list_and_tuple()
