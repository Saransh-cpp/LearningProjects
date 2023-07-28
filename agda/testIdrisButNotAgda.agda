open import Data.Nat.Base
open import Data.Bool
open import Data.Bool.Properties
open import Relation.Binary.PropositionalEquality.Core

xor-is-ok' : ∀ x y → x xor y ≡ (x ∨ y) ∧ not (x ∧ y)
xor-is-ok' false y = sym (∧-identityʳ y)
xor-is-ok' true  y = refl

not-xor' : ∀ x y → not (x xor y) ≡ (not x) xor y
not-xor' false y = refl
not-xor' true  y = not-involutive _

not-xor-cancel' : ∀ x y → (not x) xor (not y) ≡ x xor y
not-xor-cancel' false y = not-involutive _
not-xor-cancel' true  y = refl

xor-associative' : ∀ x y z → x xor (y xor z) ≡ (x xor y) xor z
xor-associative' false y z = refl
xor-associative' true  y z = not-xor' y z
