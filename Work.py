def test_range(x, y, *check): # Укажите параметры
    range_list = []
    for i in cheсk:
        if i >= x and i <= y:
            range_list.append(i)
        else:
            print('Число за границами диапазона')
    return range_list

start = 4
end = 12
print(test_range(start, end, 5, 16, 32, 6, 7, 1))