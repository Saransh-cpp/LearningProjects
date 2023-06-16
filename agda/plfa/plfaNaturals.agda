{-# OPTIONS --exact-split #-}

module plfaNaturals where

data ℕ : Set where
  zero : ℕ
  suc  : ℕ → ℕ

{-# BUILTIN NATURAL ℕ #-}

-- import the file as Eq
import Relation.Binary.PropositionalEquality as Eq
-- from the Eq file, import _≡_ and refl
open Eq using (_≡_; refl)
-- import begin_, _≡⟨⟩_, _∎ from the ≡-Reasoning module inside Eq
open Eq.≡-Reasoning using (begin_; _≡⟨⟩_; _∎)
-- don't import as stuff is defined above
-- import Data.Nat using (ℕ; zero; suc; _+_; _*_; _∸_)

_+_ : ℕ → ℕ → ℕ
zero + n  = n
suc m + n = suc (m + n)

_ : 2 + 3 ≡ 5
_ = refl

_*_ : ℕ → ℕ → ℕ
zero * n    = zero
(suc m) * n = n + (m * n)

-- _^_ : ℕ → ℕ → ℕ
-- m ^ 0       = 1
-- m ^ (1 + n) = m * (m ^ n)

_∸_ : ℕ → ℕ → ℕ
m     ∸ zero  = m
zero  ∸ suc n = zero
suc m ∸ suc n = m ∸ n

-- infixl 6 _+_ _∸_
-- infixl 7 _*_ _^_

{-# BUILTIN NATPLUS _+_ #-}
{-# BUILTIN NATTIMES _*_ #-}
{-# BUILTIN NATMINUS _∸_ #-}

