module Week2 where

data Bool : Set where
  true false : Bool

_&_ : Bool → Bool  → Bool
true & y = false
false & y = y


