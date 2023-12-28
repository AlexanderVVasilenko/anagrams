# Running Tests for `test_reverse_words.py`

This repository includes a test file named `test_reverse_words.py` for testing the reverse_words function.

## Setting Up Virtual Environment

To set up a virtual environment, follow these steps:

1. Open a terminal in the project directory.

2. Run the following commands:

   ```bash
   python -m venv venv
   ```
This will create a virtual environment named venv.

Activate the virtual environment:

On Windows:

```bash
.\venv\Scripts\activate
```
On Unix or macOS:

```bash
source venv/bin/activate
```

## Prerequisites

Make sure you have the necessary dependencies installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```
## Running Tests
To run the tests, execute the following command:

```bash
pytest test_reverse_words.py
```
This will execute the test suite in the specified file and display the results.

### Options
You can also specify additional options when running tests. For example:

Run tests and show print statements:

```bash
pytest -s test_reverse_words.py
```
Run specific tests by providing the test name:

```bash
pytest test_reverse_words.py::test_reverse_words_single_word
```
For more information about available options, you can refer to the [pytest documentation](https://docs.pytest.org/en/latest/).
