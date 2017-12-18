import System.IO (readFile)
import Data.List.Split (splitOn)

readSpreadsheet :: String -> [[Int]]
readSpreadsheet = map (map read . (splitOn "\t")) . lines

maxMinChecksum :: [[Int]] -> Int
maxMinChecksum = sum . map (\row -> (maximum row) - (minimum row))

evenlyDivisibleChecksum :: [[Int]] -> Int
evenlyDivisibleChecksum = sum . map (\row -> head [x `div` y | x <- row, y <- row, x /= y, x `mod` y == 0]) 

main :: IO()
main = do   puzzleInput <- readFile "./data/02"
            print . maxMinChecksum $ readSpreadsheet puzzleInput
            print . evenlyDivisibleChecksum $ readSpreadsheet puzzleInput