import sys
import re
from sympy import symbols, Eq, solve, sympify

def print_ascii_art():
    ascii_art = """
  

 /$$      /$$  /$$$$$$  /$$$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$ 
| $$$    /$$$ /$$__  $$|__  $$__/| $$  | $$ /$$__  $$| $$__  $$
| $$$$  /$$$$| $$  \ $$   | $$   | $$  | $$| $$  \ $$| $$  \ $$
| $$ $$/$$ $$| $$$$$$$$   | $$   | $$$$$$$$| $$  | $$| $$$$$$$/
| $$  $$$| $$| $$__  $$   | $$   | $$__  $$| $$  | $$| $$__  $$
| $$\  $ | $$| $$  | $$   | $$   | $$  | $$| $$  | $$| $$  \ $$
| $$ \/  | $$| $$  | $$   | $$   | $$  | $$|  $$$$$$/| $$  | $$
|__/     |__/|__/  |__/   |__/   |__/  |__/ \______/ |__/  |__/
                                                               
                                                               
                                                               

  """
    print(ascii_art)

def print_intro():
    print_ascii_art()
    print("Mathor - Version 1.0")
    print("Créé par AE Corp.")
    print("Code par Abiye Enzo")
    print("Tous droits réservés.\n")

def evaluate_expression(expression):
    try:
        # Convertir l'expression en objet sympy et évaluer
        expr = sympify(expression)
        return expr.evalf()
    except Exception as e:
        return f"Erreur d'évaluation: {e}"

def solve_equation(equation):
    try:
        # Identifier la variable inconnue dans l'équation
        variables = re.findall(r'[a-zA-Z_]\w*', equation)
        if len(variables) != 1:
            return "Erreur: Cette version ne prend en charge qu'une seule variable inconnue."
        
        var_name = variables[0]
        var = symbols(var_name)
        symbols_dict = {var_name: var}

        # Séparer l'équation en deux parties
        lhs, rhs = equation.split('=')
        
        # Créer l'équation SymPy avec la variable trouvée
        lhs_expr = sympify(lhs, locals=symbols_dict)
        rhs_expr = sympify(rhs, locals=symbols_dict)
        eq = Eq(lhs_expr, rhs_expr)
        
        # Résoudre l'équation
        solutions = solve(eq, var)
        
        if len(solutions) == 0:
            return "Pas de solution"
        
        return {var_name: solutions[0]}
    except Exception as e:
        return f"Erreur de résolution: {e}"

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    if '=' in line:
                        result = solve_equation(line)
                        if isinstance(result, dict):
                            result_str = f"{list(result.keys())[0]} = {list(result.values())[0]}"
                            print(f"{line} => {result_str}")
                        else:
                            print(f"{line} => {result}")
                    else:
                        result = evaluate_expression(line)
                        print(f"{line} = {result}")
    except FileNotFoundError:
        print(f"Le fichier {filename} n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")

def interactive_mode():
    print_intro()
    print("Mode interactif activé. Tapez 'exit' pour quitter.")
    while True:
        try:
            line = input(">>> ").strip()
            if line.lower() == 'exit':
                break
            if '=' in line:
                result = solve_equation(line)
                if isinstance(result, dict):
                    result_str = f"{list(result.keys())[0]} = {list(result.values())[0]}"
                    print(f"{line} => {result_str}")
                else:
                    print(f"{line} => {result}")
            else:
                result = evaluate_expression(line)
                print(f"{line} = {result}")
        except Exception as e:
            print(f"Erreur: {e}")

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if filename.endswith(".mth"):
            process_file(filename)
        else:
            print("Le fichier doit avoir l'extension .mth")
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
