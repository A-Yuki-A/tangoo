# tangoo
import ipywidgets as widgets
from IPython.display import display
import random

# サンプルデータ
words = [
    {"word": "apple", "meaning": "A fruit", "importance": 5, "learned": False},
    {"word": "banana", "meaning": "Another fruit", "importance": 3, "learned": False},
    {"word": "cat", "meaning": "A small animal", "importance": 4, "learned": False},
    {"word": "dog", "meaning": "A domesticated animal", "importance": 2, "learned": False},
    {"word": "elephant", "meaning": "A large animal", "importance": 1, "learned": False},
]

# 単語と意味を切り替える関数
def toggle_word_meaning(button, word):
    if button.description == word["word"]:
        button.description = word["meaning"]
    else:
        button.description = word["word"]

# 単語を覚えたとマークする関数
def mark_as_learned(word):
    word["learned"] = True
    display_all()

# 単語帳の表示（タップで意味を表示）
def display_words(word_list):
    for word in word_list:
        if not word["learned"]:
            word_button = widgets.Button(description=word["word"])
            word_button.on_click(lambda b, wd=word: toggle_word_meaning(b, wd))
            display(word_button)
            learned_button = widgets.Button(description="Mark as learned")
            learned_button.on_click(lambda b, wd=word: mark_as_learned(wd))
            display(learned_button)

# アルファベット順に並び替え
def sort_alphabetically():
    words_sorted = sorted(words, key=lambda x: x["word"])
    display_all(words_sorted)

# ランダム順に並び替え
def sort_randomly():
    words_sorted = random.sample(words, len(words))
    display_all(words_sorted)

# 単語帳の表示
def display_all(word_list=words):
    display(widgets.HTML("<h2>Word List</h2>"))
    display_words(word_list)
    display(sort_alpha_button)
    display(sort_random_button)

# 並び替えボタン
sort_alpha_button = widgets.Button(description="Sort Alphabetically")
sort_alpha_button.on_click(lambda b: sort_alphabetically())

sort_random_button = widgets.Button(description="Sort Randomly")
sort_random_button.on_click(lambda b: sort_randomly())

# 初期表示
display_all()
