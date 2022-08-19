const express = require('express')
const app = express()
const port = 7865

app.get('/', (req, res) => {
  res.status(200)
  res.send('Welcome to the payment system')
})

app.get('/cart/:id', (req, res) => {
  const { id } = req.params
  console.log(parseInt(id))
  if (isNaN(parseInt(id))) {
    res.status(404)
    res.send("Not a number")
  } else {
    res.status(200)
    res.send(`Payment methods for cart ${id}`)
  }
})

app.listen(port, () => {
  console.log(`API available on localhost port 7865`)
})
