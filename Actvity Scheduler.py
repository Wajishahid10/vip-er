def scheduleActivities(subject_array,star,final):
    n = len(final)

    Array=[0]*n
    i = 0
    Array[i]=subject_array[i]
    
    for j in range(n):
        
        if star[j] >= final[i]:
            i = j
            Array[i]=subject_array[j]

    return Array
  
def print_Array(A):
    print ("The following activities are selected")
    for i in range(len(A)):
         if A[i]!=0:
             print(A[i])
  
subject_array = ["Maths","Enslish","Biology","Chemistry","Geography","Music"]
star = [1, 3, 0, 5, 8, 5] 
final = [2, 4, 6, 7, 9, 9]
Array = scheduleActivities(subject_array,star,final)
print_Array(Array)