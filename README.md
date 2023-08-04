## PDF2Index

PDF2Index is a Python script that converts a SANS PDF to a text file and generates an index from the text. The script utilizes `pdftotext` to convert the PDF to a text file and then processes the text to create an index. Users can specify specific words, phrases, or acronyms to be included in the index.

### Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)

### Usage

```
python3 pdf2index.py -i <input-file> [-o <output-file>] [-n <student-name>] [-w <words-file>]
```

#### Arguments:

- `-i`, `--input-file`: The path to the SANS text file.
- `-o`, `--output-file`: (Optional) The path to save the generated index file. If not provided, a default file will be created using the input file's name with `_index.txt` appended.
- `-n`, `--student-name`: (Optional) The full name of the student. This is used as a delimiter to split the pages of the SANS book.
- `-w`, `--words-file`: (Optional) The path to a file containing specific words, phrases, or acronyms that you want to include in the index.

### AcronymHunter

AcronymHunter is a Python tool I created to work in conjunction with PDF2Index. It allows users to extract abbreviations, acronyms, and function calls from text files. Using regular expressions, this script facilitates a comprehensive and precise search to extract relevant patterns from the provided text.
https://github.com/Spraten/AcronymHunter

#### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Spraten/PDF2Index.git
   ```
2. Navigate to the repository directory:
   ```bash
   cd PDF2Index
   ```

#### Usage

1. Convert PDF to text: Use `pdftotext` to convert the PDF to a text file. If the PDF is password-protected, remove the password using `qpdf` before conversion. For example:
   ```bash
   qpdf --password=enterpasswordhere -decrypt "InputFilename.pdf" "OutputFilename.pdf"
   pdftotext unencryptedfile.pdf coursetxt.txt
   ```
2. Place the text file you want to analyze into the repository directory. The script is set to read from a file named `input.txt` by default.
3. Run the script:
   ```bash
   python3 AcronymHunter.py
   ```
4. The findings—abbreviations, acronyms, and function calls—will be stored in `out.txt`.

#### Customizing Input/Output

To target a different file or alter the output file name:

1. Open `AcronymHunter.py` in a text editor or IDE of your choice.
2. Change the filename in the `find_abbreviations("input.txt")` line to your intended input filename.
3. (Optionally) To adjust the output filename, modify the `io.open("out.txt", 'w', encoding='utf-8')` line.

### PDF2Index_Combiner

PDF2Index_Combiner is a Python script that combines multiple index files generated using PDF2Index into a single consolidated index. It takes the filenames of the index files as command-line arguments and merges their content into a new index file.

#### Usage

```
python pdf2index_combiner.py index1.txt index2.txt index3.txt ...
```

- Provide the filenames of the index files you want to combine as command-line arguments. Separate each filename with a space.

#### Customization

- You can modify the script according to your requirements. For example, change the output filename by modifying the `output_file` variable.
- Customize the input file format if your index files have a different structure.
- Modify the separators or formatting used when combining the entries.

## Generating Input for PDF2Index

You can use the AcronymHunter tool to extract relevant keywords, abbreviations, and acronyms from the text, which can be used as input for PDF2Index. The AcronymHunter tool recognizes and extracts abbreviations, acronyms, and function calls from the text files, making it easier to create a comprehensive index for your SANS book.

### License

This project is open-sourced and distributed under the MIT License.

# IMPORT NOTE 
The majority of the code for PDF2Index is derived from the open-source project available at https://github.com/Ge0rg3/sans-index-creator. I want to give credit to the original author, as their work forms the foundation of this project. I deeply respect and appreciate the effort they put into creating a useful tool for generating book indexes from SANS PDFs.

While I have used their code as a starting point, I have made significant modifications and improvements to suit the specific requirements of PDF2Index. These changes include adding functionalities like custom word inclusion, filtering out common English words, handling specific word indexes, and more. My goal is to enhance the tool's capabilities and tailor it to a broader audience.

I want to emphasize that I do not intend to steal credit or claim this work as entirely my own. I am committed to respecting the principles of open-source development and acknowledge the collaborative nature of such projects. Giving proper credit to the original author is essential, and I sincerely thank them for their valuable contribution to the community. I hope that my modifications will further enrich the usefulness of this tool for users interested in generating indexes for their SANS PDF books.

