```def rec_naive(a,b):
  if a==b:
    return 0
  return b + rec_naive(a-1, b)```

Let's try stepping through a smaller set of numbers:
rec_naive(2, 4) → 2 + rec_naive(1, 4)
  rec_naive(1, 4) → 3 + rec_naive(0, 4)

So for a = 2 we have two additions, therefore a = 17 → seventeen additions
