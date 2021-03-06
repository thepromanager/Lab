# -*- coding: utf-8 -*-


def ass(a, b):
    if a != b:
        print "Assert misslyckades: ", " Fel: ", a, "Rätt: ", b
        assert a == b

##########################################################################

# En lista är som en hiss i ett hus.
# Startar med noll i gatuplanet, men saknar källare.
# Man använder heltal för att ange våning.
# Listor kan innehålla allt möjligt.
# T ex tal, strängar, ordlistor och andra listor.

a = []
a.append(10)
assert a == [10]

a.append(11)
assert a == [10,11]
assert a[1] == 11

a[0] = 9
assert a == [9,11]

a.insert(1,10)
assert a == [9,10,11]

del a[1]
assert a == [9,11]
assert len(a) == 2

a.append(11)
assert a == [9,11,11]
assert a.count(11) == 2
assert a.index(11) == 1

b = a.pop()
assert b == 11
assert a == [9,11]

a.remove(9)
assert a == [11]

a.extend([9,10])
assert a == [11,9,10]
assert a[::-1] == [10,9,11]
assert sorted(a) == [9,10,11]
assert 2*a == [11,9,10,11,9,10]
assert a+a == [11,9,10,11,9,10]

b = a.pop(0)
assert b == 11
assert a == [9,10]

##########################################################################


def f(x): return sorted(x)
ass(f([3,2,4]), [2,3,4])
ass(f([9,7,8]), [7,8,9])


def g(x): return x[::-1]
ass(g([3,2,4]), [4,2,3])
ass(g([3,2,4,5]), [5,4,2,3])


def h(x): return x.pop()
ass(h([3,2,4]), 4)
ass(h([3,2,4,5]), 5)


def i(x):
    x.pop()
    return x
ass(i([3,2,4]), [3,2])
ass(i([3,2,4,5]), [3,2,4])


def j(x):
    x.insert(0,1)
    return x
ass(j([3,2,4]), [1,3,2,4])
ass(j([7,8]), [1,7,8])


def k(x):
    x.append(5)
    return x
ass(k([3,2,4]), [3,2,4,5])
ass(k([3,2,4,6]), [3,2,4,6,5])
