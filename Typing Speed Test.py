import customtkinter as ctk
from faker import Faker

font_1 = ("Barlow", 27)

font_2 = ("Mukta", 35, "bold")

font_3 = ("Barlow", 15)

gray = "#242424"

#TODO: Add timer and code explanations
#FIXME: Round the corners of the data

class App(ctk.CTk):
    def __init__(self):
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
        self.typing_speed_test_label.grid(row=0, column=1)

        self.typing_test_label = ctk.CTkLabel(
            self.main_text_frame, text="Test your typing speed", font=font_2, text_color="white")
        self.typing_test_label.grid(row=1, column=1, pady=30)

        self.data_frame = ctk.CTkFrame(
            self, width=500, height=200, fg_color=gray)
        self.data_frame.grid(row=2, column=1, padx=(150, 0), sticky="nsew")

        self.words_per_minute_button = ctk.CTkButton(
            self.data_frame, text="0", font=font_2, text_color="white", bg_color="black", width=50, height=50, corner_radius=50, fg_color="black", border_color="black", hover_color="black", border_spacing=3)
        self.words_per_minute_button.grid(row=2, column=0)

        self.words_per_minute_label = ctk.CTkLabel(
            self.data_frame, text="Words/min", font=font_3, text_color="white", fg_color=gray)
        self.words_per_minute_label.grid(row=3, column=0, pady=5)

        self.chars_per_minute_button = ctk.CTkButton(
            self.data_frame, text="0", font=font_2, text_color="white", bg_color="black", width=50, height=50, corner_radius=50, fg_color="black", border_color="black", hover_color="black", border_spacing=3)
        self.chars_per_minute_button.grid(row=2, column=1, padx=100)

        self.chars_per_minute_label = ctk.CTkLabel(
            self.data_frame, text="Chars/min", font=font_3, text_color="white", fg_color=gray)
        self.chars_per_minute_label.grid(row=3, column=1, pady=5, padx=100)

        self.percent_accuracy_button = ctk.CTkButton(
            self.data_frame, text="0", font=font_2, text_color="white", bg_color="black", width=50, height=50, corner_radius=50, fg_color="black", border_color="black", hover_color="black", border_spacing=3)
        self.percent_accuracy_button.grid(row=2, column=2)

        self.percent_accuracy_label = ctk.CTkLabel(
            self.data_frame, text="% accuracy", font=font_3, text_color="white", fg_color=gray)
        self.percent_accuracy_label.grid(row=3, column=2, pady=5)
        
        

        fake = Faker()
        random_text = fake.text()
        print(random_text)


if __name__ == "__main__":
    app = App()
    app.mainloop()