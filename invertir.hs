invertir:: Ord a=>[a]->[a]
invertir[ ]= [ ]
invertir(x:xs) =(invertir xs)++[x]
