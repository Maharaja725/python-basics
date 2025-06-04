# 3. Write a function that accepts keyword arguments for a student's details (name, marks, subject) and prints a formatted report card.
def report_card(**kwargs):
    return f"Report Card\nName: {kwargs['name']}\nSubject: {kwargs['subject']}\nMarks: {kwargs['marks']}"

print(report_card(name="John", marks=85, subject="Math"))  
# Output:
# Report Card
# Name: John
# Subject: Math
# Marks: 85