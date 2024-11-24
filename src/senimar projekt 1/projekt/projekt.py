import os
import random
import time
from datetime import datetime

QUESTIONS_FILE = "test_questions"
ANSWERS_FILE = "test_answers"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

GRADING= {        
    1: (90, 100),
    2: (75, 90),
    3: (60, 75),
    4: (45, 60),
    5: (0, 45)
}

def parse_and_and_questions(author, filename):
    questions = []
    try:
        with open(QUESTIONS_FILE, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            blocks = content.split("**Otázka:**")
            for block in blocks[1:]:  
                lines = block.strip().split("\n")
                question_text = lines[0].strip()
                answers = [line.strip() for line in lines[1:]]
                questions.append({"question": question_text, 
                                  "answers": answers, 
                                  "author": author, 
                                  "correct_answer": next(i for i, line in enumerate(lines[1:5]) if line.startswith("1;")), 
                                  "file": filename}
                                  )
    except Exception as e:
        print(f"Error reading file: {e}")
    return questions
        
def shuffle_questions(questions):
    question = questions["question"]
    answers = questions["answers"]
    correct_answer = questions["correct_answer"]
    indices = list(range(len(answers)))
    random.shuffle(indices)
    shuffled_answers = [answers[i] for i in indices]
    new_correct_answer = indices.index(correct_answer)
    question['answers'] = shuffled_answers
    question['correct_answer'] = new_correct_answer
    return question

def get_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return first_name, last_name

def get_number_of_questions(total_questions):
    while True:
        try:
            number_of_questions = int(input(f"Enter number of questions(min.1 max.{total_questions})"))
            if 0 < number_of_questions < total_questions:
                return number_of_questions
            else:
                print(f"Please enter valid number between 1-{total_questions}.")
        except ValueError:
            print("Enter a valid number.")
    
