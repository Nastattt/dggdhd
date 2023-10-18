#
# def de_none(lst):
#     return [x for x in lst if x is not None]
#
# input_lst = input("Введите элементы списка через пробел: ").split()
# input_lst = [None if x == "None" else eval(x) for x in input_lst]
# result = de_none(input_lst)
# print("Результат:", result)
#
#
# def list_insert(ref_list, start, num, rep):
#     return ref_list[:start] + [num] * rep + ref_list[start:] if len(ref_list) >= start else -1
#
#
# ref_list = input("Введите элементы списка через пробел: ").split()
# ref_list = [int(x) for x in ref_list]
# start = int(input("Введите номер позиции start: "))
# num = int(input("Введите число num: "))
# rep = int(input("Введите количество повторений rep: "))
#
# result = list_insert(ref_list, start, num, rep)
# print(result)
#
# def get_elem(d_,k_):
#     for i in d_:
#         if i == k_:
#             return d_.get(i)
#
#
# d = {'a': 1, 'b': None, 'c': [1, 2]}
# k = 'a'
#
# print(get_elem(d,k))