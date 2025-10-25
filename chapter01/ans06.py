from chapter01.ans05 import get_char_n_gram

if __name__ == "__main__":
    given_string_a = "paraparaparadise"
    given_string_b = "paragraph"

    x = set(get_char_n_gram(given_string_a, 2))
    y = set(get_char_n_gram(given_string_b, 2))

    sum_set_xy = x.union(y)
    inter_set_xy = x.intersection(y)
    diff_set_xy = x.difference(y)

    print("X:", x)
    print("Y:", y)
    print("X ∪ Y:", sum_set_xy)
    print("X ∩ Y:", inter_set_xy)
    print("X - Y:", diff_set_xy)
