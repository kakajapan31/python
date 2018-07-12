class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

    def override(self):
        print "PARENT override()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENTS altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PERENTS altered()"

dad = Parent()
print dad
son = Child()

dad.altered()
son.altered()