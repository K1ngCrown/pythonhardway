# string variable with 10 inside
x = "There are %d types of people." % 10
#binary variable with string attached to it
binary  = "binary"
#variable with string attached
do_not = "don't"
#varirable with string and two variables attached to it
y = "Those who know %s and those %s." % (binary, do_not)

#print x and y on seperate lines
print x
print y

#print string with variable strings attached 
print "I said: %r." % x
print "I also said: '%s'." % y

#variable is given boolean value
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#print joke and boolean value
print joke_evaluation % hilarious


w = "This is the left side of..."
e = "a string with a right side."

#print strings
print w + e