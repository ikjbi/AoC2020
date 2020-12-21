fhand = open('input.txt')
correct_passwords = 0 # Sum up all correct passwords 
keyword_counter = 0 # Used to compute if keyword is fulfilled by rules

for line in fhand:
    line = line.rstrip()
    ## Distinguish what parts of the string to use
    atpos1 = 0
    sspos1 = line.find('-')
    atpos2 = line.find('-')+1
    sspos2 = line.find(':')-2
    ## Setting up rules
    rule1 = int(line[atpos1:sspos1])
    rule2 = int(line[atpos2:sspos2])
    ## Finding the password
    pwpos1 = line.find(':')+2
    pwpos2 = line.find(':')+60
    password = line[pwpos1:]
    ## Finding the keyword
    keyword = line[line.find(':')-1:line.find(':')]
    ## print(rule1, rule2, keyword, password)

## Part 1 - Check for keyword in password
    for it in password:
        if it == keyword:
            keyword_counter = keyword_counter +1
    if keyword_counter >= rule1 and keyword_counter <= rule2:
        correct_passwords = correct_passwords +1
    keyword_counter = 0
    print("Number of correct passwords are: ", correct_passwords)

## Part 2 - New password requirements
fhand = open('input.txt')
correct_passwords2 = 0
for line in fhand:
    line = line.rstrip()
    ## Distinguish what parts of the string to use
    atpos1 = 0
    sspos1 = line.find('-')
    atpos2 = line.find('-')+1
    sspos2 = line.find(':')-2
    ## Setting up rules
    rule1 = int(line[atpos1:sspos1])
    rule2 = int(line[atpos2:sspos2])
    ## Finding the password
    pwpos1 = line.find(':')+2
    pwpos2 = line.find(':')+60
    password = line[pwpos1:]
    ## Finding the keyword
    keyword = line[line.find(':')-1:line.find(':')]
    ## print(rule1, rule2, keyword, password)

#    print(rule1, rule2)
#    print(password[rule1-1], password[rule2-1])
    if (keyword == password[rule1-1] and keyword != password[rule2-1]) or (keyword != password[rule1-1] and keyword == password[rule2-1]):
        correct_passwords2 = correct_passwords2 +1
    else:
        correct_passwords2 = correct_passwords2
    print(correct_passwords2)

    
    
    


