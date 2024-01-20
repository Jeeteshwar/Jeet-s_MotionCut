def word_count(sentence):
    # Check if the input sentence is empty
    if not sentence.strip():
        return 0

    # Split the sentence into words and count them
    words = sentence.split()
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ")

    # Call the word_count function to get the word count
    count = word_count(user_input)

    # Display the word count
    print(f"Word Count: {count}")

if __name__ == "__main__":
    main()
