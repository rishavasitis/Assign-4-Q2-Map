#Q2 Write a Python program to triple all numbers of a given list of integers. Use Python map.
#sample list: [1, 2, 3, 4, 5, 6, 7]
#Output :[3, 6, 9, 12, 15, 18, 21]

def triple(num):
    return int (num)*3
result= map(triple, input('Enter the list of integers : ').split(','))
print('Triple of all the avilable numbers : ',list(result))

####Direct input ,direct output
''' Num=[1,2,3,4,5,6,7]
Result= list(map(lambda x : x*3 , Num)) #to list
print(Result) ''' 