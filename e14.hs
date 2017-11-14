collatz 1 = 1
collatz n = if (odd n) then (3*n)+1
            else div n 2

collatzSeq = terminate . iterate collatz
             where
               terminate (1:_) = [1]
               terminate (x:xs) = x : terminate xs

collatzSeqLen = length . collatzSeq

sequenceLengths = [collatzSeqLen x | x <- [1..999999]]

index n xs = indexh n 0 xs
indexh _ _ [] = -1
indexh n c (x:xs) = if n==x then c
                    else indexh n (c+1) xs

answer = (index (maximum sequenceLengths) sequenceLengths) + 1

main = do
         putStrLn (show answer)