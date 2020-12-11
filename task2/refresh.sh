#!/usr/bin/env bash

while true; do
  curl "https://api.currencyfreaks.com/latest?apikey=0c764a25ede24db0b1906c5c9ff9e016" > gateway/data.json
  sleep 60
done