#������� ������� �� ��� ����-��������, ��� ����� - ��� ����� ����� �������, � �������� - ��� ���������� ����� ����� � ��������, �� �������� ����: ���������
dict = {'�': 15,'�': 1,'�': 9,'�': 1,'�':18,'�':16,'�':2,'�':1}
def fact(a):
    if a == 0:
        return 1
    return fact(a-1) * a
for i in dict:
    dict[i] = fact(dict[i])
print(dict)

#������������� ��� �� ����� � ���������� ������� � ��������� � ����.
sorteddict =  sorted(dict.values())
sorted_dict = {}
for i in sorteddict:
  for j in dict.keys():
    if dict[j]==i:
      sorted_dict[j]= dict[j]
      break
print(sorteddict)
file_to_save = open('file1.txt', 'w+')
file_to_save.write(str(sorted_dict[j]))
file_to_save.close()

#������������� �� ��������� �� �������� � �������� � ��������� � ����.
dict1 = {}
sorteddict1 = sorted(dict, key=dict.get)
for i in sorteddict1:
  dict1[i]= dict[i]
print(dict1)
file_to_save = open('file2.txt', 'w+')
file_to_save.write(str(sorteddict1))
file_to_save.close()

#������� ������ �� �������� ������� � ��������� ��� �� ���: ���� �� �������� ������ �������� �� ������, ������ - ������� � ����
dict2 = {'�': 15,'�': 1,'�': 9,'�': 1,'�':18,'�':16,'�':2,'�':1}
a = dict2.values()
mean = (sum(a) / len(a))
dict_small = [i for i in a if i < mean]
dict_big = [i for i in a if i > mean]
print('������ ��������:', dict_small)
print('������ ��������:', dict_big)