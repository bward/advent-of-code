import System.IO (readFile)
import Data.List (find, transpose)
import Data.List.Split (splitOn)

data Pixel = On | Off deriving (Eq)
type Picture = [[Pixel]]
type Rule = (Picture, Picture)

disassemble :: Picture -> [Picture]
disassemble picture =
    [[(take size) . (drop j) $ picture !! k | k <- [i..i+size-1]] | i <- range, j <- [0, size .. length picture - 1]]
    where
        size = if length picture `mod` 2 == 0 then 2 else 3
        range = [0, size.. length picture - 1]

assemble :: [Picture] -> Picture
assemble parts = 
    concat [map concat . transpose . (take size) . (drop j) $ parts | j <- [0, size.. length parts - 1]]
    where size = floor . sqrt . fromIntegral . length $ parts

enhance :: [Rule] -> Picture -> Picture
enhance rules picture
    | length picture > 3 = assemble . map (enhance rules) . disassemble $ picture
    | otherwise = snd $ case find ((`elem` transforms picture) . fst ) rules of Just x -> x
    where transforms picture = concat . take 4 . iterate (map rotate) $ [picture, flip picture]
            where
                flip = map reverse
                rotate = flip . transpose

readPicture :: String -> Picture
readPicture = map (map (\c -> case c of '#' -> On; '.' -> Off)) . splitOn "/" 

countPixels :: Picture -> Int
countPixels = sum . map (length . filter ((==) On))

main = do
    puzzleInput <- readFile "./data/21"
    let rules = map (\rule -> (readPicture $ rule !! 0, readPicture $ rule !! 2)). map words . lines $ puzzleInput
    let enhancements =  take 19 $ iterate (enhance rules) (readPicture ".#./..#/###")
    print $ map (countPixels . (!!) enhancements) [5, 18]