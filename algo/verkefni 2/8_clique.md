```def clique(n):
  print "in range..."
  for j in range(n):
    for i in range(j):
      print i, " is friends with ", j```

clique(4) →  

```  print            # 1
  range(4)            # 2
    (0)  
      range(0)        # 3
    (1)  
      range(1)        # 4
        print         # 5
    (2)  
      range(2)        # 6
        print         # 7
        print         # 8
    (3)  
      range(3)        # 9
        print         # 10
        print         # 11
        print         # 12```
