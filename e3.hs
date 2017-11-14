isqrt = floor . sqrt . fromIntegral

primes = 2:3:[x | x <- [5,7..], primeTest x (isqrt x) (tail primes)]

primeTest n sqrt_n (d:ds) = if d > sqrt_n then True 
                            else if (mod n d)==0 then False
                                 else primeTest n sqrt_n ds

eulerNum = 317584931803
eroot = isqrt eulerNum 

euler (x:xs) = if x > eroot then []
                 else if (mod eulerNum x)==0 then x : euler xs
                      else euler xs

answer = head $ reverse $ euler primes
