const axios = require('./axios');

async function fetchData() {
    const req = await axios.get('/');

    console.log(req.data);
}

fetchData();