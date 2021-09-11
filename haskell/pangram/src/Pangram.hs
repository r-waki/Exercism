module Pangram (isPangram) where
import Data.Char

alphabetList = ['a'..'z']

isPangram :: String -> Bool
-- isPangram text =  map toLower  ( filter (/=' ') text ) `elem` alphabetList
isPangram text = all ( elem (map toLower ( filter (/=' ')) text)  ) alphabetList