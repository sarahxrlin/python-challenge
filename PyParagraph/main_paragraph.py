# PyParagraph

# import modules
import csv
import os

# read file
Paragraph = os.path.join('PyParagraph_text.txt')

num_words = 0
sentence_count = 0
num_words = 0

with open(Paragraph, newline='') as txtfile:
#    file1 = txtfile.readlines()
    for line in txtfile:
        sentences = line.split('.')
        words = line.split()
        average_letters = sum((len(word)) for word in words)/(len(words))
 #       avg_words_in_sentence = sum((len(sentence)) for sentence in sentences)/(len(sentences))
        for sentence in sentences:
            words = sentence.split()
            num_words += len(words)
        avg_words_in_sentence1 = num_words/len(sentences)
        sentence_count += len(sentences) - 1
        num_words += len(words)
print("Number of words: " + str(num_words))
print("Number of sentences: " + str(sentence_count))
print("Average letter count: " + str(average_letters))
print("Average Sentence Length: " + str(avg_words_in_sentence1))
#print((len(sentence)) for sentence in sentences)