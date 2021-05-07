import express from 'express'
import mongoose from 'mongoose'
import Cards from './dbCards.js'
import Cors from 'cors'

// App config
const app = express()
const port = process.env.PORT || 8001
const connection_url = `mongodb+srv://admin:zQRgAQpCKe44jtB@cluster0.itixv.mongodb.net/tinderDB?retryWrites=true&w=majority`

// Middlewares
app.use(express.json())

// DB Config
mongoose.connect(connection_url, {
    useNewUrlParser: true,
    useCreateIndex: true,
    useUnifiedTopology: true,
})

// API Endpoints
// app.get('/', (req, res) => res.send("hello world"))
app.use(Cors())

app.post('/tinder/cards', (req, res) => {
    const dbCard = req.body

    Cards.create(dbCard, (err, data) => {
        if (err) {
            res.status(500).send(err)
        } else {
            res.status(201).send(data)
        }
    })
})

app.get('/tinder/cards', (req, res) => {
    const dbCard = req.body
    Cards.find(dbCard, (err, data) => {
        if (err) {
            res.status(500).send(err)
        } else {
            res.status(200).send(data)
        }
    })
})

// Listener
app.listen(port, () => console.log(`Listening`))