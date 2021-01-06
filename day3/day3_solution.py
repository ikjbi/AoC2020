from itertools import islice
fhand = open('input4.txt')
fhand2 = open('data.txt', 'w')
col_count1 = 1
col_count2 = 1
col_count3 = 1
col_count4 = 1
col_count5 = 1
row_count = 0
tree_count1 = 0
tree_count2 = 0
tree_count3 = 0
tree_count4 = 0
tree_count5 = 0

for line in fhand:
    # Make every line consisting of every character
    line = line.rstrip()
    # Extend line 11 times to make is as wide as long
    line = line * 300  
    #for writeline in line2:
    fhand2.write(line + '\n')
    tree_check1 = line[col_count1-1:col_count1]
    tree_check2 = line[col_count2-1:col_count2]
    tree_check3 = line[col_count3-1:col_count3]
    tree_check4 = line[col_count4-1:col_count4]
    #print(tree_check)
    if tree_check1 == '#':
        tree_count1 = tree_count1 + 1
    if tree_check2 == '#':
        tree_count2 = tree_count2 + 1
    if tree_check3 == '#':
        tree_count3 = tree_count3 + 1
    if tree_check4 == '#':
        tree_count4 = tree_count4 + 1    
    row_count = row_count + 1
    col_count1 = col_count1 + 1
    col_count2 = col_count2 + 3
    col_count3 = col_count3 + 5
    col_count4 = col_count4 + 7

print('------- SOLUTION 1 --------')
print("Row count =", row_count)
print("Column count = ", col_count1)
print('Tree count1 =', tree_count1)
print('Tree count2 =', tree_count2)
print('Tree count3 =', tree_count3)
print('Tree count4 =', tree_count4)
col_count5 = 1
row_count = 1

fhand = open('input4.txt')
tree_count5 = 0
i = 0
for i, line in fhand:
    # Make every line consisting of every character
    line = line.rstrip()
    # Extend line to make it as wide as long
    line = line * 300
    tree_check5 = line[col_count5-1:col_count5]
    if i == 0 or i % 2 == 0:
        #print(tree_check)    
        if tree_check5 == '#':
            tree_count5 = tree_count5 + 1
    row_count = row_count + 1
    col_count5 = col_count5 + 1
    i = i + 1
print("Row count =", row_count)
print('Tree count5 =', tree_count5, '\n')



print('------- SOLUTION 2 --------')
solution2 = tree_count1*tree_count2*tree_count3*tree_count4*tree_count5
print('Solution for problem 2 is:' ,solution2)