isqrt = floor . sqrt . fromIntegral

primes = 2:3:[x | x <- [5,7..], primeTest x (isqrt x) (tail primes)]

primeTest n sqrt_n (d:ds) = if d > sqrt_n then True
                            else if (mod n d)==0 then False
                                 else primeTest n sqrt_n ds

primeFactors n = primeFactors' n primes
primeFactors' n (x:xs) = if x > dn then []
                        else if (mod n x)==0 then x : primeFactors' n xs
                             else primeFactors' n xs
                        where
                          dn = if odd n then div n 3
                               else div n 2

pFactorization n [] = []
pFactorization n (x:xs) = if (mod n x)==0 then x : pFactorization (div n x) (x:xs)
                          else pFactorization n xs

count n [] = 0
count n (x:xs) = if x==n then 1 + count n xs
                 else count n xs

pfList n = pfList' pfs (pFactorization n pfs)
           where
             pfs = primeFactors n
pfList' [] pfactorization = []
pfList' (x:xs) pfactorization = (x,(count x pfactorization)) : pfList' xs pfactorization

sumFactors n = (sumFactors' (pfList n)) - n
sumFactors' [] = 1
sumFactors' (x:xs) = (getSum x 1) * (sumFactors' xs)

getSum n sum = if e==0 then sum
               else getSum (p,e-1) (sum*p+1)
               where
                 p = fst n
                 e = snd n

isAbundant n = (sumFactors n) > n

abundantNumbers = [x | x <- [12..], isAbundant x]
--AbundantNumbers = take 6962 abundantNumbers
