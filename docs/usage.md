# Usages

* `cache_size` - indicate the fixed size of internal deque
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

