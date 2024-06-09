def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero" 
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["", "thousand", "million", "billion", "trillion"]

    def two_digit_number_to_words(n):
        if n < 10:
            return ones[n]
        elif 10 < n < 20:
            return teens[n - 10]
        elif n == 10:
            return "ten"
        else:
            tens_digit = n // 10
            ones_digit = n % 10
            return tens[tens_digit] + ("-" + ones[ones_digit] if ones_digit != 0 else "")
    
    def three_digit_number_to_words(n):
        hundreds_digit = n // 100
        remainder = n % 100    
        words = []
        if hundreds_digit > 0:
            words.append(ones[hundreds_digit] + " hundred")  
        if remainder > 0:
            words.append(two_digit_number_to_words(remainder))   
        return " ".join(words)
    
    def split_into_thousands(n):
        chunks = []
        while n > 0:
            chunks.append(n % 1000)
            n //= 1000
        return chunks[::-1]   
    chunks = split_into_thousands(number)
    words = []   
    for i in range(len(chunks)):
        if chunks[i] != 0:
            words.append(three_digit_number_to_words(chunks[i]) + (f" {scales[len(chunks) - i - 1]}" if scales[len(chunks) - i - 1] else ""))  
    return " ".join(filter(None, words)).strip()
