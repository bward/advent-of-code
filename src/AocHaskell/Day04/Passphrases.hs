import System.IO (readFile)
import Data.List (nub, sort)

noDuplicates :: [[String]] -> [[String]]
noDuplicates = filter (\passphrase -> (length . nub $ passphrase) == (length passphrase))

noAnagrams :: [[String]] -> [[String]]
noAnagrams = filter (\passphrase -> (length . nub $ map sort passphrase) == (length passphrase))

main :: IO()
main = do   puzzleInput <- readFile "./data/04"
            let passphrases = map words $ lines puzzleInput
            print . length . noDuplicates $ passphrases
            print . length . noAnagrams $ passphrases