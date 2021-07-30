from random import randint
from string import punctuation
from time import sleep


def pass_gen(pass_size=False):
    from random import sample, randint
    from string import ascii_letters, digits, punctuation

    all = ascii_letters + digits + punctuation.replace('~', '')

    if pass_size == False:
        pass_size = randint(12, 15)
    pass_lst = sample(all, pass_size)
    password = ''

    for i in pass_lst:
        password += i
    return(password)


def open_file(am='r', close=True, creat=False):
    global file

    try:
        file = open('PSW', am)
    except:
        try:
            with open('PSW', 'x') as file:
                open_file(am, creat=True)
        except:
            print('\033[1;31;40mSystem failed to creat file!\033[m')
            exit()
    else:
        if creat:
            print('\033[1;32;40mFile created succesfully!\033[m')
        if close:
            file.close()


def show():
    print('\033[1;36;40m')
    print('-'*87)
    print(
        f'| {"ID".center(4)} | {"Website/App".center(25)} | {"Usuario".center(30)} | {"Password".center(15)} |')
    print('-'*87)

    open_file(close=False)
    data = file.readlines()

    for c, i in enumerate(data):
        i = i.replace('\n', '')
        website = i[:i.index("~")].title()
        username = i[i.index("~", i.index("~")) +
                     1: i.index("~", i.index("~")+1)]
        password = i[i.index("~", i.index("~")+1)+1:]
        print(f'| {c:0>4} | {website:^25} | {username:^30} | {password:<15} |')

    print('-'*87)
    print('\033[m')
    file.close()


def add():
    print()
    name = input('App/Website: ').strip()
    username = input('Username: ').strip()

    while True:
        gen_yn = input('Generate password? ').strip().title()[0]
        if gen_yn in ('Y', 'N'):
            break
        else:
            print('\033[1;31;40mNot a valid answer!\033[036m')

    while gen_yn == 'Y':
        password = pass_gen()
        print(f'Your password is \'\033[1;37;40m{password}\033[1;036;40m\'')
        while True:
            try:
                geni_yn = input('Is that okay? ').strip().upper()[0]
            except Exception:
                print('\033[1;31;40mNot a valid answer!\033[036m')
                continue
            if geni_yn in ('Y', 'N', 'E'):
                break
        if geni_yn == 'Y':
            break
        elif geni_yn == 'N':
            continue
        elif geni_yn == 'E':
            return

    else:
        password = input('Password: ')

    open_file(am='a', close=False)
    file.write(f'{name}~{username}~{password}\n')
    file.close()
    print(f'\033[1;32;40mPassword added succefully!\033[m\n')


def change():
    open_file(close=False)
    lines = file.readlines()
    file.close()
    len_lines = len(lines)
    if len_lines == 0:
        print('\033[1;31;40mNo passwords saved!\033[m')
        return

    while True:
        ID = input('Which ID would you like to change: ')

        try:
            ID = int(ID)
        except Exception:
            print(f'\033[1;31;40mNot a valid ID\033[036m')
            continue
        str_ID = f'{ID:0>4}'

        if ID < 0 or ID >= len_lines:
            print(f'\033[1;31;40m{str_ID} is not a valid ID\033[m')
            continue

        while True:
            del_yn = input(
                f'Are you sure you wanna change {str_ID}? ').strip().title()[0]
            if del_yn in ('Y', 'N'):
                break
            else:
                print('\033[1;31;40mNot a valid answer!\033[036m')
        if del_yn == 'N':
            return
        break

    name = input('App/Website: ').strip()
    username = input('Username: ').strip()

    while True:
        gen_yn = input('Generate a new password? ').strip().title()[0]
        if gen_yn in ('Y', 'N'):
            break
        else:
            print('\033[1;31;40mNot a valid answer!\033[036m')

    while gen_yn == 'Y':
        password = pass_gen()
        print(f'Your password is \'\033[1;37;40m{password}\033[1;036;40m\'')
        while True:
            try:
                geni_yn = input('Is that okay? ').strip().upper()[0]
            except Exception:
                print('\033[1;31;40mNot a valid answer!\033[036m')
                continue
            if geni_yn in ('Y', 'N', 'E'):
                break
        if geni_yn == 'Y':
            break
        elif geni_yn == 'N':
            continue
        elif geni_yn == 'E':
            return

    else:
        password = input('Password: ')

    new_lines = []
    for c, i in enumerate(lines):
        if c != ID:
            new_lines.append(i)
        else:
            new_lines.append(f'{name}~{username}~{password}\n')

    open_file(am='w', close=False)
    file.writelines(new_lines)
    file.close()
    print(f'\033[1;32;40m{str_ID} changed succefully!\033[m')


def delete():
    open_file(close=False)
    lines = file.readlines()
    file.close()
    len_lines = len(lines)
    if len_lines == 0:
        print('\033[1;31;40mNo passwords saved!\033[m')
        return

    while True:
        ID = input('Which ID would you like to delete: ')
        try:
            ID = int(ID)
        except Exception:
            print(f'\033[1;31;40mNot a valid ID\033[036m')
            continue
        str_ID = f'{ID:0>4}'

        if ID < 0 or ID >= len_lines:
            print(f'\033[1;31;40m{str_ID} is not a valid ID\033[m')
            continue

        while True:
            del_yn = input(
                f'Are you sure you wanna delete {str_ID}? ').strip().title()[0]
            if del_yn in ('Y', 'N'):
                break
            else:
                print('\033[1;31;40mNot a valid answer!\033[036m')
        if del_yn == 'N':
            return
        break

    new_lines = []
    for c, i in enumerate(lines):
        if c != ID:
            new_lines.append(i)

    open_file(am='w', close=False)
    file.writelines(new_lines)
    file.close()
    print(f'\033[1;32;40m{str_ID} deleted succefully!\033[m')


def close():
    print('\033[37mClosing', end='\033[m')
    sleep(.5)
    for i in '...':
        print(i, end='')
        sleep(.5)
    exit()


dic = (show, add, change, delete, close)


def getfun(fun):
    dic[fun-1]()
