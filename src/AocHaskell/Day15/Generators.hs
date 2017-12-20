import Data.Bits

generator :: Int -> Int -> [Int]
generator factor = map (.&. 0xffff) . iterate generate
    where generate value = factor * value `mod` 2147483647

main :: IO()
main = do
        print . length . filter (\(a, b) -> a == b) $ take 40000000 (zip generatorA generatorB)
        print . length . filter (\(a, b) -> a == b) $ take 5000000 (zip (filter ((==0) . (`mod` 4)) generatorA) (filter ((==0). (`mod` 8)) generatorB))
    where   generatorA = generator 16807 618
            generatorB = generator 48271 814