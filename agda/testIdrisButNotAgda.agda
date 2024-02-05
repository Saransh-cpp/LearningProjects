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

not-distribˡ-xor' : ∀ x y → not (x xor y) ≡ (not x) xor y
not-distribˡ-xor' false y = refl
not-distribˡ-xor' true  y = not-involutive _

not-distribʳ-xor' : ∀ x y → not (x xor y) ≡ x xor (not y)
not-distribʳ-xor' false y = refl
not-distribʳ-xor' true  y = refl

xor-identityˡ' : LeftIdentity false _xor_
xor-identityˡ' _ = refl

xor-identityʳ' : RightIdentity false _xor_
xor-identityʳ' false = refl
xor-identityʳ' true  = refl

xor-same' : ∀ x → x xor x ≡ false
xor-same' false = refl
xor-same' true  = refl

∧-distribˡ-xor' : _∧_ DistributesOverˡ _xor_
∧-distribˡ-xor' false y z = refl
∧-distribˡ-xor' true  y z = refl

∧-distribʳ-xor' : _∧_ DistributesOverʳ _xor_
∧-distribʳ-xor' x false z = refl
∧-distribʳ-xor' x true false = sym (xor-identityʳ' x)
∧-distribʳ-xor' x true true = sym (xor-same' x)

∧-distrib-xor' : _∧_ DistributesOver _xor_
∧-distrib-xor' = ∧-distribˡ-xor' , ∧-distribʳ-xor'

xor-comm' : Commutative _xor_
xor-comm' false false = refl
xor-comm' false true  = refl
xor-comm' true  false = refl
xor-comm' true  true  = refl

xor-identity' : Identity false _xor_
xor-identity' = xor-identityˡ' , xor-identityʳ'

xor-inverseˡ' : LeftInverse true not _xor_
xor-inverseˡ' false = refl
xor-inverseˡ' true = refl

xor-inverseʳ' : RightInverse true not _xor_
xor-inverseʳ' x = xor-comm' x (not x) ⟨ trans ⟩ xor-inverseˡ' x

xor-inverse' : Inverse true not _xor_
xor-inverse' = xor-inverseˡ' , xor-inverseʳ'

xor-is-ok' : ∀ x y → x xor y ≡ (x ∨ y) ∧ not (x ∧ y)
xor-is-ok' true  y = refl
xor-is-ok' false y = sym (∧-identityʳ _)

xor-assoc' : Associative _xor_
xor-assoc' true  y z = sym (not-distribˡ-xor' y z)
xor-assoc' false y z = refl

-----------------------------------------------------------

open import Data.List
open import Data.Maybe
open import Data.Fin hiding (suc; _+_)
open import Data.Nat
open import Data.Nat.Properties
open import Level hiding (suc)
open import Function.Base using (_$_)
open import Data.List.Properties using (drop-[])
import Data.Nat.GeneralisedArithmetic as ℕ


private
  variable
    a : Level
    A : Set a
    B : Set a
    n : ℕ

find' : (A → Bool) → List A → Maybe A
find' p [] = nothing
find' p (x ∷ xs) = if p x then just x else find' p xs

findIndices' : (A → Bool) → List A → List ℕ
findIndices' {A = A} p = h 0 where
  h : ℕ → List A → List ℕ
  h n [] = []
  h n (x ∷ xs) = if p x then n ∷ h (suc n) xs else h (suc n) xs 

findIndex' : (A → Bool) → (x : List A) → Maybe $ Fin (length x)
findIndex' p [] = nothing
findIndex' p (x ∷ xs) = if p x then just Fin.zero else Data.Maybe.map Fin.suc (findIndex' p xs)

drop-fusion : (n m : ℕ) → (x : List A) → drop n (drop m x) ≡ drop (n + m) x
drop-fusion  ℕ.zero  m x = refl
drop-fusion (suc n) ℕ.zero x rewrite +-identityʳ n = refl
drop-fusion (suc n) (suc m) [] = refl
drop-fusion (suc n) (suc m) (x ∷ xs) rewrite +-suc n m = drop-fusion (suc n) m xs

drop-fusion' : (n m : ℕ) → (xs : List A) → drop n (drop m xs) ≡ drop (m + n) xs
drop-fusion' n ℕ.zero [] = refl
drop-fusion' n (suc m) [] = drop-[] n
drop-fusion' ℕ.zero m (x ∷ xs) rewrite +-identityʳ m = refl
drop-fusion' (suc n) ℕ.zero (x ∷ xs) = refl
drop-fusion' (suc n) (suc m) (x ∷ xs) = drop-fusion' (suc n) m xs

