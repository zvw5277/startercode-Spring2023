# use spaces. Do NOT use tabs.

def q1(mystring):
   #mystring = 'Spring\tSemester\t2023 began this\tweek'
    parts = mystring.split('\t')
    tuple1 = parts[1]
    tuple2 = parts[2]
    tuples = (tuple1, tuple2)
    return (tuples)


def q2(mystring):
   #mystring = "a\tthe\t the \tthe\tthen"
    string_parts = mystring.split("\t")
    return (string_parts.count("the"))


def q3(myarray):
   #myarray = [("A", 2), ("B", 5), ("A", 2), ("A", 10)]
    summation = 0
    for part in myarray:
        if part[0] == "A":
            summation += part[1]
    return (summation)


def q4(myarray):
    """ 
    you cannot change how the array is iterated 
    and you cannot use any list operations on myarray """
    #myarray = [1, 1.5, 3, 7, 9, 10, 1]
    counter = 0
    for mynum in myarray:
        if mynum % 2 != 0:
            counter += 1
        elif mynum % 2 == 0:
            return (counter)
    return (-1)


def q5(myarray):
    #myarray = [('c', 2), ('a', 3), ('d', 3), ('a', 2), ('e', 1), ('c', 1)]
    dictcount = {}
    for i in myarray:
        if i[0] in dictcount:
            dictcount[i[0]] = dictcount.get(i[0]) + i[1]
        else:
            dictcount[i[0]] = i[1]
    return (dictcount)
