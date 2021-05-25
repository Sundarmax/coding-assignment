
# Function to print the output
def printTheArray(arr, n):

	for i in range(0, n):
		print(arr[i], end = " ")
	
	print()
	
# Function to convert list to string
def concatenate_list_data(_list):
    result= ''
    for element in _list:
        result += str(element)
    return result


# Function to generate all binary strings
def generateAllBinaryStrings(n, arr, i,_str):
    
	if i == n:
		_res = concatenate_list_data(arr)
		#print(_res)
		if _str in _res:
		    return 0
		return 1
		
	# First assign "0" at ith position
	# and try for all other permutations
	# for remaining positions
	arr[i] = 0
	a = generateAllBinaryStrings(n, arr, i + 1,_str)
	# And then assign "1" at ith position
	# and try for all other permutations
	# for remaining positions
	arr[i] = 1
	b = generateAllBinaryStrings(n, arr, i + 1,_str)
	return a+b
	

# Driver Code
if __name__ == "__main__":

	n = 3
	arr = [None] * n
	# No of class we can't miss 
	arr2 = [0] * n 
	# convert array to string 
	str2 = concatenate_list_data(arr2)

	# Print all ways to attend the class over N days
	print("Number of ways can attend the class : ",generateAllBinaryStrings(n, arr, 0,str2))
	

