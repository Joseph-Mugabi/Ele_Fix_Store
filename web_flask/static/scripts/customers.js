#!/usr/bin/node
const fetch = require('node-fetch');
const http = require('http');
import 'whatwg-fetch';
const url = 'http://127.0.0.1:5001/api/v1/customers';

const data = {
  name: 'John Doe',
  gender: 'Male'
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
