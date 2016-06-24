"""
#zip function example

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)


for a,b in zipped:
	print (a, b)
"""

"""
example of enumerate and zip function 
"""


# First we grab test scores from the whole gang (minus a.c. slater)
screech = [100.00, 92, 89, 93, 100]
jesse = [99, 100, 100, 97, 90]
zak = [50, 67, 33, 42, 65]
kelley = [90, 82, 92, 82, 100]

# We need a list to hold the group average of each test score, aka: "class average"
running_totals = []

# now we want to get everyone's test score for each test and also hold a reference
# to which test we are on, test_num will hold that number.
for test_num, (a, b, c, d) in enumerate(zip(screech, jesse, zak, kelley), 1):
    print "Class Scores for test %d" % test_num
    print 'Individuals %d, %d, %d, %d' % (a, b, c, d)
    total = a + b + c + d
    current_average = total / 4
    running_totals.append(current_average)
    print 'Test Average: %d' % current_average
    running_average = sum(running_totals) / len(running_totals)
    print 'Running Average: %d' % running_average
    print '-' * 30





"""
Zip Test!
"""
"""
# First we grab test scores from the whole gang (minus a.c. slater)
screech = [100.00, 92, 89, 93, 100]
jesse = [99, 100, 100, 97, 90]
zak = [50, 67, 33, 42, 65]
kelley = [90, 82, 92, 82, 100]

# We need a list to hold the group average of each test score, aka: "class average"
running_totals = []
zipped = zip(screech, jesse)

# now we want to get everyone's test score for each test and also hold a reference
# to which test we are on, test_num will hold that number.
#for test_num, (a, b, c, d) in enumerate(zip(screech, jesse, zak, kelley), 1):
for a, b, c, d in zip(screech, jesse, zak, kelley):
    #print "Class Scores for test %d" % test_num
    print 'Individuals %d, %d, %d, %d' % (a, b, c, d)
    total = a + b + c + d
    current_average = total / 4
    running_totals.append(current_average)
    print 'Test Average: %d' % current_average
    #running_average = sum(running_totals) / len(running_totals)
    #print 'Running Average: %d' % running_average
    print '-' * 30
"""
