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
    json = req.json()
    filednames = ["id", "title", "body"]

    if req.status_code == 200:
        with open('posts.csv', 'w', encoding='utf-8') as csv_file:
            new_csv = csv.DictWriter(csv_file, fieldnames=filednames)
            new_csv.writeheader()
            fetch_titles = [{"id": value['id'],
                             'title': value['title'],
                             'body': value['body']} for value in json]
            new_csv.writerows(fetch_titles)
                
    