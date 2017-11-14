fibs = 0:1:[x+y | (x,y) <- zip fibs (tail fibs)]

efibs = [x | x <- fibs, (mod x 2)==0]

euler_answer = foldl (+) 0 (take 11 efibs)

fib 0 = 0
fib 1 = 1
fib n = (fib (n-1)) + (fib (n-2))
