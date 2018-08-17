class stu(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def pr(self):
        print self.name, self.score


bart = stu('fride', 123)

bart.pr()