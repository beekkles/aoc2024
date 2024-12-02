import Data.List (zipWith)

esCreciente :: [Int] -> Bool
esCreciente xs = all (\d -> d >= 1 && d <= 3) (zipWith (-) (tail xs) xs)

esDecreciente :: [Int] -> Bool
esDecreciente xs = all (\d -> d <= -1 && d >= -3) (zipWith (-) (tail xs) xs)

esSeguro :: [Int] -> Bool
esSeguro l = esCreciente l || esDecreciente l

res1 :: [[Int]] -> Int
res1 r = length (filter esSeguro r)

rmElem :: [a] -> [[a]]
rmElem xs = [take k xs ++ drop (k+1) xs | k <- [0..length xs-1]]

esSeguro2 :: [Int] -> Bool
esSeguro2 l = esSeguro l || any esSeguro (rmElem l)

res2 :: [[Int]] -> Int
res2 r = length (filter esSeguro2 r)

io :: FilePath -> IO String
io input = do
    f <- readFile input
    let r = map (map read . words) (lines f) :: [[Int]]

    let r1 = res1 r
    putStrLn $ show r1

    let r2 = res2 r
    putStrLn $ show r2

    return "fin"