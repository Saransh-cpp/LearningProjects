data Bool : Set where
  true false : Bool

not : Bool → Bool
not true = false
not false = true

not' : Bool → Bool
not' true = false
not' false = true

idBool : Bool → Bool
idBool x = x

idBool' : Bool → Bool
idBool' = λ x → x

idBool'' : Bool → Bool
idBool'' = λ (x : Bool) → x

id' : (X : Set) → X → X
id' X x = x

id : {X : Set} → X → X
id = λ x → x

example : {P Q : Set} → P → (Q → P)
example {P} {Q} p = f
  where
    f : Q → P
    f _ = p

example' : {P Q  : Set} → P → (Q → P)
example' p = λ q → p

data ℕ : Set where
  zero : ℕ
  suc  : ℕ → ℕ

three : ℕ
three = suc (suc (suc zero))

{-# BUILTIN NATURAL ℕ #-}

three' : ℕ
three' = 3

D : Bool → Set
D true = ℕ
D false = Bool

if_then_else_ : {X : Set} → Bool → X → X → X
if true then x else y = x
if false then x else y = y
