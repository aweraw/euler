isqrt = floor . sqrt . fromIntegral

primes = 2:3:[x | x <- [5,7..], primeTest x (isqrt x) (tail primes)]

primeTest n sqrt_n (d:ds) = if d > sqrt_n then True 
                            else if (mod n d)==0 then False
                                 else primeTest n sqrt_n ds

indexOflpbm = indexOflpbm' 0 primes
indexOflpbm' c (x:xs) = if x > 1000000 then c
                        else indexOflpbm' (c+1) xs

answer = foldl (+) 0 (take indexOflpbm primes)
