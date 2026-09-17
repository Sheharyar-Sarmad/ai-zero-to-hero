
# tuples are immutable and here's are some important function tuple:

a = (4, 5, 1, 1 , 1 , 1, 1 , 1, 5, 7)  # regular filled tuple
print(a)

no = a.count(1)
indexofa = a.index(5)
lenghtofa = len(a)
maxvalueofa = max(a)
minvalueofa = min(a)
sumofa = sum(a)

print(no)
print(indexofa)
print(lenghtofa)
print(maxvalueofa)
print(minvalueofa)
print(sumofa)


#  concatenation of tuples:

firstTuple = (3 , 5 , 6 , 7 , 78 , 9 , 10)
secondTuple = (5 , 5 , 5 , 5 ,5 , 5 ,5 , 5)
summationOfBothTuples = firstTuple + secondTuple

print(summationOfBothTuples)

#  repeated tuples:

g = ('g' , 'h' , 'i' , 'j')
repeated = g *  3 # whatever time you want to mutiply it you can do it 3 ,4 ,5 etc....
print(repeated)


#  Check the specific value is existed in my tuple or not:

my_tuple = (1 , 2 , 3)
print(2 in my_tuple) # using in you can check that the 2 or anyother value is present in my tuple or not it will always answer as boolean
print(4 in my_tuple)

# Slicing in tuples
tupleForSlice = (1 , 2 , 3 , 4 , 5)
sliced = tupleForSlice[0:4]
print(sliced)

# Tuple Unpacking (also called Sequence Unpacking) method means you can assign the values of the tuple to variables to according to tuple index:

grapes = (1 , 2 , 3 , 4 , 5)
a , b , c , d , e = grapes
print(a , b , c , d , e)