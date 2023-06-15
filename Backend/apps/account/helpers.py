import random
from datetime import datetime


def generate_student_number():
    current_year = datetime.now().year
    student_number = str(current_year) + ''.join(random.choices('0123456789', k=9))
    return student_number[:11]
