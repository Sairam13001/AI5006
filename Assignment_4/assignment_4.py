#Program to prove that a line segment AD in a triangle ABC is angle bisector using triangle similarity concept

def check_if_similar(a,b,c,x,y,z):
    if (a/x == b/y == c/z):
        return 1
a,b,c = [int(x) for x in input("Enter three value: ").split()]
x,y,z = [int(x) for x in input("Enter three value: ").split()]

if check_if_similar(a,b,c,x,y,z):
    print("\nThe given two triangles are similar, so the corresponding angles are equal.")
else:
    print("The given triangles are not similar.")

