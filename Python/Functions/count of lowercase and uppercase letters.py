def count_of_lowercase_and_uppercase_letters(arg_1):
    count_of_uppercase=0
    count_of_lowercase=0
    for letters in word:
        if letters.isupper():
            count_of_uppercase+=1
        else:
            count_of_lowercase+=1
    print(count_of_uppercase)
    print(count_of_lowercase)
word = input()
count_of_lowercase_and_uppercase_letters(word)

#This problem statement is similar to "hello teja" problem statement
