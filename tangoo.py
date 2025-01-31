# -*- coding: utf-8 -*-
"""tangoo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/A-Yuki-A/48f8642709f70ca10edaa04c66fbab0c/tango.ipynb
"""

import tkinter as tk
import random

# 単語リストと意味
words = [
    ("Apple", "リンゴ"),
    ("Banana", "バナナ"),
    ("Cat", "ネコ"),
    ("Dog", "イヌ"),
    ("Elephant", "ゾウ"),
    ("Fish", "サカナ"),
    ("Grape", "ブドウ"),
    ("House", "イエ"),
    ("Ice", "コオリ"),
    ("Juice", "ジュース")
]

# 単語と意味を表示するためのラベル
class Flashcard:
    def __init__(self, master, word, meaning):
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)
        self.label = tk.Label(self.frame, text=word, font=("Arial", 24), width=10, height=2)
        self.label.pack()
        self.word = word
        self.meaning = meaning
        self.showing_word = True
        self.label.bind("<Button-1>", self.flip)

    def flip(self, event):
        if self.showing_word:
            self.label.config(text=self.meaning)
        else:
            self.label.config(text=self.word)
        self.showing_word = not self.showing_word

# シャッフル機能
def shuffle():
    random.shuffle(flashcards)
    for flashcard in flashcards:
        flashcard.frame.pack_forget()
        flashcard.frame.pack(pady=10)

# アプリのメインウィンドウ
root = tk.Tk()
root.title("単語アプリ")

flashcards = [Flashcard(root, word, meaning) for word, meaning in words]

shuffle_button = tk.Button(root, text="シャッフル", command=shuffle)
shuffle_button.pack(pady=20)

root.mainloop()