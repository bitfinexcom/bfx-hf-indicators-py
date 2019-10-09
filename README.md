# Bitfinex Indicator Library for Python

[![Build Status](https://travis-ci.org/bitfinexcom/bfx-hf-indicators-py.svg?branch=master)](https://travis-ci.org/bitfinexcom/bfx-hf-indicators-py)

This repo contains a collection of trading indicators implemented to support incremental updates, both from trade and candle data (depending on the indicator). All indicators provide the same set of base methods:

## Features
* Absolute True Range
* Acceleration
* Accumulation/Distribution
* Accumulative Swing Index
* Arnoud Legoux Moving Average
* Awesome Oscillator
* Balance of Power
* Bollinger Bands
* Chaikin Money Flow
* Chaikin Oscillator
* Chande Momentum Oscillator
* Coppock Curve
* Detrended Price Oscillator
* Donchian Channels
* Ease of Movement
* Envelope
* Exponential Moving Average
* EMA Volume
* Know Sure Thing
* MACD
* Mass Index
* Momentum
* Net Volume
* On Balance Volume
* Price Channel
* Price Oscillator
* Price Volume Trend
* RSI
* Rate of Change
* Relative Vigor Index
* Relative Volatility Index
* Simple Moving Average
* Standard Deviation
* Stochastic
* Stochastic RSI
* TRIX
* True Strength Index
* VWAP
* Volume Oscillator
* Volume Weighted Moving Average
* Weighted Moving Average
* Williams %R

## Installation

Clone package into PYTHONPATH:
```sh
git clone https://github.com/bitfinexcom/bfx-hf-indicators-py.git
cd bfx-hf-indicators-py
```

Or via pip/pip3:
```sh
pip3 install -r requirements.txt
python3 setup.py install
```

## Quickstart

```python
from bfxhfindicators import RSI

rsi = RSI([14])

rsi.add(14000)
rsi.add(14010)
rsi.add(14025)
rsi.add(14035)
# ...
# 8 more data points
# ...
rsi.add(13998)
rsi.add(13952)

v = rsi.v() # query current RSI(14) value
```

## Docs

* <b>[Usages](docs/usages.md)</b> - Documentation

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
