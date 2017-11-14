primes = 2:3:[x | x <- [5,7..], primeTest x (isqrt x) (tail primes)]

primeTest n sqrt_n (d:ds) = if d > sqrt_n then True
                     else if (mod n d)==0 then False
                          else primeTest n sqrt_n ds

isqrt = floor . sqrt . fromIntegral

spaces = [y-x | (x,y) <- zip primes (tail primes)]

tenDigitPrimes = [x | x <- primes, and [(x > 999999999),(x < 1000000000)]]

index n l = index' n l 0
index' n (x:xs) i = if x > n then -1
                    else if x == n then i
                         else index' n xs (i+1)

slice l s n = take n $ drop s l

primeFactor n = primeFactor' n (isqrt n) (tail primes)
primeFactor' n sqrt_n (x:xs) = if x > sqrt_n then n
                        else if (mod n x)==0 then x
                             else primeFactor' n sqrt_n xs

eulerNum = 317584931803
eroot = isqrt eulerNum

euler (x:xs) = if x > eroot then []
                 else if (mod eulerNum x)==0 then x : euler xs
                      else euler xs

euler_answer = head $ reverse $ euler primes
