import tkinter as tk
from consts import *
from BatterySaverbot import BatterySaverBot


class Program:
    def __init__(self):
        self.battery_saver_bot = BatterySaverBot()
        self.root = None
        self.starter = None
        self.current_state = STATES[4]
        self.origin_i = 0
        self.origin_j = 0
        self.destination_i = 0
        self.destination_j = 0
        self.n = 1

        self.mode_handler = tk.Tk()
        self.mode_handler.geometry("250x250")
        self.mode_handler.resizable(False, False)
        self.mode_handler.title("Battery Saver Bot")
        self.mode_handler.configure(background=PRIMARY_COLOR)

        add_new_path_btn = tk.Button(self.mode_handler, text="New Path", command=self.start_normal_mode)
        add_new_path_btn.pack(pady=20)

        read_last_path_btn = tk.Button(self.mode_handler, text="Read Last Path", command=self.reading_last_moves_mode)
        read_last_path_btn.pack(pady=20)
        self.battery_saver_bot.speak("welcome my friend.")
        self.battery_saver_bot.speak("how can I help you?")


    def start_normal_mode(self):
        self.mode_handler.destroy()
        self.starter = tk.Tk()
        self.starter.geometry("500x250")
        self.starter.resizable(False, False)
        self.starter.title("Battery Saver Bot")
        self.starter.configure(background=PRIMARY_COLOR)

        starter_label = tk.Label(self.starter, text="Choose n: ", font=("Arial", 18), bg=PRIMARY_COLOR,
                                 fg=PRIMARY_BG_COLOR)
        starter_label.pack(pady=20)

        value_inside = tk.StringVar(self.starter)
        value_inside.set("select one of them")

        starter_options = tk.OptionMenu(self.starter, value_inside, *options)
        starter_options.pack(pady=30)

        button = tk.Button(self.starter, text="submit", command=lambda: self.submit_handler(value_inside))
        button.pack()

    def reading_last_moves_mode(self):
        self.battery_saver_bot.speak("Alright, let's find your last path")
        self.battery_saver_bot.read_last_file()
        self.battery_saver_bot.speak("finished")

    def submit_handler(self, value_inside):
        if value_inside.get() != "select one of them":
            self.starter.destroy()
            self.n = int(value_inside.get().split()[1])
            self.current_state = STATES[1]
            self.get_position()

    def get_position(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.title("Battery Saver Bot")
        self.root.configure(background=PRIMARY_BG_COLOR)

        if self.current_state == STATES[1]:
            label_container = tk.Label(self.root, text="Select The Origin :", background=PRIMARY_BG_COLOR, fg=TEXT_COLOR)
        elif self.current_state == STATES[2]:
            label_container = tk.Label(self.root, text="Select The Destination :", background=PRIMARY_BG_COLOR, fg=TEXT_COLOR)
        elif self.current_state == STATES[3]:
            label_container = tk.Label(self.root, text="Here Is Your Path :", background=PRIMARY_BG_COLOR, fg=TEXT_COLOR)
        else:
            return
        label_container.pack()

        buttons_container = tk.Frame(self.root, width=490, height=450, bg=PRIMARY_BG_COLOR)
        buttons_container.pack()

        buttons_container.grid_columnconfigure(0, weight=1)
        buttons_container.grid_rowconfigure(0, weight=1)

        if 10 >= self.n >= 8:
            button_width  = int(360 / self.n ** 2)
            button_height = int(200 / self.n ** 2)

        elif 8 > self.n >= 6:
            button_width  = int(250 / self.n ** 2)
            button_height = int(150 / self.n ** 2)


        elif 6 > self.n > 3:
            button_width  = int(200 / self.n ** 2)
            button_height = int(100 / self.n ** 2)

        else:
            button_width  = int(100 / self.n ** 2)
            button_height = int(60 / self.n ** 2)

        for i in range(self.n):
            for j in range(self.n):
                place = [i+1, j+1]
                button = tk.Button(buttons_container, text=f"{i * self.n + j + 1}", width=button_width,
                                   height=button_height, bg=SECONDARY_COLOR, fg=PRIMARY_COLOR, command=lambda i=i, j=j: self.click_handler(i+1, j+1))
                if self.current_state == STATES[2] and j == self.origin_i-1 and i == self.origin_j-1:
                    button.configure(bg=TEXT_COLOR)
                    button["state"] = "disable"

                if self.current_state == STATES[3]:
                    button["state"] = "disable"
                    if place in self.battery_saver_bot.places:
                        button.configure(bg=TEXT_COLOR)

                    if (j == self.origin_i-1 and i == self.origin_j-1) or (j == self.destination_i-1 and i == self.destination_j-1) :
                        button.configure(bg=PRIMARY_COLOR)


                button.grid(row=i, column=j, pady=2, padx=2, sticky='nsew')

        if self.current_state == STATES[1]:
            self.battery_saver_bot.speak("Choose origin:")
        if self.current_state == STATES[2]:
            self.battery_saver_bot.speak("Choose Destination:")
        if self.current_state == STATES[3]:
            self.battery_saver_bot.speak("Here is your path:")

    def click_handler(self, i, j):
        if self.current_state == STATES[1]:
            self.origin_i = j
            self.origin_j = i
            self.root.destroy()
            self.current_state = STATES[2]
            self.get_position()

        elif self.current_state == STATES[2]:
            self.destination_i = j
            self.destination_j = i
            self.battery_saver_bot.find_path(origin_i=self.origin_i, origin_j=self.origin_j, destination_i=self.destination_i, destination_j=self.destination_j)
            self.root.destroy()
            self.current_state = STATES[3]
            self.get_position()
            self.battery_saver_bot.print_moves()


    def run(self):
        self.mode_handler.mainloop()