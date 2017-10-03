def bubble_sort(lst):
    # метод пузырька task 01_03
    n = 1# n- компонент  при первом проходе определяет элемент либо макс либо мин , и сокрашает количество элеменов в строке н 1 так как этот элемент уже найден
    i = 0  # первый элемент , ++ в цикли for  пробигает по всем элементам lst
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1




lst = [14, 8, 3, 1, 89, 2, 45,0]
print(lst)
bubble_sort(lst)
print(lst)
