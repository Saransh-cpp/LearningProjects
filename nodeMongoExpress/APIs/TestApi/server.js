const express = require('express');

const app = express();

const PORT = 3000;

app.get('/', (req, res) => {
    res.json({
        a: 5,
        b: 6,
    })
})

app.listen(PORT, () => {
    console.log('listening');
})