list1=eval(input())
list2=eval(input())
diff_list = list(set(list1) - set(list2))
print(diff_list)