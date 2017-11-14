
charVal s = zip s [0..]
valChar s = zip [0..] s

matchVal [] _ = 0
matchVal (d:ds) c = if c == (fst d) then (snd d)
                    else matchVal ds c

values cs ds = map (matchVal (charVal ds)) cs

calculate ns base = sum (map (\x -> (fst x) * (base ^ (snd x))) (zip (reverse ns) [0..]))

value_of cs ds = calculate (values cs ds) (length ds)

