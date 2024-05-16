class Calculator:
    def str_to_float(self, num_str):
        try:
            num_float = float(num_str)
            return num_float
        except ValueError:
            print("Помилка: Неможливо конвертувати строку в число.")
            return None
        finally:
            print("Метод str_to_float завершено.")

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            print("Помилка: Поділ на нуль.")
            return None
        finally:
            print("Метод division завершено.")

def main():

    while True:
        calculator = Calculator()
        num_str = input("Введіть число: ")
        num_float = calculator.str_to_float(num_str)
        num1 = num_float
        num_str = input("Введіть число: ")
        num_float = calculator.str_to_float(num_str)
        num2 = num_float
        print("\nЩо хочете зробити?")
        print("1. Додати")
        print("2. Відняти")
        print("3. Перемножити")
        print("4. Поділити")
        print("0. Вихід")

        choice = input("Виберіть дію: ")

        if choice == "1":
            print("Результат додавання: ", calculator.addition(num1, num2))
        elif choice == "2":
            print("Результат выднімання: ", calculator.subtraction(num1, num2))
        elif choice == "3":
            print("Результат множення: ", calculator.multiplication(num1, num2))
        elif choice == "4":
            print("Результат ділення: ",calculator.division(num1, num2))
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Не правільний вибір.")
        #print(f"\nРезультат: {result}")


if __name__ == "__main__":
    main()