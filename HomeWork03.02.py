my_presious_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, "", "One", "Two", 2.0, -4.0, True, False, -(True)]

nev_list = filter(lambda x: bool(x == -5), my_presious_list)
nev_list = list(nev_list)
print(nev_list)

mult3 = list(filter(lambda x: x > 3, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

print (mult3)
