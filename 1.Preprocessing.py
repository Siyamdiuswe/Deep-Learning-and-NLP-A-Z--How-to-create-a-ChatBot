#Importing the libraries
import numpy as np
import tensorflow as tf
import re 
import time

# Preprocessing

#Importing the dataset
lines = open('movie_lines.txt').read().split('\n')
conversations = open('movie_conversations.txt').read().split('\n')

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