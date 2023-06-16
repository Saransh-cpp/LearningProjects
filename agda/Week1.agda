module Week1 where

-- const function

const : {A B : Set} → A → B → A
const a b = a

-- list data type

data List (X : Set) : Set where
  []   : List X
  _::_ : X → List X → List X

append : ∀ {A} → List A → List A → List A
append [] ys        = ys
append (x :: xs) ys = x :: append xs ys

open import Data.Nat
open import Data.Bool
open import Data.Maybe

-- indexing a list

-- _!!_ : {A : Set} → List A → ℕ → Maybe A
-- [] !! n            = nothing
-- (x :: xs) !! zero  = just x
-- (x :: xs) !! suc n = xs !! n

-- indexing a list with only a valid index

data Vec (X : Set) : ℕ → Set where
  []   : Vec X zero
  _::_ : ∀ {n} → X → Vec X n → Vec X (suc n)

data Fin : ℕ → Set where
  zero : ∀ {n} → Fin (suc n)
  suc  : ∀ {n} → Fin n → Fin (suc n)

_!!_ : ∀ {A n} → Vec A n → Fin n → A
[] !! ()
(x :: xs) !! zero = x
(x :: xs) !! suc n = xs !! n

-- find : {A : Set}(n : ℕ) → (A → Bool) → Vec A n → Maybe (Fin n)
-- find p [] = nothing
-- find (n: ℕ) → p (x :: xs) = {!Maybe (Fin (suc n))!}
