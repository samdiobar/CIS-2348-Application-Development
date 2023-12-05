# Name: Samuel Barroso
# PSID: 1844307

if __name__ == "__main__":
    inputs = []
    for i in range(0,2):
        try:
            user_input = input()
            to_int = int(user_input)
            inputs.append(to_int)
        except ValueError:
            print(f'Input Exception: invalid literal for int() with base 10: \'{user_input}\'')

    try:
        quotient = inputs[0] / inputs[1]
        print(f'{quotient:g}')
    except ZeroDivisionError:
        print("Zero Division Exception: integer division or modulo by zero")
    except:
        pass