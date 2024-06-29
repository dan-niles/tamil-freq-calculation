import nltk
import csv

from nltk.stem import WordNetLemmatizer
from collections import defaultdict, Counter

nltk.download("punkt")
nltk.download("wordnet")

INPUT_FILE = "data/input/21339_Tamil.txt"
OUTPUT_FRQ_FILE = "data/output/Frq.csv"

with open(INPUT_FILE, "r") as f:
    text = f.read()
print("File read successfully.")

# Tokenize the text using nltk
words = nltk.word_tokenize(text)
print("Text tokenized successfully.")

# Initialize the WordNetLemmatizer for Tamil
lemmatizer = WordNetLemmatizer()
print("Lemmatizer initialized successfully.")

# Normalize and lemmatize the words
normalized_words = (lemmatizer.lemmatize(word) for word in words)
print("Words normalized and lemmatized successfully.")

# Count the frequencies using a defaultdict
word_freq = defaultdict(int)
for word in normalized_words:
    word_freq[word] += 1
print("Word frequencies counted successfully.")

# Write the output to a CSV file
with open(OUTPUT_FRQ_FILE, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Word", "Freq"])
    writer.writerows(word_freq.items())
print("Output written to CSV file successfully.")
