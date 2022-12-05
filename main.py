"""

Napisz program, który wczytuje od użytkownika kolejne wartości liczb całkowitych do momentu, gdy ten poda wartość 0.
Program wypisze wówczas na ekran komunikat ile użytkownik podał liczb parzystych, a ile nieparzystych.

:return:
"""


def main():
    """
    Funkcja main wywołuje wszystkie pozostałe funkcje.

    :return:
    """
    list_to_check = get_number_list()
    count_even_odd(list_to_check)


def get_number_list():
    """
    Ta funkcja ma za zadanie przyjąć kolejno wartości od użytkownika do momentu wpisania 0. Wartości mają być dodane do
    listy. Wynikiem działania funkcji jest lista wartości wprowadzonych przez użytkownika.
    :return:
    """
    user_list = []
    user_input = int(input("Please Enter any number to end process write 0: "))
    while user_input != 0:  # różne od zera
        user_list.append(user_input)
        user_input = int(input("Please Enter any number to end process write 0: "))

    return user_list


def count_even_odd(list_to_check):
    """
    Funkcja ta sprawda z listy czy numery w liście są parzyste lub nie, dodaje je do countera
    i drukuje wyniki.

    :param list_to_check:
    :return:
    """
    even_count = 0
    odd_count = 0

    # sprawdzanie liczb z listy
    for num in list_to_check:
        # sprawdzanie czy jest odd czy even
        if num % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1

    # drukowanie wyników
    print(list_to_check)
    print("Even numbers: ", even_count)   # liczby parzyste
    print("Odd numbers: ", odd_count)    # liczby nieparzyste
    return "Your results"


if __name__ == '__main__':
    main()
