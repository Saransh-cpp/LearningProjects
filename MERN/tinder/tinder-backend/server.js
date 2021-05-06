import express from 'express'
import mongoose from 'mongoose'

// App config
const app = express()
const port = process.env.PORT || 8001

// Middlewares

// DB Config

// API Endpoints
app.get('/', (req, res) => res.send("hello world"))

// Listener
app.listen(port, () => console.log(`Listening`))