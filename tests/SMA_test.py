
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import SMA

with open('tests/btc_candle_data.json', 'r') as f:
  btcCandleData = json.load(f)
  candles = list(map(lambda candleArray: {
    'mts': candleArray[0],
    'open': candleArray[1],
    'close': candleArray[2],
    'high': candleArray[3],
    'low': candleArray[4],
    'vol': candleArray[5],
    'symbol': 'tBTCUSD',
    'tf': '1min',
  }, btcCandleData))

expected = [
  318.725,
  637.37,
  957.85,
  1278.85,
  1600.2549999999999,
  1921.655,
  2243.06,
  2564.5199999999995,
  2886.1949999999997,
  3207.9299999999994,
  3529.66,
  3851.5699999999997,
  4173.469999999999,
  4495.339999999999,
  4817.109999999999,
  5138.979999999999,
  5460.714999999998,
  5782.559999999999,
  6104.269999999999,
  6426.189999999998,
  6429.399999999998,
  6432.604999999998,
  6433.979999999998,
  6434.749999999998,
  6434.9349999999995,
  6435.124999999999,
  6435.26,
  6435.55,
  6435.625,
  6435.895,
  6435.8150000000005,
  6435.33,
  6434.83,
  6434.405000000001,
  6434.035,
  6433.74,
  6434.155000000001,
  6434.8150000000005,
  6435.65,
  6436.34
]

class SMATest(unittest.TestCase):
  def test_add(self):
    indicator = SMA([20])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
