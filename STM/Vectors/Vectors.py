from math import *

#Cross Product
def cross(u,v):
    return [u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]

#Dot Product
def dot(u,v):
    total = 0
    for i in range(0,len(u)):
            total+=u[i]*v[i]
    return total

#Magnitude
def mag(u):
    total = 0
    for i in range(0,len(u)):
            total+=u[i]*u[i]
    return sqrt(total)

#Projection
def projection(u,v):
    m= (1.0*dot(u,v)/dot(v,v))
    return [m*v[0],m*v[1],m*v[2]]

#Convert the Vector Equation of a Line to Parametric
def parametric(l1Vec):
    return [[l1Vec[1][0],l1Vec[0][0]],[l1Vec[1][1],l1Vec[0][1]],[l1Vec[1][2],l1Vec[0][2]]]
            
#Find the point of intersection of a line and plane
def pointOfIntLP(l1,p1):
    tsum = p1[0]*l1[0][0]+p1[1]*l1[1][0]+p1[2]*l1[2][0]
    print (p1[0]*l1[0][0])
    print (p1[1]*l1[1][0])
    print (p1[2]*l1[2][0])
    csum = p1[0]*l1[0][1]+p1[1]*l1[1][1]+p1[2]*l1[2][1]+p1[3]
    print("t", tsum," c",csum)
    t = -1.0*csum/tsum
    print("t",t)
    return [l1[0][0]*t+l1[0][1],l1[1][0]*t+l1[1][1],l1[2][0]*t+l1[2][1]]

#Find the scalar equation of a plane
def scalar(P1):
    n = cross(P1[1],P1[2])
    d = -dot(P1[0],n)
    return [n[0],n[1],n[2],d]

#Some commands to try the above functions:

l1Vec = [[-1,-2,1],[-2,3,1]]
l2Vec = [[1,-1,8],[2,3,1]]
l1Parametric = parametric(l1Vec)
l2Parametric = parametric(l2Vec)
n = cross(l1Vec[1],l2Vec[1])

P1 = [[1,0,-3],[1,2,2],[4,-3,1]]
P1Scalar = scalar(P1)
print("P1 Scalar: ", P1Scalar)
print(l1Parametric)
print(pointOfIntLP(l1Parametric,P1Scalar))
print (cross(P1[1],P1[2]))
P1P2 = [l2Vec[0][0]-l1Vec[0][0],l2Vec[0][1]-l1Vec[0][1],l2Vec[0][2]-l1Vec[0][2]]
Shortest = mag(projection(P1P2,n))
print(n)
print(projection(P1P2,n))
print("Shortest Distance Between L1 and L2:", Shortest)
AB = [2,2,-3]
m2=[2,3,1]
D = mag(projection(AB,m2))
C = mag(AB)
Shortest2 = sqrt(C*C-D*D)
print(Shortest2)

print (projection([7,3,0],[-2,2,0]))
c = mag([32,21,0])
b =mag([4,9])
a = sqrt(c*c-b*b)
print(a)
bu=[-a*9/b,a*4/b]
print (bu)
md = mag([1,2,-2])
du = [1/md,2/md,-2/md]
print (dot(du,[3,1,2])*150)
print(dot([0,5,-1],cross([-2,2,5],[0,4,1])))
    