while True:
    file = input("Enter a file name (or 'q' to quit): ")
    if file.lower() == "q":
        break

    try:
        with open(file, "r") as f:
            content = f.read()

            # Count characters
            num_chars = len(content)
            print(f"Number of characters: {num_chars}")

            # Count words
            words = content.split()
            num_words = len(words)
            print(f"Number of words: {num_words}")

            # Count lines
            lines = content.splitlines()
            num_lines = len(lines)
            print(f"Number of lines: {num_lines}")

            # Find most frequent words
            word_freq = {}
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1

            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
            print("Most frequent words:")
            for word, freq in sorted_words[:5]:  # Print top 5 most frequent words
                print(f"  {word}: {freq}")

    except FileNotFoundError:
        print(f"File '{file}' not found. Please try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    print()  # Add a blank line for readability between iterations
