def poisson(lambd, x):
  return (exp(-lambd) * (lambd ** x)) / factorial(x)