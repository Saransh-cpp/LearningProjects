{-# OPTIONS --exact-split #-}

module test where

data ℕ : Set where
  zero : ℕ
  suc  : ℕ → ℕ

{-# BUILTIN NATURAL ℕ #-}

open import Function.Bijection using (from)
