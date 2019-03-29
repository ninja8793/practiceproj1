def empname(name):
    print(name)

def decorate(empname):
    def concat_fun(name):

        constr = 'Hello ' + name
        return empname(constr)

    return concat_fun


def decorate1(empname):
    def uppercase(name):

        constr = str(name).upper()
        return empname(constr)

    return uppercase

def decorate2(empname):
    def auth_fun(name):
        if str(name).lower() == "nitin":
            msg="you enter correct name."
            return empname(msg)

    return auth_fun

empname = decorate(empname)
empname = decorate1(empname)
empname = decorate2(empname)

empname('nitin')