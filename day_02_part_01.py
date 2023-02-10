import os
def read_file(file_path):
    address="{}.txt".format(file_path)
    if os.path.exists(address):
        file=open(address , "r")
        txt=file.read()
        x=txt.split(",")
        if "" in x:
            x.remove("")
        numbers=list(map(int , x))
        return numbers
    
    else:
        return False

def calculate(numbers:list):
    for i in range(0, len(numbers) , 4):
        if numbers[i]==99:
            break

        elif numbers[i]==1:
            index1=numbers[i+1]
            index2=numbers[i+2]
            index3=numbers[i+3]
            numbers[index3]=numbers[index1]+numbers[index2]
        
        else :
            index1=numbers[i+1]
            index2=numbers[i+2]
            index3=numbers[i+3]
            numbers[index3]=numbers[index1]*numbers[index2]
    
    return numbers


numbers=read_file("input_02")
numbers[1]=12
numbers[2]=2

result=calculate(numbers)
print("answer part one: ", result[0])
