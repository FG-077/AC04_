d = {}
def fib(n):
  if (n < 2):
    d[n] = n
    return d[n]
  if (d.keys().__contains__(n)):
    return d[n]    
  d[n] = fib(n - 2) + fib(n - 1)    
  return d[n]  

for i in range(0,50):
  print('fib(',i,'): ', fib(i))