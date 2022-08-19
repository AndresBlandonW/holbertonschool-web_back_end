const express = require('express')
const app = express()
const port = 7865

app.use(express.json())

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

app.get('/available_payments', (req, res) => {
  res.status(200)
  res.send({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  })
})

app.post('/login', (req, res) => {
  const { userName } = req.body
  if (userName) {
    res.status(200)
    res.send(`Welcome ${userName}`)
  } else {
    res.status(404)
    res.end()
  }
})

app.listen(port, () => {
  console.log(`API available on localhost port 7865`)
})
