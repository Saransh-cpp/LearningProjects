open import Data.Nat.Base
open import Data.Bool.Base
open import Data.Bool.Properties
open import Relation.Binary.PropositionalEquality.Core
open import Algebra.Bundles
open import Algebra.Lattice.Bundles
import Algebra.Lattice.Properties.BooleanAlgebra as BooleanAlgebraProperties
open import Algebra.Definitions {A = Bool} _≡_
open import Algebra.Structures {A = Bool} _≡_
open import Algebra.Lattice.Structures {A = Bool} _≡_
open import Data.Product.Base using (_×_; _,_; proj₁; proj₂)
open import Function.Base using (_⟨_⟩_; const; id)

{-
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
-}

not-xor' : ∀ x y → not (x xor y) ≡ (not x) xor y
not-xor' false y = refl
not-xor' true  y = not-involutive y

xor-comm' : Commutative _xor_
xor-comm' false false = refl
xor-comm' false true  = refl
xor-comm' true  false = refl
xor-comm' true  true  = refl

xor-identityˡ' : LeftIdentity false _xor_
xor-identityˡ' _ = refl

xor-identityʳ' : RightIdentity false _xor_
xor-identityʳ' false = refl
xor-identityʳ' true  = refl

xor-identity' : Identity false _xor_
xor-identity' = xor-identityˡ , xor-identityʳ

xor-inverseˡ' : LeftInverse true not _xor_
xor-inverseˡ' false = refl
xor-inverseˡ' true = refl

xor-inverseʳ' : RightInverse true not _xor_
xor-inverseʳ' x = xor-comm x (not x) ⟨ trans ⟩ xor-inverseˡ x

xor-inverse' : Inverse true not _xor_
xor-inverse' = xor-inverseˡ , xor-inverseʳ

xor-is-ok' : ∀ x y → x xor y ≡ (x ∨ y) ∧ not (x ∧ y)
xor-is-ok' true  y = refl
xor-is-ok' false y = sym (∧-identityʳ _)

xor-assoc' : Associative _xor_
xor-assoc' true  y z = sym (not-xor y z)
xor-assoc' false y z = refl
