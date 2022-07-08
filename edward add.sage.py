

# This file was *autogenerated* from the file edward add.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_4 = Integer(4); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3)
R = QQ['y1, y2, c, d, x1, x2']; (y1, y2, c, d, x1, x2,) = R._first_ngens(6)
e = _sage_const_1 -d*c**_sage_const_4 
S = R.quotient([x1**_sage_const_2 +y1**_sage_const_2 -c**_sage_const_2 *(_sage_const_1 +d*x1**_sage_const_2 *y1**_sage_const_2 ), x2**_sage_const_2 +y2**_sage_const_2 -c**_sage_const_2 *(_sage_const_1 +d*x2**_sage_const_2 *y2**_sage_const_2 )])

# the Edwards addition law:
x3 = (x1*y2+y1*x2)/(c*(_sage_const_1 +d*x1*x2*y1*y2))
y3 = (y1*y2-x1*x2)/(c*(_sage_const_1 -d*x1*x2*y1*y2))


# map to the Montgomery curve:
u1 = (c+y1)/(c-y1); v1=_sage_const_2 *c*u1/x1
g = (_sage_const_1 /e)*v1**_sage_const_2 -u1**_sage_const_3 -(_sage_const_4 /e-_sage_const_2 )*u1**_sage_const_2 -u1
print(S(g.numerator()))

u2 = (c+y2)/(c-y2); v2 = _sage_const_2 *c*u2/x2
g = (_sage_const_1 /e)*v2**_sage_const_2 -u2**_sage_const_3 -(_sage_const_4 /e-_sage_const_2 )*u2**_sage_const_2 -u2
print(S(g.numerator()))

u3 =(c+y3)/(c-y3); v3=_sage_const_2 *c*u3/x3
g = (_sage_const_1 /e)*v3**_sage_const_2 -u3**_sage_const_3 -(_sage_const_4 /e-_sage_const_2 )*u3**_sage_const_2 -u3
print (S(g.numerator()))

# add on the Montgomery curve:
lambd = (v2-v1)/(u2-u1)
r3 = (_sage_const_1 /e)*lambd**_sage_const_2 -(_sage_const_4 /e-_sage_const_2 )-u1-u2; s3 =lambd*(u1-r3)-v1;

# check the answer:
print (S((u3-r3).numerator()), S((v3-s3).numerator()))

