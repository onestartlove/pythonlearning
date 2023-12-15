lst=[1,'two',3,'four',5,'six']
sorted_nums=sorted([x for x in lst if isinstance(x,int)])
print(sorted_nums)