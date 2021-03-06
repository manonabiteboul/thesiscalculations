import itertools
from operator import mul, add
from functools import reduce
from compare import checker
from compare import order

def dim(x):
  sol=1
  for i in range(0,len(x)):
    sol = sol*(x[i]+1)
  return(sol)

def isZero(sol):
  return reduce(mul, (reduce(add, x, 0) for x in zip(*sol)), 1) == 0

#vs = [[(2,0,0)],[(1,1,0)],[(0,1,0),(0,1,0)],[(0,0,3),(0,0,3)]]
vs = [[(0, 0, 0, 0, 0)], [(1, 0, 0, 0, 0), (1, 0, 0, 0, 0)], [(2, 0, 0, 0, 0)], [(3, 0, 0, 0, 0), (3, 0, 0, 0, 0)], [(4, 0, 0, 0, 0)], [(5, 0, 0, 0, 0), (5, 0, 0, 0, 0)], [(6, 0, 0, 0, 0)], [(8, 0, 0, 0, 0)], [(10, 0, 0, 0, 0)], [(0, 1, 0, 0, 0), (0, 1, 0, 0, 0)], [(0, 0, 1, 0, 0), (0, 0, 1, 0, 0)], [(0, 0, 0, 1, 0), (0, 0, 0, 1, 0)], [(0, 0, 0, 0, 1), (0, 0, 0, 0, 1)], [(0, 2, 0, 0, 0)], [(0, 0, 2, 0, 0)], [(0, 0, 0, 2, 0)], [(0, 0, 0, 0, 2)], [(0, 3, 0, 0, 0), (0, 3, 0, 0, 0)], [(0, 0, 3, 0, 0), (0, 0, 3, 0, 0)], [(0, 0, 0, 3, 0), (0, 0, 0, 3, 0)], [(0, 0, 0, 0, 3), (0, 0, 0, 0, 3)], [(0, 4, 0, 0, 0)], [(0, 0, 4, 0, 0)], [(0, 0, 0, 4, 0)], [(0, 0, 0, 0, 4)], [(0, 5, 0, 0, 0), (0, 5, 0, 0, 0)], [(0, 0, 5, 0, 0), (0, 0, 5, 0, 0)], [(0, 0, 0, 5, 0), (0, 0, 0, 5, 0)], [(0, 0, 0, 0, 5), (0, 0, 0, 0, 5)], [(0, 6, 0, 0, 0)], [(0, 0, 6, 0, 0)], [(0, 0, 0, 6, 0)], [(0, 0, 0, 0, 6)], [(0, 8, 0, 0, 0)], [(0, 0, 8, 0, 0)], [(0, 0, 0, 8, 0)], [(0, 0, 0, 0, 8)], [(0, 10, 0, 0, 0)], [(0, 0, 10, 0, 0)], [(0, 0, 0, 10, 0)], [(0, 0, 0, 0, 10)], [(1, 1, 0, 0, 0)], [(2, 2, 0, 0, 0)], [(1, 3, 0, 0, 0)], [(1, 1, 2, 0, 0)], [(1, 0, 1, 0, 0)], [(1, 0, 0, 1, 0)], [(1, 0, 0, 0, 1)], [(0, 1, 1, 0, 0)], [(0, 1, 0, 1, 0)], [(0, 1, 0, 0, 1)], [(0, 0, 1, 1, 0)], [(0, 0, 1, 0, 1)], [(0, 0, 0, 1, 1)], [(2, 0, 2, 0, 0)], [(2, 0, 0, 2, 0)], [(2, 0, 0, 0, 2)], [(0, 2, 2, 0, 0)], [(0, 2, 0, 2, 0)], [(0, 2, 0, 0, 2)], [(0, 0, 2, 2, 0)], [(0, 0, 2, 0, 2)], [(0, 0, 0, 2, 2)], [(1, 0, 3, 0, 0)], [(1, 0, 0, 3, 0)], [(1, 0, 0, 0, 3)], [(3, 1, 0, 0, 0)], [(3, 0, 1, 0, 0)], [(3, 0, 0, 1, 0)], [(3, 0, 0, 0, 1)], [(0, 1, 3, 0, 0)], [(0, 1, 0, 3, 0)], [(0, 1, 0, 0, 3)], [(0, 3, 1, 0, 0)], [(0, 3, 0, 1, 0)], [(0, 3, 0, 0, 1)], [(0, 0, 1, 3, 0)], [(0, 0, 1, 0, 3)], [(0, 0, 3, 1, 0)], [(0, 0, 3, 0, 1)], [(0, 0, 0, 1, 3)], [(0, 0, 0, 3, 1)], [(1, 1, 0, 2, 0)], [(1, 1, 0, 0, 2)], [(1, 2, 1, 0, 0)], [(1, 2, 0, 1, 0)], [(1, 2, 0, 0, 1)], [(1, 0, 1, 2, 0)], [(1, 0, 1, 0, 2)], [(1, 0, 2, 1, 0)], [(1, 0, 2, 0, 1)], [(1, 0, 0, 1, 2)], [(1, 0, 0, 2, 1)], [(2, 1, 1, 0, 0)], [(2, 1, 0, 1, 0)], [(2, 1, 0, 0, 1)], [(2, 0, 1, 1, 0)], [(2, 0, 1, 0, 1)], [(2, 0, 0, 1, 1)], [(0, 1, 1, 2, 0)], [(0, 1, 1, 0, 2)], [(0, 1, 2, 1, 0)], [(0, 1, 2, 0, 1)], [(0, 1, 0, 1, 2)], [(0, 1, 0, 2, 1)], [(0, 2, 1, 1, 0)], [(0, 2, 1, 0, 1)], [(0, 2, 0, 1, 1)], [(0, 0, 1, 1, 2)], [(0, 0, 1, 2, 1)], [(0, 0, 2, 1, 1)]]
vs=[[(0, 0, 0, 0, 0)], [(1, 0, 0, 0, 0), (1, 0, 0, 0, 0)], [(2, 0, 0, 0, 0)], [(3, 0, 0, 0, 0), (3, 0, 0, 0, 0)], [(4, 0, 0, 0, 0)], [(5, 0, 0, 0, 0), (5, 0, 0, 0, 0)], [(6, 0, 0, 0, 0)], [(7, 0, 0, 0, 0), (7, 0, 0, 0, 0)], [(8, 0, 0, 0, 0)], [(10, 0, 0, 0, 0)], [(12, 0, 0, 0, 0)], [(14, 0, 0, 0, 0)], [(0, 1, 0, 0, 0), (0, 1, 0, 0, 0)], [(0, 0, 1, 0, 0), (0, 0, 1, 0, 0)], [(0, 0, 0, 1, 0), (0, 0, 0, 1, 0)], [(0, 0, 0, 0, 1), (0, 0, 0, 0, 1)], [(0, 2, 0, 0, 0)], [(0, 0, 2, 0, 0)], [(0, 0, 0, 2, 0)], [(0, 0, 0, 0, 2)], [(0, 3, 0, 0, 0), (0, 3, 0, 0, 0)], [(0, 0, 3, 0, 0), (0, 0, 3, 0, 0)], [(0, 0, 0, 3, 0), (0, 0, 0, 3, 0)], [(0, 0, 0, 0, 3), (0, 0, 0, 0, 3)], [(0, 4, 0, 0, 0)], [(0, 0, 4, 0, 0)], [(0, 0, 0, 4, 0)], [(0, 0, 0, 0, 4)], [(0, 5, 0, 0, 0), (0, 5, 0, 0, 0)], [(0, 0, 5, 0, 0), (0, 0, 5, 0, 0)], [(0, 0, 0, 5, 0), (0, 0, 0, 5, 0)], [(0, 0, 0, 0, 5), (0, 0, 0, 0, 5)], [(0, 6, 0, 0, 0)], [(0, 0, 6, 0, 0)], [(0, 0, 0, 6, 0)], [(0, 0, 0, 0, 6)], [(0, 7, 0, 0, 0), (0, 7, 0, 0, 0)], [(0, 0, 7, 0, 0), (0, 0, 7, 0, 0)], [(0, 0, 0, 7, 0), (0, 0, 0, 7, 0)], [(0, 0, 0, 0, 7), (0, 0, 0, 0, 7)], [(0, 8, 0, 0, 0)], [(0, 0, 8, 0, 0)], [(0, 0, 0, 8, 0)], [(0, 0, 0, 0, 8)], [(0, 10, 0, 0, 0)], [(0, 0, 10, 0, 0)], [(0, 0, 0, 10, 0)], [(0, 0, 0, 0, 10)], [(0, 12, 0, 0, 0)], [(0, 0, 12, 0, 0)], [(0, 0, 0, 12, 0)], [(0, 0, 0, 0, 12)], [(0, 14, 0, 0, 0)], [(0, 0, 14, 0, 0)], [(0, 0, 0, 14, 0)], [(0, 0, 0, 0, 14)], [(1, 1, 0, 0, 0)], [(2, 2, 0, 0, 0)], [(1, 3, 0, 0, 0)], [(1, 1, 2, 0, 0)], [(1, 0, 1, 0, 0)], [(1, 0, 0, 1, 0)], [(1, 0, 0, 0, 1)], [(0, 1, 1, 0, 0)], [(0, 1, 0, 1, 0)], [(0, 1, 0, 0, 1)], [(0, 0, 1, 1, 0)], [(0, 0, 1, 0, 1)], [(0, 0, 0, 1, 1)], [(2, 0, 2, 0, 0)], [(2, 0, 0, 2, 0)], [(2, 0, 0, 0, 2)], [(0, 2, 2, 0, 0)], [(0, 2, 0, 2, 0)], [(0, 2, 0, 0, 2)], [(0, 0, 2, 2, 0)], [(0, 0, 2, 0, 2)], [(0, 0, 0, 2, 2)], [(1, 0, 3, 0, 0)], [(1, 0, 0, 3, 0)], [(1, 0, 0, 0, 3)], [(3, 1, 0, 0, 0)], [(3, 0, 1, 0, 0)], [(3, 0, 0, 1, 0)], [(3, 0, 0, 0, 1)], [(0, 1, 3, 0, 0)], [(0, 1, 0, 3, 0)], [(0, 1, 0, 0, 3)], [(0, 3, 1, 0, 0)], [(0, 3, 0, 1, 0)], [(0, 3, 0, 0, 1)], [(0, 0, 1, 3, 0)], [(0, 0, 1, 0, 3)], [(0, 0, 3, 1, 0)], [(0, 0, 3, 0, 1)], [(0, 0, 0, 1, 3)], [(0, 0, 0, 3, 1)], [(1, 1, 0, 2, 0)], [(1, 1, 0, 0, 2)], [(1, 2, 1, 0, 0)], [(1, 2, 0, 1, 0)], [(1, 2, 0, 0, 1)], [(1, 0, 1, 2, 0)], [(1, 0, 1, 0, 2)], [(1, 0, 2, 1, 0)], [(1, 0, 2, 0, 1)], [(1, 0, 0, 1, 2)], [(1, 0, 0, 2, 1)], [(2, 1, 1, 0, 0)], [(2, 1, 0, 1, 0)], [(2, 1, 0, 0, 1)], [(2, 0, 1, 1, 0)], [(2, 0, 1, 0, 1)], [(2, 0, 0, 1, 1)], [(0, 1, 1, 2, 0)], [(0, 1, 1, 0, 2)], [(0, 1, 2, 1, 0)], [(0, 1, 2, 0, 1)], [(0, 1, 0, 1, 2)], [(0, 1, 0, 2, 1)], [(0, 2, 1, 1, 0)], [(0, 2, 1, 0, 1)], [(0, 2, 0, 1, 1)], [(0, 0, 1, 1, 2)], [(0, 0, 1, 2, 1)], [(0, 0, 2, 1, 1)]]
vs=[[(2,0)],[(0,2)],[(4,0)],[(0,4)],[(6,0)], [(0,6)],[(8,0)],[(0,8)],[(1,0),(1,0)],[(0,1),(0,1)],[(3,0),(3,0)],[(0,3),(0,3)],[(1,1)],[(1,2),(1,2)],[(1,3)],[(3,1)],[(2,2)],[(0,0)]]
solutions = set()

count = 0
def assemble(sol):
  global count
  count += 1
  if count % 10000 == 0:
    print(count, len(sol))
  dim_sum = 0
  for v in itertools.chain.from_iterable(sol):
    dim_sum += dim(v)

  if dim_sum == 12 and not isZero(list(itertools.chain.from_iterable(sol))):
    return [sol]
  if dim_sum >= 12:
    return []

  sols = []
  for i in range(len(vs)):
    sols += assemble(sol + [vs[i]])

  return sols

solutions = assemble([])

print(list(solutions))

for sol in solutions:
  print(sol)
print("Length of solution:")
print(len(solutions))

orderList2=order(2)
basis =[[0]]
for sol in solutions:
    res=[]
    for x in sol:
        for y in x:
            res.append(y)
    if checker(res,basis,orderList5)==-1:
        basis.append(res)
print("length of the basis:")
print(len(basis))
for b in basis:
  print(b)
