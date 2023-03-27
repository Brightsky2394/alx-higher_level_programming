#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        elem_prt = 0
        for j in my_list:
            if elem_prt < x:
                print("{}".format(my_list[elem_prt]), end='')
                elem_prt += 1
        print()
    except IndexError:
        pass
    finally:
        return elem_prt