drop-drop : (m n : ℕ) → (xs : List A) → drop n (drop m xs) ≡ drop (m + n) xs
drop-drop zero n xs = refl
drop-drop (suc m) n [] = drop-[] n
drop-drop (suc m) n (x ∷ xs) = drop-drop m n xs

insert-at : (xs : List A) → (i : ℕ) → A → List A
insert-at xs ℕ.zero a = a ∷ xs
insert-at [] (suc i) a = []
insert-at (x ∷ xs) (suc i) a = x ∷ (insert-at xs i a)

insert' : (xs : List A) → (i : Fin (length xs)) → A → List A
insert' (x ∷ xs) Fin.zero    v = v ∷ x ∷ xs
insert' (x ∷ xs) (Fin.suc i) v = v ∷ insert' xs i v

open import Data.Vec using (Vec; toList)
import Data.Vec.Base

_─'_ : Vec A (suc n) → Fin (suc n) → Vec A n
xs ─' i = Data.Vec.remove xs i

delete-at : (xs : List A) → (i : ℕ) → List A
delete-at [] ℕ.zero = []
delete-at (x ∷ xs) ℕ.zero = xs
delete-at [] (suc i) = []
delete-at (x ∷ xs) (suc i) = x ∷ delete-at xs i

delete-at' : (xs : List A) → (i : Fin (length xs)) → List A
delete-at' (x ∷ xs) Fin.zero = xs
delete-at' (x ∷ xs) (Fin.suc i) = x ∷ delete-at' xs i

updateAt' : (xs : List A) → (A → A) → Fin (length xs) → List A
updateAt' (x ∷ xs) f Fin.zero = f x ∷ xs
updateAt' (x ∷ xs) f (Fin.suc k) = x ∷ updateAt' xs f k

iterate' : (A → A) → A → ℕ → List A
iterate' f k ℕ.zero = []
iterate' f k (suc n) = k ∷ iterate' f (f k) n

remove-insert : ∀ (xs : List A) (i : Fin (length xs)) (v : A) (k : Fin (length (insert xs i v))) → remove (insert xs i v) k  ≡ xs
remove-insert x i v k = {!!}
-- remove-insert (x ∷ xs) Fin.zero v Fin.zero = refl
-- remove-insert (x ∷ xs) Fin.zero v (Fin.suc k) = {!!}
-- remove-insert (x ∷ xs) (Fin.suc i) v k = {!!}

-- insert-lookup' : ∀ (xs : List A) (i : Fin (length xs)) (v : A) → let m = Fin.suc i in Data.List.lookup (insert xs m v) m ≡ v
-- insert-lookup' xs       zero     v = refl
-- insert-lookup' (x ∷ xs) (suc i)  v = insert-lookup xs i v

iterate-is-replicate-if-id : ∀ (n : ℕ) (x : A) → iterate' id x n ≡ replicate n x
iterate-is-replicate-if-id  ℕ.zero x = refl
iterate-is-replicate-if-id  (suc n) x = cong (_ ∷_) (iterate-is-replicate-if-id n (id x))

length-iterate' : ∀ (s : A → A) (z : A) n → length (iterate' s z n) ≡ n
length-iterate' s z ℕ.zero = refl
length-iterate' s z (suc n) = cong suc (length-iterate' s (s z) n)

-- iterate-id' : ∀ (n : ℕ) (x : A) → Data.Vec.Base.iterate id x n ≡ Data.Vec.Base.replicate x
-- iterate-id' ℕ.zero x = refl
-- iterate-id' (suc n) x = cong (_ Vec.∷_) (iterate-id' n (id x))

-- vec-list-insert : ∀ (v : A) (xs : Vec A n) (i : Fin (suc n)) (j : Fin (length (toList xs))) → toList (Data.Vec.insert xs i v) ≡ insert (toList xs) j v
-- vec-list-insert v (x Vec.∷ xs) Fin.zero Fin.zero = refl
-- vec-list-insert v (x Vec.∷ xs) Fin.zero (Fin.suc j) = cong (_ ∷_) {!!}
-- vec-list-insert v (x Vec.∷ xs) (Fin.suc i) j = {!!}
