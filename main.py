def reverse_words(text: str) -> str:
    reversed_words = []

    for word in text.split():
        symbols = [[len(word) - index - 1, c] if c.isalpha() else [index, c] for index, c in enumerate(word)]

        reversed_word = ''.join(symbol[1] for symbol in sorted(symbols, key=lambda x: x[0]))
        reversed_words.append(reversed_word)

    result = ' '.join(reversed_words)
    return result


if __name__ == '__main__':
    input_text = "a1bcd efg!h"
    output_text = reverse_words(input_text)
    print(output_text)
