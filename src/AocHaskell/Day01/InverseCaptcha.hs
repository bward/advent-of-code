import System.IO (readFile)
import Data.Char (digitToInt)

inverseCaptcha :: String -> (Int -> Int) -> Int
inverseCaptcha input checkPosition = sum . map fst $ filter (\(x, i) -> x == (cycle digits) !! checkPosition i) (zip digits [0..])
    where digits = map digitToInt input

main :: IO ()
main = do   puzzleInput <- readFile "./data/01"
            print $ inverseCaptcha puzzleInput succ
            print $ inverseCaptcha puzzleInput (\i -> i + div (length puzzleInput) 2)