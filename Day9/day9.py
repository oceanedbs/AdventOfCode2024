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
print(res)

res_list = list(res)


for i in range(0, len(res_list)):
    not_placed = True
    if res_list[i] == '.':
        last_digit = ''
        for j in range(len(res_list) - 1, -1, -1):
            if res_list[j].isdigit() and not_placed and i<j:
                res_list[i] = res_list[j]
                res_list[j] = '.'
                not_placed = False
                

result_string = ''.join(res_list)
print(result_string)

total=0
for k, char in enumerate(res_list):
    if(res_list[k]!='.'):
        total+= int(res_list[k])*k

print(total)
