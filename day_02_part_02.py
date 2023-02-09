from day_02_part_01 import read_file, calculate


def find_output(output: int , numbers:list):
    
    check=False
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            check_numbers=numbers.copy()
            check_numbers[1]=i
            check_numbers[2]=j
            result=calculate(check_numbers)
            if output==result[0]:
                check=True
                break
        
        if check:
            break
    
    if check:
        return 100*check_numbers[1]+check_numbers[2]
    
    else:
        return False


            




numbers=read_file("input_02")
result_2=find_output(19690720 , numbers)
print("answer part two: " , result_2)




