import Data.List (zipWith) 
--monotona y blabla 
taSafe :: [Int] -> Bool 
taSafe xs = all (\y -> -3 <= y && y <= -1) d || all (\y -> 3 >= y && y >= 1) d 
  where d = zipWith (-) (tail xs) xs 
 
res :: [[Int]] -> Int 
res xs = length (filter taSafe xs) 
 
--2 
taSafe2 :: [Int] -> Bool 
taSafe2 xs = any taSafe [take k xs ++ drop (k+1) xs | k <- [0..length xs-1]] 
 
res2 :: [[Int]] -> Int 
res2 xs = length (filter taSafe2 xs) 
 
io :: FilePath -> IO() 
io input = do 
    f <- readFile input 
    let r = map (map read . words) (lines f) :: [[Int]] 
    putStrLn $ show (res r) 
    putStrLn $ show (res2 r) 
    return ()