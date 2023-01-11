def f(x):
    return x**4 - 2*x**2 + 1/2

def fp(x):
    #return 5*x**4 + 1
    # Vi aprximerar derivatan med delta x som 0.01
    return (f(x + 0.00001) - f(x))/0.00001

def findNextX(x0):
    # x uttlöst ur tangentens ekvation
    return -f(x0)/fp(x0) + x0

def solveX(x0, aproximations=100):
    xList = [x0]
    for i in range(1, aproximations):
        xList.append(findNextX(xList[i-1]))
    return xList[-1]

def main():
    grad = 4

    # vi kollar derivatan i varije punkt för att hitta när derivatan byter täcken
    x = 0
    last_x = 0
    extremes = []
    while x<10:
        if fp(last_x)/fp(x) < 0:
            extremes.append(x)
        if fp(-last_x)/fp(-x) < 0:
            extremes.append(-x)
        last_x = x 
        x += 0.1
    extremes.sort()
    #print(extremes)

    #bra att ta nytt värde om derivatan är för stor

    if grad %2 == 0:
        #print("f(x) har nollstället x1 = " + str(solveX(extremes[0]+(extremes[0]-extremes[1])/2)))
        #print("f(x) har nollstället x2 = " + str(solveX((extremes[0]-extremes[1])/2)))

        #print("f(x) har nollstället x3 = " + str(solveX((extremes[2]-extremes[1])/2)))
        #print("f(x) har nollstället x4 = " + str(solveX(extremes[2]+(extremes[2]-extremes[1])/2)))

        print("f(x) har nollstället x1 = " + str(solveX(extremes[0]+(extremes[0]-extremes[1])/2)))
        for i in range(0, len(extremes)-1):
            if extremes[i] < 0:
                print("f(x) har nollstället x" + str(i+2) + " = " + str(solveX((extremes[i]-extremes[i+1])/2)))
            else:
                print("f(x) har nollstället x" + str(i+2) + " = " + str(solveX((extremes[i+1]-extremes[i])/2)))

        print("f(x) har nollstället x" + str(len(extremes)+1) + " = " + str(solveX(extremes[-1]+(extremes[-1]-extremes[-2])/2)))

    else:
        #om inte minus före x^grad
        pass
    input()

if __name__ == '__main__':
    main()




"""
    gammlaNollställe = 0
    for i in range(-100, 100, 1):
        xList = [i/10]
        for j in range(1, 100):
            xList.append(findNextX(xList[j-1]))
            #print(xList[j])
        #print()
        if gammlaNollställe != xList[-1]:
            print("f(x) har nollstället: " + str(xList[-1]))
            gammlaNollställe = xList[-1]
    """