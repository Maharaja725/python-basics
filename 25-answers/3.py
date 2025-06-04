# 3. Write a function that accepts keyword arguments for a student's details (name, marks, subject) and prints a formatted report card.
#    Input: name="John", marks=85, subject="Math"
#    Output: "Report Card\nName: John\nSubject: Math\nMarks: 85"

def report_card(name, subject, marks):
    return f"Report Card\nName: {name}\nSubject: {subject}\nMarks: {marks}"

print(report_card("John", "Math", 85))   