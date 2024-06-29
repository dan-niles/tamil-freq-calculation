import nltk
import csv
import string

import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from collections import defaultdict, Counter

nltk.download("punkt")
nltk.download("wordnet")

INPUT_FILE = "data/input/21339_Tamil.txt"
OUTPUT_FRQ_FILE = "data/output/Frq.csv"
OUTPUT_FRFR_FILE = "data/output/FrFr.csv"
OUTPUT_RANK_FILE = "data/output/Rank.csv"
OUTPUT_GRAPH_FILE = "data/output/Graph.png"

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
normalized_words = (
    lemmatizer.lemmatize(word)
    for word in words
    if not all(char in string.punctuation for char in word)  # Remove punctuation
)
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

# Calculate the frequency of frequencies
freq_of_freq = Counter(word_freq.values())

# Write the frequency of frequencies to a CSV file
with open(OUTPUT_FRFR_FILE, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Freq", "FreqOfFreq"])
    writer.writerows(freq_of_freq.items())
print("Output written to FrFr.csv file successfully.")

# Sort the words by frequency in descending order
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Write the ranked words to Rank.csv
with open(OUTPUT_RANK_FILE, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Word", "Freq", "Rank"])
    for rank, (word, freq) in enumerate(sorted_word_freq, start=1):
        writer.writerow([word, freq, rank])
print("Output written to Rank.csv file successfully.")

# Extract ranks and frequencies for plotting
ranks = list(range(1, len(sorted_word_freq) + 1))
frequencies = [freq for word, freq in sorted_word_freq]

# Plotting rank vs frequency
plt.figure(figsize=(10, 6))
plt.plot(
    ranks,
    frequencies,
    marker="o",
    linestyle="-",
    color="b",
    label="Word Frequency",
    markersize=3,
)

plt.yscale("log")  # Logarithmic scale for better visualization of frequencies

plt.title("Rank vs Frequency of Words")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.legend()

# Save the plot to Graph.png
plt.savefig(OUTPUT_GRAPH_FILE)
plt.show()
