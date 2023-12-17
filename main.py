import numpy as np

## Factors

def factorize(number: int) -> list:
    i = 1
    out = []
    while i <= number:
        rem = np.mod(number, i)
        if rem == 0:
            out.append(i)
        i += 1
    return out

## Chain Rule for Polynomials

def chain(expression: str) -> str:
    new_exp = []
    expression = expression.replace('-', ' - ')
    expression = expression.replace('+', ' + ')
    exp_split = expression.split()
    if exp_split[0] not in ['-', '+']:
        exp_split.insert(0, '+')
    for term in exp_split:
        if term not in ['-', '+']:
            term = term.replace('^', '')
            split = term.split('x')
            if 'x' not in term:
                pass

            if len(split) == 1:
                pass

            else:
                if split[1] == '':
                    new_term = split[0]
                    new_exp.append(new_term)
                else:
                    chain_term = int(split[0]) * int(split[1])
                    new_coef = int(split[1]) - 1
                    new_term = f"{chain_term}x^{new_coef}"
                    new_exp.append(new_term)
        else:
            new_exp.append(term)
    if new_exp[0] == '+':
        new_exp.pop(0)
    if new_exp[-1] in ['+', '-']:
        new_exp.pop(-1)
    
    new_exp = ' '.join(new_exp)
    new_exp = new_exp.replace('x^1 ', 'x ')

    return new_exp 


