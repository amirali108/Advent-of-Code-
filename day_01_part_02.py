from day_01_part_01 import read_file




def calculate_multi(fuels:list):
    sum=0
    for item in fuels:
        item=(item//3)-2
        while item>0:
            sum+=item
            item=(item//3)-2
    

    return sum



fuels=read_file("input_01")
result=calculate_multi(fuels)
print("answer part two:  ", result)



