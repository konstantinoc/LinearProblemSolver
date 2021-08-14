import re


def toLp2(input, output):
    class A_Eqin_b:
        # A class that is help us to return 3 lists from one method
        def __init__(self, a, eqin, b):
            self.A = a
            self.Eqin = eqin
            self.b = b

        def getA(self):
            return self.A

        def getB(self):
            return self.b

        def getEqin(self):
            return self.Eqin

    def stringToList(strg):
        # Split a String(strg) to a list. It splits it when it founds characters (SplitChars)
        strg = re.split('(\+|-|x|X|<|=|>|\n|,|s|S)', strg)
        strg = [i for i in strg if i and i != '\n']
        counter = -1
        for i in strg:
            counter += 1
            try:
                strg[counter] = i.lower()
            except:
                pass
        return strg

    def minOrMax(strg):
        if strg == "min":
            return -1
        else:
            if strg == "max":
                return 1
            else:
                exit("Error!! Min or Max is missing or has spelling error")

    def find_st_pos(lst):
        # try to find if subject to(s.t. or st) is found and it return the position where found,
        # if user didn't typed enter or ',' after objective function and before subject to(s.t. or st)
        # it try to find 's' or 'S' and checks the next position of the list if is ".t." or "t" or "ujectto"
        # if exists it returns the next position of the position where 's' found
        pos = -1
        for i in lst:
            pos += 1
            if i == "s.t." or i == "st" or i == "subjectto":
                return pos
            try:
                if i == 's' or 'S' and lst[pos + 1] == ".t." or lst[pos + 1] == "t" or lst[pos + 1] == "ubjectto":
                    return pos + 1
            except:
                pass
        exit("Subject to is missing")

    def increaseArraySize(lst, more, data):
        # appends in a list(lst) more data(data) that the number of that is equal with the parameter (more)
        for x in range(more):
            lst.append(data)

    def checkSizeAndIncrease(lst, pos):
        # checks if a list has a specific position, if not it calls the increaseArraySize and appends the list  until
        # it created
        if len(lst) < int(pos):
            increaseArraySize(lst, int(pos) - len(lst), 0)

    def missingOperationSymbol(lst):
        flag = False
        for i in lst:
            if i == 'x':
                if not flag:
                    flag == True
                else:
                    return True
            if i == '+' or i == '-':
                flag = False
        return False


    def create_c(ob):
        # it gets the data before a variable. When variable x is found posFlag turn to True and it gets the index.
        # When an operation symbol or ',' found it calls the checkSizeAndIncrease to check if the list is big enough
        # to add the data to the specific index.
        # If an operations symbol is missing or the index of a variable is negative it exits with error messages.
        # return the list c
        arrayC = []
        data = ''
        pos = ''
        posFlag = False
        if missingOperationSymbol(ob):
            exit("+/- is missing: Objective Function")
        if ob[0] == '+' or ob[0] == '-':
            data = ob[0]
            ob = ob[1:]
        for i in ob:
            if i == 'x':
                posFlag = True
                if data == '' or data == '+' or data == '-':
                    data += '1'
            else:
                if i == '+' or i == '-':
                    if posFlag:
                        exit("Variable X cant has negative index: Objective Function")
                    else:
                        data += i
                else:
                    try:
                        int(i)
                        if posFlag:
                            pos = i
                        else:
                            data += i
                        if posFlag:
                            checkSizeAndIncrease(arrayC, int(pos))
                            arrayC[int(pos) - 1] += int(data)
                            data = ''
                            pos = ''
                            posFlag = False
                    except:
                        pass
        return arrayC

    def listToSublists(lst, char, end):
        # appends list elements in a sublist until it find a specified character(char),
        # when char found appends the sublist in the list, then starts again until the list(lst) end or find the end(end)
        # return the new list
        nlist = []
        sub = []
        for i in lst:
            if i == end:
                break
            if i != char:
                sub.append(i)
            else:
                nlist.append(sub)
                sub = []
        return nlist

    def isInt(i):
        # checks if the parameter (i) can cast to integer
        s = ""
        for ii in i[compareSymbolPos(i) + 1:]:
            s += ii
        try:
            int(s)
            return False
        except:
            return True

    def compareSymbolPos(i):
        # finds the position in the list(i) where the compare symbol found.
        # if it didn't found it returns -1
        pos = -1
        for ii in i:
            pos += 1
            if ii == '=':
                return pos
        return -1

    def comparatorCoding(char):
        # <= to -1
        # >= to 1
        # = to 0
        if char == "<=":
            return -1
        else:
            if char == ">=":
                return 1
            else:
                if char == '=':
                    return 0

    def create_A_Eqin_b(res, varc):
        # after the checks for the comparator symbol and the right side,
        # it creates a new list, for all lists elements(res), with the same size as the list C.
        # For every element it gets the data before the variable.
        # When variable x is found posFlag turn to True and it gets the index. When a comparator or an operation
        # symbol found, it add the data to the specific index of the new list. If the symbol is a comparator
        # (compFlag = True), it appends it to the list Eqin, after the comparatorCoding is called .
        # then appends the right side to the b list
        # creates a new object A_Eqin_b(a, Eqin, b) and returns it
        res_count = 0
        a = []
        eqin = []
        b = []
        for i in res:
            if compareSymbolPos(i) == -1:
                exit("Error!!! Operation Symbol of restriction No" + str(res_count + 1) + "must be <= >= or = ")
            if isInt(i):
                exit("Error in right side of restriction No" + str(res_count + 1))

            subA = []
            increaseArraySize(subA, varc, 0)
            data = ''
            pos = ''
            comparator = ''
            posFlag = False
            compFlag = False
            if i[0] == '+' or i[0] == '-':
                data = i[0]
                i = i[1:]
            for char in i:
                if char == 'x':
                    if posFlag:
                        exit("+/- is missing: Restriction No" + str(res_count + 1))
                    else:
                        posFlag = True
                    if data == '' or data == '+' or data == '-':
                        data += '1'
                else:
                    if char == '+' or char == '-':
                        if not posFlag:
                            data += char
                        else:
                            try:
                                subA[int(pos) - 1] += int(data)
                                data = char
                                pos = ''
                                posFlag = False
                            except:
                                exit("Variable X index error")
                    else:
                        try:
                            int(char)
                            if not posFlag:
                                data += char
                            else:
                                pos = char
                            if compFlag:
                                b.append(int(data))
                                data = ''
                                compFlag = False

                        except:
                            if char == '<' or char == '>':
                                compFlag = True
                                comparator += char
                            else:
                                if char == '=':
                                    if not compFlag:
                                        compFlag = True
                                    comparator += char
                                    eqin.append(comparatorCoding(comparator))
                                    try:
                                        subA[int(pos) - 1] += int(data)
                                        data = ''
                                        pos = ''
                                        posFlag = False
                                    except:
                                        try:
                                            int(pos)
                                            exit(
                                                "Variable with bigger index than Objective Function: Restriction No"
                                                + str(res_count + 1))
                                        except:
                                            exit("Operation symbol error: Restriction No" + str(res_count + 1))
            res_count += 1
            a.append(subA)
        arrays = A_Eqin_b(a, eqin, b)
        return arrays

    def listToArrayAsString(lst):
        strg = "["
        for i in lst[:-1]:
            strg += str(i) + '\n'

        strg += str(lst[-1]) + ']'
        return strg

    file = open(input)
    text = file.read()
    file.close()
    text = text.replace(" ", "")

    MinMax = text[0:3]
    MinMax = [minOrMax(MinMax)]

    text = text[3:]
    text = stringToList(text)

    st_pos = find_st_pos(text)
    objectiveFunction = text[0:st_pos]

    c = create_c(objectiveFunction)

    res = text[st_pos + 1:]
    res = listToSublists(res, ',', "end")
    arrays = create_A_Eqin_b(res, len(c))

    file = open(output, "w")
    file.write("\nMinMax = " + listToArrayAsString(MinMax) + "\n")
    file.write("\nc = " + listToArrayAsString(c) + "\n")
    file.write("\nA = " + listToArrayAsString(arrays.getA()) + "\n")
    file.write("\nb = " + listToArrayAsString(arrays.getB()) + "\n")
    file.write("\nEqin = " + listToArrayAsString(arrays.getEqin()) + "\n")
    file.close()


toLp2("text.txt", "parse.txt")
