numb=[123345676776543,12345566777]
numb2=[]
def recurv(N,K):
        product=1
        if len(str(N))<2:
            return N
        else:
            for char in range(len(str(N))):
                if (char % K == 0) or char == 0:
                    product = product*int(str(N)[int(char)])
            return recurv(product,K)
for i in numb:
    recurv(numb, 2)