print("TASK 1")

arr1 = [[3,7,2,9],
       [8,3,6,7],
       [4,8,3,5],
       [9,6,5,4]]

weight1 =[8,9,6,7]
sumarr1=[]

for i in range(len(arr1)):
    print("")
    for j in range(len(arr1)):
        arr1[i][j]=arr1[i][j]*weight1[j]
        print(arr1[i][j], end=" ")

for i in arr1:
    rowsum1=sum(i)
    sumarr1.append(rowsum1)
print("\nFunction:",sumarr1, end=" ")
     
max_i1=sumarr1.index(max(sumarr1))

print("\nBest choise is number",max_i1+1,"with result",max(sumarr1))


print("\nTASK 2")


arr2 = [
    [85, 30, 22, 0.65, 6],
    [60, 20, 10, 0.6, 7],
    [30, 12, 5, 0.45, 5],
    [75, 24, 13, 0.7, 8],
    [40, 15, 7, 0.55, 7],
]

weight2 = [7, 5, 6, 8, 6]
max_values_in_columns = []
min_values_in_columns = []
sumarr2=[]

for col in range(len(arr2)):
    max_value = max(arr2[row][col] for row in range(len(arr2[col])))
    max_values_in_columns.append(max_value)

for col in range(len(arr2)):
    min_value = min(arr2[row][col] for row in range(len(arr2[col])))
    min_values_in_columns.append(min_value)


for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        if j == 1:
            arr2[i][j] = (max_values_in_columns[j] - arr2[i][j]) / (
                max_values_in_columns[j] - min_values_in_columns[j]
            )
            
        else:
            arr2[i][j] = (arr2[i][j] - min_values_in_columns[j]) / (
                max_values_in_columns[j] - min_values_in_columns[j]
            )


for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        arr2[i][j]=arr2[i][j]*weight2[j]
       

for i in arr2:
    rowsum2=sum(i)
    sumarr2.append(rowsum2)
print("\nFunction:",sumarr2, end=" ")
     
max_i2=sumarr2.index(max(sumarr2))

print("\nBest choise is number",max_i2+1,"with result",max(sumarr2))
    
