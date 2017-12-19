import System.IO (readFile)
import Control.Monad.ST (runST)
import qualified Data.Vector.Unboxed as V (fromList, thaw)
import qualified Data.Vector.Unboxed.Mutable as M (length, read, write)

countSteps :: [Int] -> (Int -> Int) -> Int
countSteps instructions jumpChange = runST $ V.thaw jumps >>= jump 0 0
    where   jumps = V.fromList instructions
            jump count index list
                | index < 0 || index >= M.length list = return count
                | otherwise = do
                    val <- M.read list index 
                    M.write list index $ jumpChange val
                    jump (count + 1) (index + val) list

main :: IO()
main = do   puzzleInput <- readFile "./data/05"
            let instructions = (map read . lines $ puzzleInput) :: [Int]
            print $ countSteps instructions (+1)
            print $ countSteps instructions (\j -> if j >= 3 then j-1 else j+1)