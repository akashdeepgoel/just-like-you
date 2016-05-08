# Index file where the flow begins

from time import sleep
from data import people
from math import sqrt

# Just here for printing cool statement :p
def welcome():
	print "Welcome to Just-Like-You!\nYou will now be asked to enter few details"
	sleep(3)

# Writing modular code..because Why not?
def takeData():
	name = raw_input("Enter your name :: ")
	return name

# Everything that works lies here :p
def getList():
	welcome()
	user_name = takeData()
	user_name.strip()
	flag = False 
	while not flag:
		if not user_name in people:
			print "Sorry! That is not in database. Kindly add yourself in 'data.py'"
			user_name = takeData()
		else:
			flag = True

	ordered_list = topMatches(people,user_name)
	return ordered_list


# Returns the Pearson correlation coefficient for p1 and p2
# The real deal
def sim_pearson(prefs,p1,p2):
	# Get the list of mutually rated items
	si={}

	for item in prefs[p1]:
		if item in prefs[p2]:
			si[item]=1

	# Find the number of elements
	n=len(si)
	
	# if they are no ratings in common, return 0
	if n==0: return 0
	
	# Add up all the preferences
	sum1=sum([prefs[p1][it] for it in si])
	sum2=sum([prefs[p2][it] for it in si])
	
	# Sum up the squares
	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
	
	# Sum up the products
	pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
	
	# Calculate Pearson score
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	
	if den==0: 
		return 0
	r=num/den
	return r

# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(prefs,person,n=6,similarity=sim_pearson):
	scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]
	# Sort the list so the highest scores appear at the top
	scores.sort( )
	scores.reverse( )
	return scores[0:n]

def printResult():
	similarityList = getList()
	print "Here is the list of persons like you in descending order of similarity :"
	for i in range(len(similarityList)):
		print "["+str(i+1)+"]: " + str(similarityList[i][1]) + " -> " + str(similarityList[i][0])

printResult()