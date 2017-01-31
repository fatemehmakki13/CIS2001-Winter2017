def CountDown(number):
    print(number)
    if number > 0:
        CountDown(number-1)

CountDown(10)

def Bad_Fib(sequence_number):
    if sequence_number <= 0:
        return 0
    elif sequence_number == 1 or sequence_number == 2:
        return 1
    else:
        return Bad_Fib(sequence_number - 1) + Bad_Fib(sequence_number - 2)

#print(Bad_Fib(30))

def Good_Fib(sequence_number):
    if sequence_number <= 0:
        return 0
    elif sequence_number == 1 or sequence_number == 2:
        return 1
    else:
        return _Recursive_Fib(1,1,3,sequence_number)

def _Recursive_Fib(nth_minus_1, nth_minus_2, current_position, sequence_number):
    if current_position == sequence_number:
        return nth_minus_1 + nth_minus_2
    return _Recursive_Fib(nth_minus_1 + nth_minus_2, nth_minus_1, current_position+1, sequence_number)

print(Good_Fib(50))

print(' | | | |W| | | ')
print('---------------')
print(' | | |B| |B| | ')