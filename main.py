

def getSolution():
    step_size = input("step size (h)\n")
    M = input("M*X insert(M)\n")
    Xsquare = input("X^ if none enter 1\n")
    N = input("N*Y insert(N)\n")
    Ysquare = input("Y^ (if none enter 1)\n")
    Y = input("Starting Y(X) = Y(enter Y)\n")
    X = input("Y(X) = Y(enter X)\n")
    constants = input("constants\n")

    iterations = input("number of steps\n")

    constants = float(constants)
    X = int(X)
    Y = int(Y)
    N = float(N)
    Xsquare = int(Xsquare)
    Ysquare = int(Ysquare)
    M = float(M)
    step_size = float(step_size)

    answers = []
    print("i  xi  yi")
    for i in range(int(iterations)):
        MX = X
        NY = Y
        for i in range(Xsquare-1):
            MX = X * MX
        for j in range(Ysquare-1):
            NY = Y * NY

        #Fxy
        final_answer = (M*MX) + (N*NY) + constants
        #H * fxy
        final_answer = step_size * final_answer
        #Yn-1 + (H*fxy)
        final_answer = Y + final_answer
        answers.append(final_answer)
        print((i+1), X, answers[i])
        X += step_size
        Y = final_answer

getSolution()