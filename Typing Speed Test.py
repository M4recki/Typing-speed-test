import customtkinter as ctk
from faker import Faker
import threading

font_1 = ("Barlow", 27)

font_2 = ("Mukta", 35, "bold")

font_3 = ("Barlow", 15)

gray = "#242424"

# TODO: Add code explanations


class App(ctk.CTk):
    def __init__(self):

        def generate_random_sentence(self):
            fake = Faker()
            random_text = fake.text()
            return random_text

        def start_timer(self):
            if self.seconds > 0:
                self.seconds -= 1
                self.time_counter_label["text"] = str(self.seconds)
                self.time_counter_label.after(1000, self.start_timer)
            else:
                self.writing_area_entry.config(state="disabled")
                self.analyze_data()

        def count_words_per_minute(self, time_elapsed, typed_text):
            words = typed_text.split()
            words_per_minute = len(words) / (time_elapsed / 60)
            return words_per_minute

        def count_chars_per_minute(self, time_elapsed, typed_text):
            chars_per_minute = len(typed_text) / (time_elapsed / 60)
            return chars_per_minute

        def calculate_accuracy(typed_text, original_text):
            typed_chars = list(typed_text)
            original_chars = list(original_text)
            errors = 0
            for i in range(len(typed_chars)):
                if typed_chars[i] != original_chars[i]:
                    errors += 1
            accuracy = ((len(typed_chars) - errors) / len(typed_chars)) * 100
            return accuracy

        def start_analyzing_data(self):
            if not threading.enumerate():
                elapsed_time = 60 - self.seconds
                self.words = count_words_per_minute(
                    elapsed_time, self.writing_area_entry.get())
                self.characters = count_chars_per_minute(
                    elapsed_time, self.writing_area_entry.get())
                self.accuracy = calculate_accuracy(
                    self.writing_area_entry.get(), self.random_sentence)
                self.words_per_minute_button["text"] = f"{self.words:.2f}"
                self.chars_per_minute_button["text"] = f"{self.characters:.2f}"
                self.accuracy_button["text"] = f"{self.accuracy:.2f}%"

        # Attributes
        self.words = 0
        self.characters = 0
        self.accuracy = 0
        self.seconds = 60
        self.random_sentence = generate_random_sentence(self)

        # Window settings
        super().__init__()
        self.geometry("700x700")
        self.title("Typing speed test by Marek Baranski")
        self.iconbitmap("typing.ico")

        self.main_text_frame = ctk.CTkFrame(
            self, width=500, height=200, fg_color=gray)
        self.main_text_frame.grid(
            row=0, column=1, pady=25, sticky="e")

        self.typing_speed_test_label = ctk.CTkLabel(
            self.main_text_frame, text="Typing speed test", font=font_1, text_color="grey")
        self.typing_speed_test_label.grid(row=0, column=1, padx=(0, 50))

        self.typing_test_label = ctk.CTkLabel(
            self.main_text_frame, text="Test your typing speed", font=font_2, text_color="white")
        self.typing_test_label.grid(row=1, column=1, pady=30, padx=(0, 50))

        self.data_frame = ctk.CTkFrame(
            self, width=500, height=200, fg_color=gray)
        self.data_frame.grid(row=2, column=1, padx=(125, 0), sticky="nsew")

        self.words_per_minute_button = ctk.CTkButton(
            self.data_frame, text=f"{self.words}", font=font_2, text_color="white", width=70, height=50, corner_radius=10, fg_color="black", hover_color="black", border_spacing=3)
        self.words_per_minute_button.grid(row=2, column=0)

        self.words_per_minute_label = ctk.CTkLabel(
            self.data_frame, text="Words/min", font=font_3, text_color="white", fg_color=gray)
        self.words_per_minute_label.grid(row=3, column=0, pady=5)

        self.chars_per_minute_button = ctk.CTkButton(
            self.data_frame, text=f"{self.characters}", font=font_2, text_color="white", width=70, height=50, corner_radius=10, fg_color="black", hover_color="black", border_spacing=3)
        self.chars_per_minute_button.grid(row=2, column=1, padx=100)

        self.chars_per_minute_label = ctk.CTkLabel(
            self.data_frame, text="Chars/min", font=font_3, text_color="white", fg_color=gray)
        self.chars_per_minute_label.grid(row=3, column=1, pady=5, padx=100)

        self.percent_accuracy_button = ctk.CTkButton(
            self.data_frame, text=f"{self.accuracy}", font=font_2, text_color="white", width=70, height=50, corner_radius=10, fg_color="black", border_color="black", hover_color="black", border_spacing=3)
        self.percent_accuracy_button.grid(row=2, column=2)

        self.percent_accuracy_label = ctk.CTkLabel(
            self.data_frame, text="% accuracy", font=font_3, text_color="white", fg_color=gray)
        self.percent_accuracy_label.grid(row=3, column=2, pady=5)

        self.time_border_label = ctk.CTkButton(self.data_frame, text="", width=120, height=95,
                                               bg_color=gray, hover_color="#E04E01", corner_radius=100, fg_color="#E04D01", border_color=gray)
        self.time_border_label.grid(row=4, column=1, pady=30, padx=100)

        self.time_counter_label = ctk.CTkButton(
            self.data_frame, text=self.seconds, font=font_2, text_color="white", width=1, height=60, corner_radius=100, fg_color="black", hover_color="black", border_spacing=4, bg_color="#E04D01")
        self.time_counter_label.grid(row=4, column=1, pady=30, padx=100)

        self.seconds_label = ctk.CTkLabel(
            self.data_frame, text="Seconds", font=font_3, text_color="white", fg_color=gray)
        self.seconds_label.grid(row=4, column=1, pady=(130, 0), padx=100)

        self.writing_area_frame = ctk.CTkFrame(
            self, width=500, height=200, fg_color=gray)
        self.writing_area_frame.grid(
            row=5, column=1, padx=(125, 0), sticky="nsew")

        self.writing_area_entry = ctk.CTkEntry(
            self.writing_area_frame, width=450, height=200, fg_color="#4e4e4e", corner_radius=10)
        self.writing_area_entry.grid(
            row=5, column=1, pady=25, padx=0, sticky="w")
        self.writing_area_entry.bind(
            "<KeyRelease>", lambda event: self.start_analyzing_data(self))
        self.writing_area_entry.bind(
            "<KeyRelease>", lambda event: self.start_timer(self))

        self.sentence_label = ctk.CTkLabel(
            self.writing_area_frame, text=self.random_sentence, font=font_3, fg_color="#4e4e4e", text_color="#E04D01", justify="center", wraplength=445)
        self.sentence_label.grid(
            row=5, column=1, padx=15, pady=30, sticky="nw")


if __name__ == "__main__":
    app = App()
    app.mainloop()
