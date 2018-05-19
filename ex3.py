import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

# Q5. function add_vectors(u, v)를 작성하라

def add_vectors(u, v):
    for i in range(len(u)):
        u[i] += v[i]
    return u

test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

# Q6. function scalar_mult(s, v)를 작성하라

def scalar_mult(s, v):
    for i in range(len(v)):
        v[i] *= s
    return v

test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

# Q7. function dot_product(u, v)를 작성하라

def dot_product(u, v):
    for i in range(len(u)):
        u[i] *= v[i]
    return sum(u)

test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

# Q8. function cross_product(u, v)를 작성하라

def cross_product(u, v):
    a = []
    for i in range(len(u)):
        b = u[i]
        c = v[i]
        u.remove(u[i])
        v.remove(v[i])
        a.append((u[0]*v[1]) - (u[1]*v[0]))
        u.insert(i, b)
        v.insert(i, c)
    return a
test(cross_product([1, 2, 3], [2, 3, 4]) == [-1, -2, -1])
test(cross_product([3, 5, 1], [4, 3, 8]) == [37, 20, -11])
test(cross_product([1,3,4],[2,7,-5]) == [-43, -13, 1])

# Q9 " ".join(song.split()) 과 song과 같은지 비교하고 언제 다른지 설명하여라

song = " The rain in Spain"

test(song == " ".join(song.split())) #같은것을 알수 있다.
print(song.split())
test(song == "e".join(song.split())) #join앞에 ""안을 띄어쓰기가 아닌 다른 글자를 기준으로 하면 다르다.


# 10. function replace(s, old, new)를 작성하라

def replace(s, old, new):
    wlist = s.split(old)
    s = new.join(wlist)
    return s

test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")