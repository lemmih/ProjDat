class time(object):
    h = 0
    m = 0
    s = 0

    def __init__(self, s=0, m=0, h=0):
        minutes, self.s = divmod(s, 60)
        hours, self.m = divmod(minutes+m, 60)
        self.h = h + hours

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.h, self.m, self.s)
        

        
    
