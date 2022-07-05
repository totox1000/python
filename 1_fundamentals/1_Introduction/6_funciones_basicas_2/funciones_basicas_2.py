# #1
num = 6
for i in range(1,num+1):
    print(num-i)
# este ejercicio imprime 5,4,3,2,1

# #2
def print_and_return(list):
    print(list[0])
    return list[1]
# Este ejercicio imprime 1,2

#3
def acepta_lista(list):
    return list[0] + len(list)
print(acepta_lista([1,2,3,4,5]))
# # Este ejercicio imprime 6

#4
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output


print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))
# No lo entendi

# #5
def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))
# No lo entendi




