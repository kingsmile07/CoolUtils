# cool_utils.py

import requests
import numpy as np

def cool_function():
    print("This is a cool function!")

def fetch_data(url):
    response = requests.get(url)
    return response.text

def calculate_mean(numbers):
    return np.mean(numbers)
