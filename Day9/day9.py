with open('Day9/data.txt', 'r') as file:
    data = file.read()

print(data)

# Part 1

i = 0
res=''

for k, char in enumerate(data):
    if k%2 == 0:
        res+= str(i)*int(char)
        i+=1
    else:
        res += '.'*int(char)
print(res[0:200])
print(res[-200:-1])

res_list = list(res)

last_digit_index = len(res_list) - 1
for i in range(0, len(res_list)):
    if res_list[i] == '.':
        not_placed = True
        while last_digit_index > i and not_placed:
            if res_list[last_digit_index].isdigit():
                res_list[i] = res_list[last_digit_index]
                res_list[last_digit_index] = '.'
                not_placed = False
            last_digit_index -= 1
                

result_string = ''.join(res_list)
print(result_string[0:200])

total=0
for k, char in enumerate(res_list):
    if(res_list[k]!='.'):
        total+= int(res_list[k])*k

print(total)
