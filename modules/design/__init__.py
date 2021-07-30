def menu(lst):
    from time import sleep

    while True:
        print('\033[1;35;40mChoose one of the options below!\033[m')
        print('\033[1;34;40m', end='')
        for c, i in enumerate(lst):
            print(f'{c+1} - {i}')
        print('\033[m', end='')

        try:
            R = int(input('\033[1;35;40mwhich do you choose: '))
            print('\033[036m', end='')
            if R > len(lst) or R < 1:
                int('str')
        except:
            print('\033[1;31;40mNot a valid option!\033[m\n')
            sleep(1)
            continue
        break

    return R
