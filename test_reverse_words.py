# test_reverse_words.py
from main import reverse_words  # Replace 'your_module' with the actual module name


class TestReverseWords:
    def test_reverse_words_basic(self):
        input_text = "abcd efgh"
        expected_output = "dcba hgfe"
        assert reverse_words(input_text) == expected_output

    def test_reverse_words_with_symbols(self):
        input_text = "a1bcd efg!h"
        expected_output = "d1cba hgf!e"
        assert reverse_words(input_text) == expected_output

    def test_reverse_words_empty_input(self):
        input_text = ""
        assert reverse_words(input_text) == ""

    def test_reverse_words_single_word(self):
        input_text = "hello"
        expected_output = "olleh"
        assert reverse_words(input_text) == expected_output

    def test_reverse_words_mixed_case(self):
        input_text = "AbCd EfGh"
        expected_output = "dCbA hGfE"
        assert reverse_words(input_text) == expected_output
