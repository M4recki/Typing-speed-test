import customtkinter as ctk
from faker import Faker
from threading import Thread
from time import sleep

# TODO: Add final score window

# Fonts
font_1 = ("Barlow", 27)
font_2 = ("Mukta", 35, "bold")
font_3 = ("Barlow", 15)

# Main color
gray = "#242424"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Generate random sentence
        def generate_random_sentence():
            fake = Faker()
            random_text = fake.text()
            return random_text

        # Attributes
        self.words = 0
        self.characters = 0
        self.accuracy = 0
        self.seconds = 60
        self.random_sentence = generate_random_sentence()
        self.running = False

        # Starting a multi-threaded task
        def start_timer(event=None):
            if not self.running:
                self.running = True
                parallel_task = Thread(target=count_down_and_analyze_data)
                parallel_task.start()

        # Counting down time and collecting data on the user's typing
        def count_down_and_analyze_data():
            # Counting down time
            for i in range(60):
                self.seconds -= 1
                self.time_counter_label.configure(text=self.seconds)
                sleep(1)
                i += 1
                
                # Collecting data on the user's typing (words, characters, accuracy)
                elapsed_time = 60 - self.seconds
                typed_text = self.writing_area_entry.get()
                
                words_per_minute = int(
                    len(typed_text.split()) / (elapsed_time / 60))
                
                chars_per_minute = int(len(typed_text) / (elapsed_time / 60))
                
                typed_chars = list(typed_text.strip())
                
                original_chars = list(self.random_sentence.strip())
                
                errors = 0
                
                # Counting effectiveness
                for typed_char, original_char in zip(typed_chars, original_chars):
                    if typed_char.strip() != original_char.strip():
                        errors += 1
                        
                accuracy = round(((len(original_chars) - errors) / len(original_chars)) * 100)
                
                # Display data
                self.words_per_minute_button.configure(text=str(words_per_minute))
                self.chars_per_minute_button.configure(text=str(chars_per_minute))
                self.percent_accuracy_button.configure(text=str(accuracy))


        # Window settings
        self.geometry("700x700")
        self.title("Typing speed test by Marek Baranski")
        self.iconbitmap("typing.ico")

        # Main frame
        self.main_text_frame = ctk.CTkFrame(
            self, width=500, height=200, fg_color=gray)
        self.main_text_frame.grid(
            row=0, column=1, pady=25, sticky="e")

        # Main texts
        self.typing_speed_test_label = ctk.CTkLabel(
            self.main_text_frame, text="Typing speed test", font=font_1, text_color="grey")
        self.typing_speed_test_label.grid(row=0, column=1, padx=(0, 50))

        self.typing_test_label = ctk.CTkLabel(
            self.main_text_frame, text="Test your typing speed", font=font_2, text_color="white")
        self.typing_test_label.grid(row=1, column=1, pady=30, padx=(0, 50))

        # Section showing user typing data
        self.data_frame = ctk.CTkFrame(
            self, width=500, height=200, fg_color=gray)
        self.data_frame.grid(row=2, column=1, padx=(125, 0), sticky="nsew")

        # Words per minute
        self.words_per_minute_button = ctk.CTkButton(
            self.data_frame, text=f"{self.words}", font=font_2, text_color="white", width=70, height=50, corner_radius=10, fg_color="black", hover_color="black", border_spacing=3)
        self.words_per_minute_button.grid(row=2, column=0)

        self.words_per_minute_label = ctk.CTkLabel(
            self.data_frame, text="Words/min", font=font_3, text_color="white", fg_color=gray)
        self.words_per_minute_label.grid(row=3, column=0, pady=5)

        # Characters per minute
        self.chars_per_minute_button = ctk.CTkButton(
            self.data_frame, text=f"{self.characters}", font=font_2, text_color="white", width=70, height=50, corner_radius=10, fg_color="black", hover_color="black", border_spacing=3)
        self.chars_per_minute_button.grid(row=2, column=1, padx=100)

        self.chars_per_minute_label = ctk.CTkLabel(
            self.data_frame, text="Chars/min", font=font_3, text_color="white", fg_color=gray)
        self.chars_per_minute_label.grid(row=3, column=1, pady=5, padx=100)

        # % Accuracy data
        self.percent_accuracy_button = ctk.CTkButton(
            self.data_frame, text=f"{self.accuracy}", font=font_2, text_color="white", width=70, height=50, corner_radius=10, fg_color="black", border_color="black", hover_color="black", border_spacing=3)
        self.percent_accuracy_button.grid(row=2, column=2)

        self.percent_accuracy_label = ctk.CTkLabel(
            self.data_frame, text="% accuracy", font=font_3, text_color="white", fg_color=gray)
        self.percent_accuracy_label.grid(row=3, column=2, pady=5)

        # Timer
        self.time_border_label = ctk.CTkButton(self.data_frame, text="", width=120, height=95,
                                               bg_color=gray, hover_color="#E04E01", corner_radius=100, fg_color="#E04D01", border_color=gray)
        self.time_border_label.grid(row=4, column=1, pady=30, padx=100)

        self.time_counter_label = ctk.CTkButton(
            self.data_frame, text=self.seconds, font=font_2, text_color="white", width=1, height=60, corner_radius=100, fg_color="black", hover_color="black", border_spacing=4, bg_color="#E04D01")
        self.time_counter_label.grid(row=4, column=1, pady=30, padx=100)

        self.seconds_label = ctk.CTkLabel(
            self.data_frame, text="Seconds", font=font_3, text_color="white", fg_color=gray)
        self.seconds_label.grid(row=4, column=1, pady=(130, 0), padx=100)

        # Writing area
        self.writing_area_frame = ctk.CTkFrame(
            self, width=500, height=200, fg_color=gray)
        self.writing_area_frame.grid(
            row=5, column=1, padx=(125, 0), sticky="nsew")

        self.writing_area_entry = ctk.CTkEntry(
            self.writing_area_frame, width=450, height=200, fg_color="#4e4e4e", corner_radius=10)
        self.writing_area_entry.grid(
            row=5, column=1, pady=25, padx=0, sticky="w")
        self.writing_area_entry.bind(
            "<KeyRelease>", start_timer)

        # Random sentence
        self.sentence_label = ctk.CTkLabel(
            self.writing_area_frame, text=self.random_sentence, font=font_3, fg_color="#4e4e4e", text_color="#E04D01", justify="center", wraplength=430)
        self.sentence_label.grid(
            row=5, column=1, padx=15, pady=30, sticky="nw")


if __name__ == "__main__":
    app = App()
    app.mainloop()
