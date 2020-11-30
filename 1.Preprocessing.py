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
