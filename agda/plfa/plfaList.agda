import Relation.Binary.PropositionalEquality as Eq
open Eq using (_≡_; refl; sym; trans; cong)
open Eq.≡-Reasoning
open import Data.Bool using (Bool; true; false; T; _∧_; _∨_; not)
open import Data.Nat using (ℕ; zero; suc; _+_; _*_; _∸_; _≤_; s≤s; z≤n)
open import Data.Nat.Properties using
  (+-assoc; +-identityˡ; +-identityʳ; *-assoc; *-identityˡ; *-identityʳ; *-distribʳ-+)
open import Relation.Nullary using (¬_; Dec; yes; no)
open import Data.Product using (_×_; ∃; ∃-syntax) renaming (_,_ to ⟨_,_⟩)
open import Function using (_∘_)
open import Level using (Level)

data List (A : Set) : Set where
  []   : List A
  _::_ : A → List A → List A

infixr 5 _::_

_ : List ℕ
_ = 1 :: 2 :: []

infixr 5 _++_

_++_ : {A : Set} → List A → List A → List A
[]        ++ ys = ys
(x :: xs) ++ ys = x :: (xs ++ ys)

length : {A : Set} → List A → ℕ
length []        = 0
length (x :: xs) = suc (length xs)

-- reverse : ∀ {A : Set} → List A → List A
-- reverse []        = []
-- reverse (x :: xs) = (reverse xs) ++ [ x ]

-- map : ∀ {A B : Set} → (A → B) → List A → List A
-- map f [] = []
-- map f (x :: xs) = f x :: map f xs
