def calculator():
    print("=== Простой калькулятор ===")
    print("Операции: +, -, *, /, **, %")
    print("Для выхода введите 'q'\n")
    
    while True:
        try:
            expression = input("Введите выражение (например, 2 + 3): ")
            
            if expression.lower() == 'q':
                print("До свидания!")
                break
            
            # Проверка безопасности — разрешаем только цифры и операторы
            allowed = set("0123456789.+-*/%() ")
            if not all(c in allowed for c in expression):
                print("Ошибка: недопустимые символы!\n")
                continue
            
            result = eval(expression)
            print(f"Результат: {result}\n")
        
        except ZeroDivisionError:
            print("Ошибка: деление на ноль!\n")
        except Exception as e:
            print(f"Ошибка: {e}\n")


if __name__ == "__main__":
    calculator()
