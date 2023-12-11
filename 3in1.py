import numpy as np
arr= np.array([3,5,7,9,11,15,18,22])
print('creating numpy arrays')
print('numpy arrays are:',arr)
arr1=(arr[1:6])
print(arr1)
newarr1=arr.reshape(2,4)
print('convert 1D array to 2D array')
print('2D arrayis:',newarr1)

print('slice starting from 3rd value to end')
print(arr[-1:])

print('slice 0 to 4 index')
print('0 to 4 index are:',arr[:5])

print('use negative slicing')
print('negative slicing value is:', arr[-4:-2])

print('use step value using start and end value is empty')
print(arr[::2])

print('slicing with interval')
print('slicing with ineterval is:',arr[3::4])

arr= np.array([[3,5,7,9],[11,15,18,22]])
print('use slicing a 2D arrays')
print('slicing 2D arrays is:',arr[1:,0:3])

arr= np.array([[[3,5,7,9],[11,15,18,22]],[[1,2,3,4],[5,6,7,8,]]])
print('slicing 3-D arrays')
print('slicing 3-D arrays is:',arr[0,1,1:4])

arr1=np.array([1,2,3])
arr2=np.array([[1.8,2.5,3.14],[4,5,6]])
arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('datatype of an array')
print('datatype of array1:',arr1.dtype)
print('datatype of array2:',arr2.dtype)
print('datatype of array3:',arr3.dtype)

arr=np.array([4,7,12])
arr1=np.array([5,9,15])
con=np.concatenate((arr,arr1))
print('concatenated two arrays')
print('concatenated arrays:',con)


arr=np.array([[4,7],[11,12]])
arr1=np.array([[5,9],[14,15]])
con=np.concatenate((arr,arr1),axis=1)
print('concatenate with axis')
print(con)

arr=np.array([[4,7],[12,4]])
arr1=np.array([[5,9],[15,9]])
con=np.concatenate((arr,arr1),axis=0)
print('concatenate with axis')
print(con)

arr=np.array([4,7,12])
arr1=np.array([5,9,15])
arr=np.stack((arr,arr1))
print('join arrays using stack')
print(arr)

arr=np.array([1,2,3])
arr1=np.array([5,9,15])
arr=np.concatenate((arr,arr1),axis=None)
print('joining the two arrays along axis=None')
print(arr)

arr=np.array([1,2,3])
arr1=np.array([5,9,15])
arr2=np.hstack((arr,arr1))
arr3=np.vstack((arr,arr1))
arr4=np.dstack((arr,arr1))
print('stacking of rows,coulmns,height')
print((arr,arr1))
print('stcaking along rows:',arr2)
print('stacking along cloumns:',arr3)
print('stacking along height:',arr4)

res=np.flip(arr[-8:])
print('rever of the data:',res)
