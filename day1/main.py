import re
with open('calibration_document.txt') as doc:
    #first part: only with digits
    lines = doc.readlines()
    calibration_values_list=[]
    int_regex=re.compile(r'\d')
    for line in lines:
        digits=re.findall(int_regex, line)
        calibration_values_list.append(str(digits[0])+str(digits[-1]))
    calibration_value=sum(map(int, calibration_values_list))


    #second part: with spelled digits
    digits_spelled_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
    }
    calibration_values_list=[]
    for line in lines:
        digits_index={index: char for index, char in enumerate(line) if char.isdigit()}
        for digit in digits_spelled_dict.keys():
            index = 0
            while index < len(line):
                index = line.find(digit, index)
                if index == -1:
                    break
                digits_index[index] = digit
                index += 1
        first=digits_spelled_dict.get(sorted(digits_index.items())[0][1], sorted(digits_index.items())[0][1])
        last=digits_spelled_dict.get(sorted(digits_index.items())[-1][1], sorted(digits_index.items())[-1][1])
        calibration_values_list.append(str(first)+str(last))
    calibration_value=sum(map(int, calibration_values_list))
    print(calibration_value)