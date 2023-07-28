open import Data.Nat
open import Data.List hiding (filter)
open import Data.Bool
open import Relation.Binary.PropositionalEquality
open import Function

is-non-zero : ℕ → Bool
is-non-zero zero    = false
is-non-zero (suc _) = true

filter : {X : Set} (p : X → Bool) → List X → List X
filter p [] = []
filter p (x ∷ xs) with p x
... | true  = x ∷ filter p xs
... | false = filter p xs

-- foo : {X : ℕ} → List X
-- foo = filter is-non-zero (4 ∷ 3 ∷ 0 ∷ 1 ∷ []) 

_&&_ : Bool → Bool → Bool
false && false = false
false && true  = false
true  && false = false
true  && true  = true

&&-is-commutative : (b s : Bool) → (b && s) ≡ (s && b)
&&-is-commutative false false = refl
&&-is-commutative false true  = refl
&&-is-commutative true false  = refl
&&-is-commutative true true   = refl

-- map-id : {X : Set} (xs : List X) → map id xs ≡ xs
-- map-id []       = refl
-- map-id (x ∷ xs) = {!map-id xs!}
