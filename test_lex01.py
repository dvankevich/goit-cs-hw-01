from lex01 import Lexer, Parser, Interpreter  # Update this to your module name

def run_tests():
    test_cases = {
        "3 + 5": 8,
        "10 - 2": 8,
        "4 * 7": 28,
        "20 / 4": 5,
        "3 + 4 * 5": 23,
        "10 - 2 + 3": 11,
        "5 * 2 - 3": 7,
        "(3 + 5) * 2": 16,
        "10 - (2 + 3)": 5,
        "4 * (7 - 3)": 16,
        "(8 / 2) + (3 * 5)": 19,
        "((2 + 3) * (4 - 1))": 15,
        "(3 + (2 * 2)) - (5 / 5)": 6,
        "3 + (4 * (5 - 2))": 15,
        "(10 / (2 + 3)) * 4": 8,
        "((2 * 3) + (5 - 1)) / 2": 5,
        "(6 * 3) / 2": 9,
        "18 / (2 * 3)": 3
    }

    for expression, expected in test_cases.items():
        lexer = Lexer(expression)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        assert result == expected, f"Test failed for '{expression}': expected {expected}, got {result}"
        print(f"Test passed for '{expression}': {result}")

if __name__ == '__main__':
    run_tests() 
    
    # python test_interpreter.py