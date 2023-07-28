open import Data.String.Base using (String)
open import Data.List.Base using (_∷_)
open import Agda.Builtin.Reflection using (Precedence)

showsPrec : Precedence → String → String
showsPrec prec (x ∷ xs) = "Hello" 
