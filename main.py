def reverse_words(text: str) -> str:
    reversed_words = []

    for word in text.split():
        # Create a list of [position, character] for each symbol
        symbols = [[len(word) - index - 1, c] if c.isalpha() else [index, c] for index, c in enumerate(word)]

        # Sort the list based on the position and reconstruct the word
        reversed_word = ''.join(symbol[1] for symbol in sorted(symbols, key=lambda x: x[0]))
        reversed_words.append(reversed_word)

    # Join the reversed words to form the final result
    result = ' '.join(reversed_words)
    return result


# Example usage
input_text = "a1bcd efg!h"
output_text = reverse_words(input_text)
print(output_text)
