import os
def read_file(file_path:str):
    address="{}.txt".format(file_path)
    if os.path.exists(address):
        file=open(address , "r")
        txt=file.read()
        lines=txt.split("\n")
        if "" in lines:
            lines.remove("")
        numbers=list(map(int , lines))
        return numbers
    
    else:
        return False


def calculate_fuel(mass_list: list):
    sum=0
    for item in mass_list:
        sum+=(item//3)-2
    
    return sum



fuels=read_file("input_01")
result=calculate_fuel(fuels)
print(result)
