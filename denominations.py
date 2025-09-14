def no_notes(a):
    Q = [2000, 500, 200, 100]
    X = 0
    for i in range(4):
        q = Q[i]
        x = a//q
        print (q,x)
amount = int(input ("Enter your Amount"))
no_notes (amount)

