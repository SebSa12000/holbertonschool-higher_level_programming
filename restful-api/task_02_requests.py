#!/usr/bin/python3
'''
    Requests from serveur
'''


import requests
import csv 


def fetch_and_print_posts():
    '''
    def fetch_and_print_posts():
    '''
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: " + str(req.status_code))
    if req.status_code == 200:
        post = req.json()
        for tab in post:
            print(tab['title'])

def fetch_and_save_posts():
    '''
    fetch_and_save_posts
    '''
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    if req.status_code == 200:
        post = req.json()
        with open("posts.csv", "w") as file:
            wr = csv.writer(file, dialect='excel')       
            for tab in post:
                data = []
                data.append(tab['id'])
                data.append(tab['title'])
                data.append(tab['body'])
                wr.writerow(data)
                
    