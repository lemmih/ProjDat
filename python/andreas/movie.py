import mytime

class movie(object):
    def __init__(self, title, length=None, year=0):
        self.title = title
        if length == None:
            self.length = mytime.time()
        else:
            self.length = length
        self.year = year

    def __str__(self):
        return 'Title: ' + self.title + " Length: "+ str(self.length) + " Year: " + str(self.year)


m = movie("onion")
print m
