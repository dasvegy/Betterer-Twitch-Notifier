import tkinter as tk
import os

from functions.config import load_config
from functions.load_streamer_file import check_file_no_empty
from functions.logging import logger
from functions.loop import run_checker_loop
from functions.tray import run_tray
from functions.tui import tui
from functions.variables import name, version_number

WINDOW_RESOLUTION = "320x480"

TitleFont = ("Iosevka", 14)
NormalFont = ("Iosevka", 12)
SmallFont = ("Iosevka", 10)

BACKGROUND_COLOR = "#101010"
FORCEGROUND_COLOR = "#d1d1d1"

BLUE = "#101010"
RED = "#D43333"
GREEN = "#33D44E"

button_style = {
    'font': NormalFont,
    'background': BACKGROUND_COLOR,
    'foreground': FORCEGROUND_COLOR,
    'activebackground': RED,
    'highlightthickness': 0,
    'border': 0,
    'width': 100,
    'anchor': "w"
}

button_theme_wide_style = {
    'font': NormalFont,
    'background': BACKGROUND_COLOR,
    'foreground': FORCEGROUND_COLOR,
    'activebackground': RED,
    'highlightthickness': 0,
    'border': 0,
    'height': 2,
    'width': 22,
}

label_style = {'bg': BACKGROUND_COLOR,
               'foreground': FORCEGROUND_COLOR,
               'font': NormalFont
               }

title_style = {'bg': BACKGROUND_COLOR,
               'foreground': FORCEGROUND_COLOR,
               'font': TitleFont
               }

config = load_config()


class MainWindow(tk.Tk):

    async def async_main(self, config):
        print(f"{Colors.bold}{Colors.green}Starting the loop{Colors.reset}\n")
        check_file_no_empty()
        await run_checker_loop(config["interval_minutes"])

    def change_color_on_hover(self, event):
        event.widget.config(background=RED, foreground=BACKGROUND_COLOR)

    def restore_color_on_hover(self, event):
        event.widget.config(background=BACKGROUND_COLOR, foreground=FORCEGROUND_COLOR)

    def main_page(self):
        self.main_frame = tk.Frame(self.root, background=BACKGROUND_COLOR)

        self.CheckBtn = tk.Button(self.main_frame,
                                  text="Check Streamers in the list",
                                  command=lambda: run_checker_loop(config["interval_minutes"]),
                                  **button_style)
        self.CheckBtn.pack(side=tk.TOP, padx=5, pady=1)
        self.CheckBtn.bind("<Enter>", self.change_color_on_hover)
        self.CheckBtn.bind("<Leave>", self.restore_color_on_hover)

        self.AddBtn = tk.Button(self.main_frame,
                                text="Add Streamers to the list",
                                command=lambda: print("2"),
                                **button_style)
        self.AddBtn.pack(side=tk.TOP, padx=5, pady=1)
        self.AddBtn.bind("<Enter>", self.change_color_on_hover)
        self.AddBtn.bind("<Leave>", self.restore_color_on_hover)

        self.RemoveBtn = tk.Button(self.main_frame,
                                   text="Remove Streamers from the list",
                                   command=lambda: print("3"),
                                   **button_style)
        self.RemoveBtn.pack(side=tk.TOP, padx=5, pady=1)
        self.RemoveBtn.bind("<Enter>", self.change_color_on_hover)
        self.RemoveBtn.bind("<Leave>", self.restore_color_on_hover)

        self.ClearBtn = tk.Button(self.main_frame,
                                  text="Clear the Streamers list",
                                  command=lambda: print("4"),
                                  **button_style)
        self.ClearBtn.pack(side=tk.TOP, padx=5, pady=1)
        self.ClearBtn.bind("<Enter>", self.change_color_on_hover)
        self.ClearBtn.bind("<Leave>", self.restore_color_on_hover)

        self.SettingsBtn = tk.Button(self.main_frame,
                                     text="Settings",
                                     command=lambda: print("settings placeholder 🦕"),
                                     **button_style)
        self.SettingsBtn.pack(side=tk.TOP, padx=5, pady=1)
        self.SettingsBtn.bind("<Enter>", self.change_color_on_hover)
        self.SettingsBtn.bind("<Leave>", self.restore_color_on_hover)

        self.main_frame.pack(pady=5, side=tk.TOP)

    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.geometry(WINDOW_RESOLUTION)
        self.root.title("Betterer Twitch Notifier")
        self.root.resizable(False, False)
        self.root.configure(background=BACKGROUND_COLOR)
        self.icon = tk.PhotoImage(file="./icon.png")
        self.iconphoto(False, self.icon)

        self.title_label = tk.Label(self.root,
                                    text="Betterer Twitch Notifier",
                                    font=TitleFont,
                                    foreground=FORCEGROUND_COLOR,
                                    background=BACKGROUND_COLOR)
        self.title_label.pack(padx=4, pady=4, side=tk.TOP)

        self.quit_btn_frame = tk.Frame(self.root, background=BACKGROUND_COLOR)
        self.quit_btn_frame.pack(pady=15, side=tk.BOTTOM)

        self.QuitBtn = tk.Button(self.quit_btn_frame,
                                 text="Quit",
                                 command=quit,
                                 **button_style)
        self.QuitBtn.pack(side=tk.RIGHT, padx=5)
        self.QuitBtn.bind("<Enter>", self.change_color_on_hover)
        self.QuitBtn.bind("<Leave>", self.restore_color_on_hover)

        self.main_page()

        self.root.mainloop()


MainWindow()
