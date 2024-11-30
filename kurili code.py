from collections import Counter
from decimal import Decimal, getcontext
def decimal_to_binary(number, precision=200):
    binary = ''
    count = 0
    while count < precision:
        number *= 2
        if number >= 1:
            binary += '1'
            number -= 1
        else:
            binary += '0'
        count += 1
    return binary
#точность
getcontext().prec = 100
input_text = "Курилин Тимофей Ильич"
input_text = input_text.replace(" ", "").lower()
frequencies = Counter(input_text)
total_symbols = sum(frequencies.values())
probabilities = {char: Decimal(freq) / Decimal(total_symbols) for char, freq in frequencies.items()}
#кумулят 
sorted_chars = sorted(probabilities.keys())
cumulative_prob = {}
cumulative = Decimal('0')
for char in sorted_chars:
    cumulative_prob[char] = cumulative
    cumulative += probabilities[char]
low = Decimal('0')
high = Decimal('1')
intervals = []
for char in input_text:
    range_ = high - low
    high_temp = low + range_ * (cumulative_prob[char] + probabilities[char])
    low_temp = low + range_ * cumulative_prob[char]
    intervals.append({
        'char': char,
        'low': low_temp,
        'high': high_temp
    })
    low, high = low_temp, high_temp
code = (low + high) / 2
binary_code = decimal_to_binary(code)
print("Таблица интервалов:")
print("| Шаг | Символ | Левая граница                           | Правая граница                          |")
print("|-----|--------|-----------------------------------------|-----------------------------------------|")
for idx, interval in enumerate(intervals):
    print(f"| {idx+1:3} | {interval['char']}      | {interval['low']:.100f} | {interval['high']:.100f} |")
print("\nБинарный код:")
print(binary_code)
