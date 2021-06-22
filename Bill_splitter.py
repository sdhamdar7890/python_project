import random

friends = {}
friends_list = []
print('Enter the number of friends joining (including you):')
number_friends = int(input())
if number_friends > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for _ in range(number_friends):
        friend_name = input()
        friends[friend_name] = 0
        friends_list.append(friend_name)
    print("Enter the total bill value:")
    total_value = int(input())
    each_person_value = round(total_value / number_friends, 2)
    for i in friends.keys():
        friends[i] = each_person_value
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == 'Yes':
        answer = random.choice(friends_list)    
        print(f"{answer} is the lucky one!")
        each_person_value = round(total_value / (number_friends - 1), 2)
        for i in friends.keys():
            if i != answer:
                friends[i] = each_person_value
            else:
                friends[i] = 0
    elif answer == 'No':
        print("No one is going to be lucky")
    print(friends)
else:
    print("No one is joining for the party")

