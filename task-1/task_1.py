def romanToInt(s: str) -> int:
    # ������� ��� �������� ������� �� �� �������� �������
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev_value = 0

    # ��������� �� ������� ������� � ����� s
    for char in s:
        # �������� �������� ��������� �������
        current_value = roman[char]
        
        # ���� ������� �������� ����� ������������, �� ������, �� ��� ������� ��������
        if current_value > prev_value:
            # ³������ ������� �������� ��������, ������� ����� �� ���� ��� ������
            total += current_value - 2 * prev_value
        else:
            # ���� ��������� �������� ����, ������ ������ ��������
            total += current_value
        
        # ��������� �������� �������� ��� �������� ��������
        prev_value = current_value
    return total

# ��������
print(romanToInt("III"))    # �����: 3
print(romanToInt("LVIII"))  # �����: 58
print(romanToInt("MCMXCIV"))# �����: 1994
