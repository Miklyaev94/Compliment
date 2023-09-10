def select_compliment():
    import random
    Compl=open('Compliment.txt','r',-1, 'utf-8')
    const1=random.randint(0, 128)
    const2=0
    for i in Compl:
        if const2 == const1:
            break
        else:
            const2+=1
    return Compl.readline()
    Compl.close()