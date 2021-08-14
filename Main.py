import re

f = open("text.txt")


def errorList(e):
    switch = {
        1: exit("Subject to/st/s.t is missing"),
        2: exit("Please check +/- between variables in Objective Function"),
    }


def solver(txt):
    lp = re.sub(' +', ' ', txt.read()).lstrip().rstrip()
    print(lp + "\n")

    def MinOrMax():
        s = lp[0:lp.find(" ")]
        print(s)
        if s == "max":
            return 1
        else:
            if s == "min":
                return -1
            else:
                return 0

    def find_st_pos():
        st_pos = lp.find("st")
        if st_pos != -1:
            return st_pos
        else:
            st_pos = lp.find("s.t.")
            if st_pos != -1:
                return st_pos
            else:
                st_pos = lp.find("subject to")
                if st_pos != -1:
                    return st_pos
                else:
                    errorList(1)

    def separate_ob():
        return lp[lp.find("=") + 1:find_st_pos()].replace(" ", "")

    def separate_res():
        return lp[find_st_pos():].strip('st').strip('s.t').strip('subject to').replace(' ', '')

    def increaseArraySize(array, more):
        for x in range(more):
            array.append(0)

    def checkSizeAndIncrease(array, pos):
        if len(array) < int(pos):
            increaseArraySize(array, int(pos) - len(array))

    def create_C():
        ob = separate_ob()
        print("Objective Function:" + ob)
        m_c = []
        pos = ""
        if ob[0] != '+' and ob[0] != '-':
            p = '+'
        else:
            p = ob[0]
            ob = ob[1:]
        while True:
            if ('0' <= ob[0] <= '9') or ob[0] == '+' or ob[0] == '-' or ob[0] == '.':
                p = p + ob[0]
                ob = ob[1:]
            else:
                if ob[0] == 'x':
                    if p == '+' or p == '-':
                        p = p + '1'
                    ob = ob[1:]
                    while True:
                        if '0' <= ob[0] <= '9':
                            pos = pos + ob[0]
                            ob = ob[1:]
                        else:
                            if ob[0] == '+' or ob[0] == '-':
                                print(len(ob))
                                checkSizeAndIncrease(m_c, pos)
                                m_c[int(pos) - 1] = int(p)
                                p = ""
                                pos = ""
                                break
                            else:
                                if ob[0] == 'x':
                                    errorList(2)
                                else:
                                    if ob[0] == '\n' or (not ob):
                                        checkSizeAndIncrease(m_c, pos)
                                        m_c[int(pos) - 1] = int(p)
                                        return m_c


    def create_A_and_Eqin():
        res = separate_res()
        print("Restrictions: \n\n" + res)
        m_A = []
        pos = ""
        counter = 0
        while True:
            a = []
            increaseArraySize(a, len(c))
            if res[0] != '+' and res[0] != '-':
                p = '+'
            else:
                p = res[0]
                res = res[1:]
            while True:
                if ('0' <= res[0] <= '9') or res[0] == '+' or res[0] == '-' or res[0] == '.':
                    p = p + res[0]
                    res = res[1:]
                else:
                    if res[0] == 'x':
                        if p == '+' or p == '-':
                            p = p + '1'
                        res = res[1:]
                        while True:
                            if '0' <= res[0] <= '9':
                                pos = pos + res[0]
                                res = res[1:]
                            else:
                                if res[0] == '+' or res[0] == '-':
                                    a[int(pos) - 1] = int(p)
                                    p = ""
                                    pos = ""
                                    break
                                else:
                                    if res[0] == 'x':
                                        errorList(2)
                                    else:
                                        if res[0] == ',':
                                            print(pos)
                                            a[int(pos) - 1] = int(p)
                                            print(a)
                                            m_A[counter] = a
                                            counter += 1
                                        else:
                                            if res[0] == '<' or res[0] == '>' or res[0] == '=':
                                                res = res[1:]
                                                print(a)

                                            else:
                                                res[0] == 'e'
                                                return m_A



    MinMax = [MinOrMax()]
    if MinMax[0] == 0:
        print("Min or Max error? Please check your Objective Function")

    print(MinMax)
    print("\n====================================\n====================================\n")

    c = create_C()
    print("C = " + str(c))
    print("\n====================================\n====================================\n")

    #a = create_A_and_Eqin()
    #print(a)

solver(f)
