class Animal:
    """comment"""

    def __init__(self, claw, tail):
        self.claw = claw
        self.tail = tail
        self.a = {}
        self.a[0,0]=11
        self.a[0,1]=22

    def get_claw(self):
        return "my claw is:" + self.claw

    def get_tail(self):
        return "my tail is:" + self.tail
