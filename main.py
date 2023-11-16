# QUESTION 1

def hello_name(user_name):
   
   print("hello", user_name)

def get_name():
   user_name = input("What's your username?\n")
   return user_name

user_name = get_name()
hello_name(user_name)


#QUESTION 2

def first_odds():
   for num in range (1,100,2):
      print()
first_odds()


# QUESTION 3
a_list = [11, 28, 2, 87, 61]

def max_num_in_list(a_list):
   maxValue = max(a_list)
   print(maxValue)

max_num_in_list(a_list)

#QUESTION 4

def is_leap_year(a_year):
    leap = False 

    if (a_year %400==0):
        leap = True
    elif (a_year%4 ==0 and a_year%100 !=0):
        leap = True
    elif (a_year%100 !=0 and a_year%400 !=0):
        leap = False
    else:
        leap = False

    return leap

a_year = int(input())
print(is_leap_year(a_year))


#QUESTION 5
a_list = [13,3,4,5]

def is_consecutive(a_list):
    a_list = [13,3,4,5]
    b_list = a_list
    b_list.sort()
    if a_list == b_list:
      return True
    else:
       return False

print(is_consecutive(a_list))