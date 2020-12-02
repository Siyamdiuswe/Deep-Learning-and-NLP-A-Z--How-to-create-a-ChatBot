#Importing the libraries
import numpy as np
import tensorflow as tf
import re 
import time

# Preprocessing

#Importing the dataset
lines = open('C:/Users/Siyam/Desktop/github/Deep-Learning-and-NLP-A-Z--How-to-create-a-ChatBot/movie_lines.txt').read().split('\n')
conversations = open('C:/Users/Siyam/Desktop/github/Deep-Learning-and-NLP-A-Z--How-to-create-a-ChatBot/movie_conversations.txt').read().split('\n')

#Creating a library that maps each line and it's id
id2line = {}
for line in lines[:-1]:  #As last row is empty
    _line = line.split(' +++$+++ ')
    id2line[_line[0]] = _line[-1]

# List of conversations
conversations_ids = []
for conversation in conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ", "") # Splitting the conversations, and formatting them to remove [];'';spaces
    conversations_ids.append(_conversation.split(',')) # Formating the large list to consist only the id's in a list
    
#Getting separately the questions and answers
questions = []
answers = []
for conversation in conversations_ids:
    for i in range(len(conversation)-1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])

# Cleaning the text function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"don't", "do not", text)
    text = re.sub(r"can't", "can not", text)
    text = re.sub(r"didn't", "did not", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"[-()\"#/@;:<>+-=~|.,?]", "", text)
    return text


# Cleaning Questions
clean_questions = []
for q in questions:
    clean_questions.append(clean_text(q))


# Cleaning Answers
clean_answers = []
for a in answers:
    clean_answers.append(clean_text(a))
    
#Creating a dictionary that maps each words  to its number of occurances
word2count = {}
for question in clean_questions:
    for word in question.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1

for answer in clean_answers:
    for word in answer.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1
            
#Creating two dictionaries that map the questions words and the answers words
threshold = 20
questionsword2int = {}
word_number = 0
for word, count in word2count.items():
     if count >= threshold:
         questionsword2int[word] = word_number
         word_number += 1

answersword2int = {}
word_number = 0
for word, count in word2count.items():
     if count >= threshold:
         answersword2int[word] = word_number
         word_number += 1
            
#Adding the last tokens to these two dictionaries
tokens = ['<PAD>','<EOS>','<OUT>','<SOS>']
for token in tokens:
    questionsword2int[token]=len(questionsword2int)+1

for token in tokens:
    answersword2int[token] = len(answersword2int)+1
              
print(questionsword2int['<PAD>'])
print(questionsword2int['<EOS>'])
print(questionsword2int['<OUT>'])
print(questionsword2int['<SOS>'])
print("\n")
print(answersword2int['<PAD>'])
print(answersword2int['<EOS>'])
print(answersword2int['<OUT>'])
print(answersword2int['<SOS>'])     
print("OK!")