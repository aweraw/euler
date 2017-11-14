fibs = 0:1:[x+y | (x,y) <- zip fibs (tail fibs)]

efibs = [x | x <- fibs, (mod x 2)==0]

euler_answer = foldl (+) 0 (take 11 efibs)
