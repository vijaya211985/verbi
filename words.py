import streamlit as st
import numpy as np
import pandas as pd
import time
import json
import random

def get_random_word():
    with open('words.json', 'r', encoding='utf-8') as file:
        words = json.load(file)
        random_entry = random.choice(words)
        return random_entry['word'], random_entry['meaning'], random_entry['example']

# Example usage to print a random word, meaning, and example
if __name__ == "__main__":
    random_word, meaning, example = get_random_word()
    print(f"Random Word: {random_word}")
    print(f"Meaning: {meaning}")
    print(f"Example: {example}")
