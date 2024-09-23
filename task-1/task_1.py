def romanToInt(s: str) -> int:
    # Словник для римських символів та їх числових значень
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev_value = 0

    # Проходимо по кожному символу в рядку s
    for char in s:
        # Отримуємо значення поточного символу
        current_value = roman[char]
        
        # Якщо поточне значення більше попереднього, це означає, що був випадок віднімання
        if current_value > prev_value:
            # Віднімаємо подвоєне попереднє значення, оскільки раніше ми його вже додали
            total += current_value - 2 * prev_value
        else:
            # Якщо поточного віднімання немає, просто додаємо значення
            total += current_value
        
        # Оновлюємо попереднє значення для наступної ітерації
        prev_value = current_value
    return total

# Приклади
print(romanToInt("III"))    # Вихід: 3
print(romanToInt("LVIII"))  # Вихід: 58
print(romanToInt("MCMXCIV"))# Вихід: 1994
