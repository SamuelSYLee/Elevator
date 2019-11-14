from time import sleep

current_floor = 5       # Current floor
Lower = 1               # Upper floor
Upper = 7               # Lower floor
ask_flag = False        # Floor-asking flag
target_floor = 5        # Target floor

while True:
    while (target_floor < Lower) or (target_floor > Upper) or (target_floor == current_floor) or (ask_flag == False):
        try:
            print('Currently,', current_floor, 'floor!')
            target_floor = int(input('Which floor are you going to (1 ~ 7)?'))
        except ValueError:
            print('Please type in number!')
            continue
        if (target_floor <= Upper) and (target_floor >= Lower) and (target_floor != current_floor):
            ask_flag = True
        else:
            ask_flag = False
        

    if target_floor < current_floor:
        print('Currently,', current_floor, 'floor! Going Down!')
        current_floor -= 1
    elif target_floor > current_floor:
        print('Currently,', current_floor, 'floor! Going Up!')
        current_floor += 1
    else:
        ask_flag = False
    
    sleep(0.8)