#create a set using curly braskets
from calendar import different_locale

#my_set = {1,2,3}

#print(my_set)

#creating a set from a list using the set() function
#my_set = ([4,5,6])
#print(my_set)

#create an empty set using the set() function
#my_set = set()
#print(my_set)

#my_set = {1,1,2,3,4,5,6,3,2,3}
#print(my_set) #set will automaticlly remove duplicates


###############3#

set1 = {1,2,3}
set2 = {3,4,5}


#Union between set1 and set2 using union() method

union_method = set1.union(set2)

#compute union between set1 and set2 using the operator

union_operator = set set2

print("union of set1 and set2 using method: ", union_method)
print("Union of set1 and set2 using operator", union_operator)

#Compute intersection between set 1 and set2 using the intersection () method

intersection_method = set1.intersection(set2)

#Computing intersection between set1 and set2 using & operator

intersection_operator= set1 & set2

print("Intersection of set1 and set2 using the intersection method", intersection_method)
print("Intersection of set1 and set2 using the intersection operator", intersection_operator)

#Computing the elements that are unique to set1 usning the difference method
difference_method = set1.differenve(set2)

#comuting elements that are unique to set1 ysing the - operator
difference_operator = sset1 - set2

print("Difference of set1 and set2 using the difference method: ",difference_method)
print("Difference of set 1 and set2 using the - operator",difference_operator)

#Computing the elements that are in set1 and set2 but not in their intersection
symmertric_difference_method = set1.symmetrick_difference(set2)

#Computing the elements that are in set1 and set2 but not in their intersection using ^ operator
symmetrick_difference_operator = set1 ^ set2

print()


#SET METHODS

#create a set

my_set = {1,2,3}

#Add number 7 at the end of the set

my_set.add(7) #add method

#Remove number 3 from my set

my_set.remove(3) #remove method

#Removing 8 from the set without throwing and error if 8 in snow on the set

my_set.discard(8)
print(my_set)

#Remving all the numbers from the set
my_set.clear()

print(my_set)


#Remove duplications from a list

#create a list that contains duplications

my_list = [1,2,2,2,3,4,4,4,5,6]

#Convert this list to a set to remove duplications
unique_set =set(my_list)

print(unique_set)

#convert this set to a list
unique_list = list(unique_set)
print(unique_list)


#Checking for common elements

blertas_interest = {"music", "movies", "travel"}
drilonis_interests = {"movies", "games","skiing"}

common_interests = blertas_interests.interesction(drilonis_interests)
print(common_interests)

#IN operator

colors = {"red","purple","yellow","blue"}
colors = "blue"
print(color in colors)
