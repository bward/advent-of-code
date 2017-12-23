import Data.List (transpose)
import Data.List.Split (splitOn)
import qualified Data.Map.Strict as M
import Data.Foldable (asum)
import qualified Data.Vector as V

data Pixel = On | Off deriving (Eq, Ord)
type Picture = V.Vector (V.Vector Pixel)
type Rules = M.Map Picture Picture

vecTranspose :: V.Vector (V.Vector a) -> V.Vector (V.Vector a)
vecTranspose = V.fromList . map V.fromList . transpose . V.toList . V.map V.toList

disassemble :: Picture -> V.Vector Picture
disassemble picture =
    V.fromList [V.map (V.slice j size) . (V.slice i size) $ picture | i <- range, j <- range]
    where
        size = if length picture `mod` 2 == 0 then 2 else 3
        range = [0, size.. length picture - 1]

assemble :: V.Vector Picture -> Picture
assemble parts = 
    V.concat [V.map V.concat . V.map V.toList . vecTranspose . (V.slice j size) $ parts | j <- [0, size.. length parts - 1]]
    where size = floor . sqrt . fromIntegral . V.length $ parts

enhance :: Rules -> Picture -> Picture
enhance rules picture
    | length picture > 3 = assemble . V.map (enhance rules) . disassemble $ picture
    | otherwise = case asum . map (\p -> M.lookup p rules) $ transforms picture of Just x -> x
    where transforms picture = concat . take 4 . iterate (map rotate) $ [picture, reflect picture]
            where
                reflect = V.map V.reverse
                rotate = reflect . vecTranspose

readPicture :: String -> Picture
readPicture = V.fromList . map (V.fromList . map (\c -> case c of '#' -> On; '.' -> Off)) . splitOn "/" 

countPixels :: Picture -> Int
countPixels = sum . V.map (V.length . V.filter ((==) On))


main = do
    puzzleInput <- readFile "./data/21"
    let rules = M.fromList . map (\rule -> (readPicture $ rule !! 0, readPicture $ rule !! 2)). map words . lines $ puzzleInput
    let enhancements =  take 19 $ iterate (enhance rules) (readPicture ".#./..#/###")
    print $ map (countPixels . (!!) enhancements) [5, 18]