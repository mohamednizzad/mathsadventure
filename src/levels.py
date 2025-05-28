import random
from dataclasses import dataclass

@dataclass
class Problem:
    num1: int
    num2: int
    operator: str
    answer: int
    
    def __str__(self):
        return f"{self.num1} {self.operator} {self.num2} = ?"

def generate_problem(grade: int) -> Problem:
    """Generate a math problem appropriate for the given grade level"""
    
    if grade == 1:
        # Grade 1: Simple addition and subtraction with numbers 1-10
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-'])
        
        # Ensure subtraction doesn't result in negative numbers
        if operator == '-' and num2 > num1:
            num1, num2 = num2, num1
            
    elif grade == 2:
        # Grade 2: Addition and subtraction with numbers 1-20
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-'])
        
        if operator == '-' and num2 > num1:
            num1, num2 = num2, num1
            
    elif grade == 3:
        # Grade 3: Addition, subtraction with numbers 1-50, and simple multiplication
        num1 = random.randint(1, 50)
        operator = random.choice(['+', '-', '*'])
        
        if operator == '*':
            num2 = random.randint(1, 10)
        else:
            num2 = random.randint(1, 50)
            if operator == '-' and num2 > num1:
                num1, num2 = num2, num1
                
    elif grade == 4:
        # Grade 4: All operations, multiplication with larger numbers
        num1 = random.randint(1, 100)
        operator = random.choice(['+', '-', '*', '/'])
        
        if operator == '*':
            num2 = random.randint(1, 12)
        elif operator == '/':
            # Generate division problems with whole number answers
            num2 = random.randint(1, 12)
            num1 = num2 * random.randint(1, 10)
        else:
            num2 = random.randint(1, 100)
            if operator == '-' and num2 > num1:
                num1, num2 = num2, num1
                
    else:  # grade 5
        # Grade 5: Larger numbers and more complex operations
        num1 = random.randint(1, 200)
        operator = random.choice(['+', '-', '*', '/'])
        
        if operator == '*':
            num2 = random.randint(2, 15)
        elif operator == '/':
            num2 = random.randint(2, 15)
            num1 = num2 * random.randint(1, 20)
        else:
            num2 = random.randint(1, 200)
            if operator == '-' and num2 > num1:
                num1, num2 = num2, num1
    
    # Calculate answer
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:  # operator == '/'
        answer = num1 // num2
    
    return Problem(num1, num2, operator, answer)