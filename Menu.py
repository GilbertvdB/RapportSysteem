# here we test and modify the menu's
main_menu = ["Cijfer Invoeren",
             "Rapport",
             "Vak toevoegen"]

sub_menu = ["Nog een update maken?"
            ]

x_menu = ["optie 1",
          "optie 2",
          "optie 3",
          "optie 4"]


def menu(options: list):
    print("Menu:")
    for index, optie in enumerate(options):
        print(f'{index + 1}: {optie}')
    print("0: Exit")
    print("-" * 20)


# def menus():
#     print("Hoofd Menu:")
#     for index, optie in enumerate(menu):
#         print(f'{index + 1}: {optie}')
#     print("0: Exit")
#     print("-" * 20)
#
#
# def submenu():
#     print("Sub Menu:")
#     for indx, opties in enumerate(sub_menu):
#         print(f'{indx + 1}: {opties}')
#     print("0: Exit")
#     print("-" * 20)


if __name__ == '__main__':
    # menu(main_menu)
    # menu(sub_menu)
    # menu(x_menu)

    while True:
        menu(main_menu)
        choice = int(input("Kies een optie: "))
        print()
        if choice == 1:
            while choice == 1:
                # input_change()
                menu(sub_menu)

                choice = int(input("Kies een sub optie: "))
                print()
            if choice == 0:
                break
            else:
                pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 0:
            break

#     while True:
#         menus()
#
#         choice = int(input("Kies een optie: "))
#         print()
#         if choice == 1:
#             while choice == 1:
#                 # input_change()
#                 submenu()
#
#                 choice = int(input("Kies een sub optie: "))
#                 print()
#             if choice == 0:
#                 break
#             else:
#                 pass
#         elif choice == 2:
#             pass
#         elif choice == 3:
#             pass
#         elif choice == 0:
#             break
