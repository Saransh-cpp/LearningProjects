data ℕ : Set where
  zero : ℕ
  suc  : ℕ → ℕ

data Bool : Set where
  true false : Bool

_+_ : ℕ → ℕ → ℕ
zero + n  = n
suc m + n = suc (m + n)

id : {A : Set} → A → A
id x = x

if_then_else : {A : Set} → Bool → A → A → A
if true then x else y = x
if false then x else y = y

data List (A : Set) : Set where
  [] : List A
  _::_ : A → List A → List A

data _×_ (A B : Set) : Set where
  _,_ : A → B → A × B

fst : {A B : Set} → A → B → A
fst a b = a

snd : {A B : Set} → A → B → B 
snd a b = b

data Vec (A : Set) : ℕ → Set where
  [] : Vec A zero
  _::_ : ∀ {n} → A → Vec A n → Vec A (suc n)
infixr 5 _::_

{-# BUILTIN NATURAL ℕ #-}

myVec1 : Vec ℕ 5
myVec1 = 1 :: 2 :: 3 :: 4 :: 5 :: []

zeroes : (n : ℕ) → Vec ℕ n
zeroes zero    = []
zeroes (suc n) = 0 :: zeroes n

_++Vec_ : {A : Set} {m n : ℕ} → Vec A m → Vec A n → Vec A (m + n)
[] ++Vec ys = ys
(x :: xs) ++Vec ys = x :: (xs ++Vec ys)

-- head : {A : Set} {n : ℕ} → Vec A n → Maybe A
-- head (x :: xs) = just x
-- head [] = nothing

data ⊤ : Set where
  tt : ⊤

data ⊥ : Set where

absurd : {A : Set} → ⊥ → A
absurd ()

proof1 : {P : Set} → P → P
proof1 p = p

-- proof2 : {P Q R : Set} → (P → Q) × (Q → R) → (P → R)
-- proof2 f g = λ x → g (f x)

data IsEven : ℕ → Set where
  zeroIsEven : IsEven zero
  sucsucIsEven : ∀ {n} → IsEven n → IsEven (suc (suc n))

6-is-even : IsEven 6
6-is-even = sucsucIsEven (sucsucIsEven (sucsucIsEven zeroIsEven))

data IsTrue : Bool → Set where
  TrueIsTrue : IsTrue true

_=ℕ_ : ℕ → ℕ → Bool
zero =ℕ zero = true
suc m =ℕ suc n = m =ℕ n
_ =ℕ _ = false

length-is-3 : IsTrue(3 =ℕ 3)
length-is-3 = TrueIsTrue

double : ℕ → ℕ
double zero = zero
double (suc n) = suc (suc (double n))

double-is-even : (n : ℕ) → IsEven (double n)
double-is-even zero = zeroIsEven
double-is-even (suc m) = sucsucIsEven (double-is-even m)

n=n : (n : ℕ) → IsTrue (n =ℕ n)
n=n zero = TrueIsTrue
n=n (suc n) = n=n n

data _≡_ {A : Set} : A → A → Set where
  refl : {x : A} → x ≡ x
infix 4 _≡_

-- 1+1 : 1 + 1 = 2
-- 1+1 = refl

-- id-returns-input : {A : Set} → (x : A) → id x ≡ x
-- id-returns-input = refl

data Tree (A : Set) : Set where
  leaf : A → Tree A
  node : Tree A → Tree A → Tree A

-- flatten : {A : Set} → Tree A → List A
-- flatten (leaf x) = [ x ]
-- flatten (node t1 t2) = flatten t1 ++ flaten t2
