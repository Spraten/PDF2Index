# PDF2Index

# SANS Text to Index

## Overview

SANS Text to Index is a Python script that facilitates the process of generating an index for a SANS PDF book converted into a text file using pdftotext. The script extracts relevant words and phrases from the text and organizes them into an index. Additionally, it offers the option to include specific user-defined words, phrases, or acronyms in the index.

## Usage

```
python3 sans_text_to_index.py -i <input-file> [-o <output-file>] [-n <student-name>] [-w <words-file>]
```

#### Arguments:

- `-i`, `--input-file`: The path to the SANS text file.
- `-o`, `--output-file`: (Optional) The path to save the generated index file. If not provided, a default file will be created using the input file's name with `_index.txt` appended.
- `-n`, `--student-name`: (Optional) The full name of the student. This is used as a delimiter to split the pages of the SANS book.
- `-w`, `--words-file`: (Optional) The path to a file containing specific words, phrases, or acronyms that you want to include in the index.

## Requirements

- Python 3.x
- The `requests` library

Install the required library using pip:

```
pip install requests
```

## Examples

1. Basic usage:

```
python3 sans_text_to_index.py -i input.txt
```

This command will generate an index for the `input.txt` file, and the output will be saved in `input_index.txt`.

2. Including specific words:

```
python3 sans_text_to_index.py -i input.txt -w specific_words.txt
```

This will generate an index for `input.txt`, and it will include the words, phrases, or acronyms listed in the `specific_words.txt` file.

## Notes

- The script uses an online list of common English words to filter out frequently used and unimportant words from the index.
- It removes common punctuation and other characters from the words to improve accuracy.
- The final index is sorted alphabetically, case-insensitive, and written to the output file.

