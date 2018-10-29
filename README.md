## HF Indicators: `bfxhfindicators`

This repo contains a collection of trading indicators implemented to support incremental updates, both from trade and candle data (depending on the indicator). All indicators provide the same set of base methods:

* `reset()` - clears indicator values
* `update(value or candle)` - updates the current indicator value with a different data point
* `add(value or candle)` - adds a new data point/value to the indicator
* `l()` - returns the number of available indicator values
* `v()` - returns the current indicator value
* `prev(n = 1)` - returns the nth previous indicator value

#### Indicator Seeding

All indicators have a seed period which should be respected before valid data can be obtained, which can be read via `i.get_seed_period()`

#### Indicator Data Types

To query which type of data an indicator requires, `get_data_type()` and `get_data_key()` are available. The data type can be either `'trade'`, `'candle'`, or `'*'` to signal that both are acceptable. For candle data, the data key will be either `'open`', `'high'`, `'low'`, or `'close'`.

## Example Usage

```js
from bfxhfindicators import RSI

rsi = RSI([14])

rsi.add(14000)
rsi.add(14010)
rsi.add(14025)
rsi.add(14035)
// ...
// 8 more data points
// ...
rsi.add(13998)
rsi.add(13952)

v = rsi.v() // query current RSI(14) value
```

## Available Indicators
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
