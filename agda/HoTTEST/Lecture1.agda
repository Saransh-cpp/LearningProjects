data ℕ : Set where
  zero : ℕ
  suc  : ℕ → ℕ

data Bool : Set where
  true false : Bool

data List (A : Set) : Set where
  []   : List A
  _::_ : A → List A → List A
infixr 5 _::_

{-# BUILTIN NATURAL ℕ #-}

infix 5 _+_

_+_ : ℕ → ℕ → ℕ
zero  + x = x
suc x + y = suc (x + y)

data ⊥ : Set where

data ⊤ : Set where
  ⋆ : ⊤

infix 0 _≣_

_≣_ : ℕ → ℕ → Set
zero ≣ zero = ⊤
zero ≣ suc y = ⊥
suc x ≣ zero = ⊤
suc x ≣ suc y = x ≣ y

ℕ-refl : (x : ℕ) → x ≣ x
ℕ-refl zero    = ⋆
ℕ-refl (suc x) = ℕ-refl x

_++_ : {A : Set} → List A → List A → List A
[]        ++ ys = ys
(x :: xs) ++ ys = x :: (xs ++ ys)

length : {A : Set} → List A → ℕ
length []        = 0
length (x :: xs) = suc (length xs)

lh : {X : Set} (xs ys : List X) → length (xs ++ ys) ≣ length xs + length ys
lh []        ys = ℕ-refl (length ys)
lh (x :: xs) ys = IH
  where
    IH : length (xs ++ ys) ≣ (length xs + length ys)
    IH = lh xs ys
