#Honour Roll Calculator

sum = 0 #counter


while True:
    try:
        coursenumbers = int(raw_input("How many courses were there? (1-8)")) #asks user for course amnt
        while coursenumbers >=9 or coursenumbers <=0: #while loop so you cant enter anything more than 9 or less than 0
            print "Stop right there, you must enter a number between 1-8! Try again!"
            coursenumbers = int(raw_input("How many courses were there? (1-8)"))
        else: #code to prevent it from entering strings into the input
            break
    except ValueError:
        print "Stop right there, you must enter a number between 1-8! Try again!"



for i in range(coursenumbers): #for loop. loops the amount of courses there are
    mark = input("What were your averages? (0-100)") #input for averages
    while mark >100 or mark <0: #while loop so you cant enter more than 100, less than 0
        print "Stop right there, you must enter a number between 0-100! Try again!"
        mark = input("What were your averages? (0-100)")
    if mark <100 or mark >0: #if it meets the range 0 - 100 then add that number to sum
        sum=sum+mark



totalaverage = float(sum)/coursenumbers #divide sum by course numbers to get average
print "The amount of course(s) that you have is {0}".format(coursenumbers)
print "Your total average is {0}".format(totalaverage)

if totalaverage >= 80: #if you have more than an 80 average you get honour roll
    print "Congratulations you made honour roll."
else: #otherwise you didnt get honour roll
    print "You didn't make honour roll! :C, that must really suck man."




