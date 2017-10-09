tour_A=[4,3,2,1]
tour_B=[]
tour_C=[]

def move_top(A,B):
    B.append(A.pop())

move_top(tour_A,tour_B)
print(tour_A)
print(tour_B)
print(tour_C)
