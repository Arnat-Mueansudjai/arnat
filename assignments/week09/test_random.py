import random

def test_random():
    random_number = random.randint(1, 10)

    num = int(input("Chose your number (1-10)"))
    if random_number == num:
        print("Wow Wow Wow you are winner")
    
    else :
        print("HaHaHa GG EZ WIN!")    
        if random_number > num:
            print("Too low")
        elif random_number < num:
            print("Too much")
    print(random_number)
    
test_random()