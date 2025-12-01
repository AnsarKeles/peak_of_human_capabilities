import tkinter as tk
from tkinter import PhotoImage
import pygame
from PIL import Image, ImageTk

pygame.mixer.init()


def play_sound(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)

def stop_sound():
    pygame.mixer.music.stop()

def open_photo_window():
    stop_sound()

    second = tk.Toplevel()
    second.title("Принято")
    second.geometry("400x500")

    img = Image.open("end_screen.jpg")
    img = img.resize((380, 380))
    img_tk = ImageTk.PhotoImage(img)

    label = tk.Label(second, image=img_tk)
    label.image = img_tk
    label.pack(pady=10)

    play_sound("sound1.mp3")

    msg = tk.Label(second, text="Ernar is trying to enter your house!", font=("Arial", 18))
    msg.pack()

def on_click(event):
    x, y = event.x, event.y
    print("Клик:", x, y)  # чтобы видеть точки

    # --- область кнопки 1 ---
    if 13 <= x <= 382 and 123 <= y <= 488:
        open_photo_window()

    # --- область кнопки 2 ---
    if 165 <= x <= 376 and 270 <= y <= 481:
        open_photo_window()

def main_window():
    root = tk.Tk()
    root.title("Входящий звонок")

    # Размер первого окна — такой же как картинка
    root.geometry("300x500")

    # Загружаем картинку
    call_img = Image.open("rasul_drop.jpg")
    call_img = call_img.resize((300, 500))
    call_img_tk = ImageTk.PhotoImage(call_img)

    label = tk.Label(root, image=call_img_tk)
    label.image = call_img_tk
    label.pack()

    play_sound("ios_17_alarm.mp3")

    # Ловим клик
    label.bind("<Button-1>", on_click)

    root.mainloop()

main_window()
