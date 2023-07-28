open import Relation.Binary.Construct.Union using (_∪_)

data ℕ : Set where
  zero : ℕ
  suc  : ℕ → ℕ

{-# BUILTIN NATURAL ℕ #-}

data List (A : Set) : Set where
  []  : List A
  _∷_ : A → List A → List A

infixr 5 _∷_

f : List ℕ
f = 1 ∷ 2 ∷ []

g : List ℕ
g = 3 ∷ 4 ∷ []

h : List ℕ
h = f ∪ g
