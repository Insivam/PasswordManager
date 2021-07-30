from time import sleep
from modules.design import menu
from modules.functions import getfun, open_file

lst = ('Show', 'Add', 'Change', 'Delete', 'Close')

open_file()
while True:
    getfun(menu(lst))
    sleep(1.5)
    print()
