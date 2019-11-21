booleanos = [False, True]
#disyunción (or)
print ('  p \t  q \tp or q')
print ('-'*22)
for p in booleanos:
  for q in booleanos:
    print (p, q, int(p or q), sep='\t')

print()


#conjunción (and)
print ('  p \t  q \tp and q')
print ('-'*22)
for p in booleanos:
  for q in booleanos:
    print (p, q, int(p and q), sep='\t')

print()


#negación (not)
print ('  p  \tnot p')
print ('-'*22)
for p in booleanos:
  print (p, int(not p), sep='\t')

print()

#bidireccional
print ('  p \t  q \tp <=> q')
print ('-'*22)
for p in booleanos:
  for q in booleanos:
    if p == q:
      print (p, q, 1, sep='\t')
    else:
      print (p, q, 0, sep='\t')

print()

#condicional
print ('  p \t  q \tp -> q')
print ('-'*22)
for p in booleanos:
  for q in booleanos:
    if p == True and q == False:
      print (p, q, 0, sep='\t')
    else:
      print (p, q, 1, sep='\t')

print()