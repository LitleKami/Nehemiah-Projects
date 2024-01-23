from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score_text = Label()
        self.score_text.config(text=f"Score:{self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Questions!!",
            font=("Arial", 20, "italic"),
            fill="black"
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.false_button = Button()
        false_img = PhotoImage(file="images/false.png")
        self.false_button.config(image=false_img, highlightthickness=0, command=self.false_butt)
        self.false_button.grid(row=2, column=0)
        self.true_button = Button()
        true_img = PhotoImage(file="images/true.png")
        self.true_button.config(image=true_img, highlightthickness=0, command=self.true_butt)
        self.true_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_butt(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_butt(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
