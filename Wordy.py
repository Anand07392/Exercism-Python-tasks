import re
def answer(question):
    operation_patterns = {
        'plus': '+',
        'minus': '-',
        'multiplied by': '*',
        'divided by': '/',
    }
    question = question.lower().strip()    
    if not question.startswith("what is") or not question.endswith("?"):
        raise ValueError("unknown operation")    
    question = question[8:-1].strip()  
    if re.fullmatch(r'-?\d+', question):
        return int(question)  
    for word in question.split():
        if word not in ['plus', 'minus', 'multiplied', 'by', 'divided'] and not re.fullmatch(r'-?\d+', word):
            raise ValueError("unknown operation")
    for verbal, symbol in operation_patterns.items():
        question = question.replace(verbal, symbol)   
    if not re.fullmatch(r'(-?\d+(\s*[\+\-\*/]\s*-?\d+)+)', question):
        raise ValueError("syntax error")  
    tokens = re.split(r'\s+', question)
    try:
        result = int(tokens[0])
        index = 1
        while index < len(tokens):
            operator = tokens[index]
            operand = int(tokens[index + 1])
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            elif operator == '/':
                result //= operand
            else:
                raise ValueError("unknown operation")
            index += 2
    except (ValueError, IndexError):
        raise ValueError("syntax error")    
    return result    
    if not re.fullmatch(r'(-?\d+(\s*[\+\-\*/]\s*-?\d+)+)', question):
        raise ValueError("syntax error")    
    tokens = re.split(r'\s+', question)
    try:
        result = int(tokens[0])
        index = 1
        while index < len(tokens):
            operator = tokens[index]
            operand = int(tokens[index + 1])
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            elif operator == '/':
                result //= operand
            else:
                raise ValueError("unknown operation")
            index += 2
    except (ValueError, IndexError):
        raise ValueError("syntax error") 
    return result
