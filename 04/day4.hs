import Data.List.Split (splitOn)
import Data.List (transpose)

parse :: String -> [[Int]]
parse =  map (map f) . splitOn "\r\n" 
    where
        f '.' = 0
        f '@' = 1

overlap :: [[Int]] -> [[Int]]
overlap list = foldl1 (zipWith (zipWith (+))) (shiftAll list)

removable :: [[Int]] -> [[Int]] -> [[Int]]
removable overlap input = zipWith (zipWith f) overlap input
  where
    f o i = if i == 1 && o >= 4 then 1 else 0

fullSum :: [[Int]]  -> Int
fullSum  =  sum . (map sum) 

removeRolls :: [[Int]] -> [[Int]]
removeRolls input =
  zipWith (zipWith f) (removable (overlap input) input) input
  where
    f a b = if a == 1 && b == 1 then 1 else 0


part2 :: ([[Int]], Int) -> Int
part2 (input, n) =
    let newInput = removeRolls input
        removed  = fullSum input - fullSum newInput
    in if input == newInput
        then  n
        else (part2 (newInput, n + removed))


main :: IO ()
main = do
    input <- parse <$> readFile "day4.txt"

    print $ fullSum input - fullSum (removeRolls input) 
    print $ part2 (input, 0)

shiftL :: [[Int]] -> [[Int]]
shiftL = map (\row -> tail row ++ [0])

shiftR :: [[Int]] -> [[Int]]
shiftR = map (\row -> 0 : init row)

shiftU :: [[Int]] -> [[Int]]
shiftU = transpose . shiftL . transpose

shiftD :: [[Int]] -> [[Int]]
shiftD = transpose . shiftR . transpose

shiftAll :: [[Int]] -> [[[Int]]]
shiftAll list = [shiftL list, shiftR list, shiftU list, shiftD list, shiftL . shiftU $ list, shiftL . shiftD $ list, shiftR . shiftU $ list, shiftR . shiftD $ list]
