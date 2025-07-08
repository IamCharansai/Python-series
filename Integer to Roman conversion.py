def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100,  90,  50,  40,
        10,   9,   5,   4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    roman = ''
    for i in range(len(val)):
        while num >= val[i]:
            roman += syms[i]
            num -= val[i]
    return roman

def roman_to_int(s):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev = 0
    for char in reversed(s):
        value = roman_dict[char]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total

# Run
choice = input("Choose conversion: 1) Integer → Roman  2) Roman → Integer: ")

if choice == "1":
    number = int(input("Enter an integer (1–3999): "))
    print("Roman numeral:", int_to_roman(number))
elif choice == "2":
    roman = input("Enter a Roman numeral (e.g., XLII): ").upper()
    print("Integer value:", roman_to_int(roman))
else:
    print(" Invalid option.")
