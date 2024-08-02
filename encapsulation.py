class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

calc = Calculator(10, 5)

result_addition = calc.add()
result_subtraction = calc.subtract()

print("Addition Result:", result_addition)
print("Subtraction Result:", result_subtraction)

output:-
![Screenshot 2024-08-02 191015](https://github.com/user-attachments/assets/6d69938b-5fa4-4af6-b8f2-ece780e1b3d1)
