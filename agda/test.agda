-- open import Data.Nat
-- open import Data.Rational
-- open import Data.Integer

-- x : ℕ
-- x = zero

-- y : ℚ
-- y = 0ℚ

-- z : ℤ
-- z = +0

open import Data.Nat.Show

open import Agda.Builtin.IO using (IO)
open import Agda.Builtin.Unit using (⊤)
open import Agda.Builtin.String using (String)

postulate putStrLn : String → IO ⊤
{-# FOREIGN GHC import qualified Data.Text as T #-}
{-# COMPILE GHC putStrLn = putStrLn . T.unpack #-}

main : IO ⊤
main = putStrLn "Hello world!"
