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
            
#fetch_and_print_posts()

def fetch_and_save_posts():
      req = requests.get('https://jsonplaceholder.typicode.com/posts')
      if req.status_code == 200:
            resp = req.json()
      else:
        print(f"Request failed with status: {req.status_code}")