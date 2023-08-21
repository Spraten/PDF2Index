#!/usr/bin/env python3
import requests as rq
import argparse
import sys
from fuzzywuzzy import process

# Parse input
Usage = ("""{}SANS Txt to Index
Use pdftotext to convert a SANS PDF to a txt file, then generate its index here.
Usage:
\t-i, --input-file: txt file of SANS book.
\t-o, --output-file: file to save new index at.
\t-n, --student-name: full name of student, used to split pages by delimiter.
\t-w, --words-file: file containing specific words/phrases/acronyms to be indexed.
""")

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-file", help="txt file of SANS book.")
parser.add_argument("-o", "--output-file", help="output file of index.")
parser.add_argument("-n", "--student-name", help="full name of student.")
parser.add_argument("-w", "--words-file", help="file containing specific words/phrases/acronyms.")
options = parser.parse_args(sys.argv[1:])

if not options.input_file:
    exit(Usage.format("Please enter an index file.\n"))

if not options.output_file:
    options.output_file = options.input_file.replace(".txt", "") + "_index.txt"

delimeter = "Licensed To: "
if options.student_name:
    delimeter += options.student_name

# Load specific words
specific_words = []
if options.words_file:
    with open(options.words_file, 'r',) as wf:
        specific_words = [line.strip() for line in wf]

# Get common English words
common_words = set(rq.get("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt").text.split("\n"))

# Function to recursively strip given characters in a word
characters_to_strip = "()'\":,”“‘?;-•’—…[]!"
phrases_to_strip = ["'s", "'re", "'ve", "'t", "[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]"]

def strip_characters(word):
    word_length = len(word)
    word = word.replace("’", "'")
    while True:
        for phrase in phrases_to_strip:
            if word.endswith(phrase):
                word = word[:-len(phrase)]
        word = word.strip(characters_to_strip).rstrip(".")
        if len(word) == word_length:
            return word
        else:
            word_length = len(word)

# Check that word should be added to index
def word_is_eligible(word):
    if len(word) < 3 or word[0].isdigit() or word.lower() in common_words or word.startswith(("http://", "https://")):
        return False
    return True

# Get pages in the text file
with open(options.input_file, "r", ) as f:
    data = f.read()
    pages = data.split(delimeter)[1:]

print(f"Number of pages found: {len(pages)}")

# Initialize specific word index
specific_word_index = {word: [] for word in specific_words}

# Process each page to build the main index and specific word index
index = {}
total_words = []
for page_idx, page in enumerate(pages):
    page = page.replace("\n", " ").replace("\t", " ").replace("  ", " ").strip()
    words = page.split(" ")
    long_words = [strip_characters(word).lower() for word in words if word_is_eligible(strip_characters(word).lower())]
    total_words += long_words
    index[page_idx] = long_words

    print(f"Processing page {page_idx}: {len(long_words)} long words found")
    print(f"Long words found on page {page_idx}: {long_words[:5]}...")  # Print first 5 long words

    # Check for specific words in the word list and populate their index
    for word in specific_words:
        if word.lower() in page.lower():
            specific_word_index[word].append(str(page_idx))

# Combine the specific word index with the main index
results = {word.lower(): sorted(set(pages)) for word, pages in specific_word_index.items() if pages}

# For the main index
for word in set(total_words):
    pages_word_is_in = [str(page) for page in index.keys() if word in index[page]]
    if len(pages_word_is_in) < 15:
        results[word.lower()] = sorted(set(pages_word_is_in))

# Consolidate similar words using fuzzy matching
consolidated_results = {}
for word, pages in results.items():
    match_score = process.extractOne(word, consolidated_results.keys(), score_cutoff=80)
    if match_score:
        match, score = match_score
        consolidated_results[match] += pages
        consolidated_results[match] = sorted(set(consolidated_results[match]))
    else:
        consolidated_results[word] = pages

# Sort and save the results
sorted_results = [f"{word}: {', '.join(pages)}" for word, pages in sorted(consolidated_results.items(), key=lambda x: x[0].casefold())]

with open(options.output_file, "w", encoding='utf-8') as f:
    for result in sorted_results:
        f.write(result + "\n")

print(f"Total results: {len(sorted_results)}")
print(f"Written index to {options.output_file}")
