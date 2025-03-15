#Part A: Python Functions Assignment

import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def prime_sum(start, end):
    total = 0
    for number in range(start, end + 1):
        if is_prime(number):
            total += number
    return total

def length_converter(value, direction):
    if direction.upper() == 'm':
        return round(value * 3.28084, 2) 
    elif direction.upper() == 'f':
        return round(value / 3.28084, 2)  
    else:
        raise ValueError("Oops! That’s not a valid option. Please enter 'm' to convert meters to feet or 'f' to convert feet to meters.")

def consonant_counter(text):
    vowels = "aeiouAEIOU"
    consonants = [char for char in text if char.isalpha() and char not in vowels]
    return len(consonants)

def min_max_finder(*numb):
    if not numb:
        raise ValueError("Please enter at least one number to proceed.")
    smallest = min(numb)
    largest = max(numb)
    return f"Smallest: {smallest}, Largest: {largest}"

def palindrome_checker(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def word_counter(file_path, words_to_count):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()
            word_counts = {word: content.split().count(word) for word in words_to_count}
            return word_counts
    except FileNotFoundError:
        raise FileNotFoundError(f"The file located at {file_path} could not be found.")
        
def main():
    words_to_count = ["the", "was", "and"]
    while True:
        print("\nHere are the functions you can use:")
        print("1. Prime Number Sum Calculator")
        print("2. Length Unit Converter")
        print("3. Count consonants in string")
        print("4. Find minimum and maximum number")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("7. Exit program")
        
        choice = input("\nEnter your choice: ").strip()
        
        try:
            if choice == '1':
                start = int(input("Specify the beginning value of the range: "))
                end = int(input("Specify the ending value of the range: "))
                result = prime_sum(start, end)
                print(f"Sum of prime numbers in the range {start}-{end}: {result}")
            
            elif choice == '2':
                value = float(input("Input a valid numerical value: "))
                direction = input("Select the conversion direction: Type 'm' for meters to feet or 'f' for feet to meters: ").strip()
                result = length_converter(value, direction)
                print(f"Converted value: {result}")
            
            elif choice == '3':
                text = input("Enter a string: ")
                result = consonant_counter(text)
                print(f"Number of consonants: {result}")
            
            elif choice == '4':
                numbers = list(map(int, input("Enter numbers separated by space: ").split()))
                result = min_max_finder(*numbers)
                print(result)
            
            elif choice == '5':
                text = input("Enter a string: ")
                result = palindrome_checker(text)
                print(f"Is palindrome: {result}")
            
            elif choice == '6':
                file_path = input("Enter the file path: ").strip()
                word_counts = word_counter(file_path, words_to_count)
                print(f"Word counts: {word_counts}")
            
            elif choice == '7':
                print("Exiting program...")
                break
            
            else:
                print("Input out of range. Enter a number from 1 to 7.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        
        continue_choice = input("\nWould you like to try another function? (yes/no7): ").strip().lower()
        if continue_choice != 'y':
            break

if __name__ == "__main__":
    main()
