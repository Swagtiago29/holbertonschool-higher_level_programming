#!/usr/bin/env python3
import requests
import csv

def fetch_and_print_posts():
      req = requests.get('https://jsonplaceholder.typicode.com/posts')
      print(f"Status Code: {req.status_code}")
      if req.status_code == 200:
            resp = req.json()
            for posts in resp:
                  print(posts['title'])
            
def fetch_and_save_posts():
      req = requests.get('https://jsonplaceholder.typicode.com/posts')
      if req.status_code == 200:
            resp = req.json()
            posts = []
            for data in resp:
                  cositas = {'id': data['id'], 'title': data['title'], 'body': data['body']}
                  posts.append(cositas)
            with open('posts.csv', mode='w', newline='', encoding='utf-8') as f:
                  writer = csv.DictWriter(f,['id', 'title', 'body'])
                  writer.writeheader()
                  writer.writerows(posts)
      else:
        print(f"Failed with status: {req.status_code}")
