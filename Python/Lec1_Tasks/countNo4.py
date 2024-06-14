#Task to Count No 4 in a given List

#function definition
def countNo4(List):
	counter=0
	counter = sum(1 for no in List if no == 4)
	return counter
	
#example
print(countNo4([1,2,4,58,9,7,4,4]))
