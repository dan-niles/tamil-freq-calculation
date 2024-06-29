# Tamil Word Frequency Analysis

This repository includes a Python script that performs word frequency analysis on a given text in the Tamil language. It counts the occurrences of each word, calculates the frequency of these frequencies, and ranks the words based on their frequency. The results are then written to CSV files for easy analysis and visualization.

## Features

- **Word Frequency Count**: Counts how many times each word appears in the text.
- **Frequency of Frequencies Calculation**: Determines how many words have the same frequency.
- **Ranking of Words**: Ranks words based on their frequency in descending order.

## Output Files

The script generates three CSV files:

1. **Frq.csv**: Contains each word and its frequency.
2. **FrFr.csv**: Contains each frequency and how many words have that frequency.
3. **Rank.csv**: Contains words ranked by frequency, along with their frequency and rank.

## Requirements

- Python 3.x
- `nltk` module

## Usage

1. Ensure you have Python installed on your system.
2. Place the script in the directory containing your text file(s).
3. Modify the script to point to your specific text file(s) by setting the appropriate file path variables.
4. Run the script:
   ```bash
   python script.py
   ```
