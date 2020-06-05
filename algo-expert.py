#Two Sum problem using TWO FOR LOOP with on(n^2) time | o(1) space
def twoNumberSum(array, targetSum):
	#loop one:
	#go all the way befor last value in the array
	for i in range(len(array) -1):
    		firstNum = array[i]
			#iterate through all the rest numbers of the array:
			for j in rage(i + 1, len(array)):
				#j is going all the way to the end of the array
				secondNum = array[j]
				if firstNum + secondNum == targetSum:
					return [firstNum, secodnNum]
	#return an empty array if we never hit the above return
	return []




