fhand = open('input.txt')
expenses = {}
it = 0
for x in fhand:
    x = x.rstrip()
    xnum = float(x)
    expenses[it] = xnum
    it = it +1 

for it_var1 in expenses:
    for it_var2 in expenses:
        if expenses[it_var1]+expenses[it_var2] == 2020:
            Answer = int(expenses[it_var1]*expenses[it_var2])
print(Answer)

for it_var1 in expenses:
    for it_var2 in expenses:
        for it_var3 in expenses:
            if expenses[it_var1] + expenses[it_var2]+expenses[it_var3] == 2020:
                Answer2 = int(expenses[it_var1]*expenses[it_var2]*expenses[it_var3])
print(Answer2)