t = ['A', 'T', 'G', 'C', 'A', 'T', 'A', 'A', 'T', 'G', 'C', 'G', 'T', 'C', 'A']
p = ['A', 'T', 'A', 'A']

s = 0
n = len(t)
m = len(p)

while (s <= n - m) :
  i = 0

  while (i < m and t[s+i] == p[i]) :
    i = i + 1

  if (i == m) :
    print("pattern found with shift %d" %(s))

  s = s + 1
