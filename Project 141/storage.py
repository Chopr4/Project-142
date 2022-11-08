from flask import Flask, jsonify, request
import csv
 
# All articles list
all_articles = []
 

# Opening the csv file
with open('articles.csv', "a+") as f:
    # Reading the file
    reader = csv.reader(f) 
    # Storing in data
    data = list(reader)
    #Taking out the first index
    all_articles = data[1: ] 
 
# Creating the other lists for liked, and disliked articles
liked_articles = []
disliked_articles = []