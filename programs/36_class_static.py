# Define a class named American which has a static method called
#  printNationality.


class American(object):
    @staticmethod
    def printNationality():
        print "America"

anAmerican = American()
anAmerican.printNationality()
American.printNationality()