
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import PC

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
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  {
    "upper": 6439.50026496,
    "lower": 6366,
    "center": 6402.75013248
  },
  {
    "upper": 6439.50026496,
    "lower": 6366,
    "center": 6402.75013248
  },
  {
    "upper": 6439.50026496,
    "lower": 6406,
    "center": 6422.75013248
  },
  {
    "upper": 6439.50026496,
    "lower": 6420,
    "center": 6429.75013248
  },
  {
    "upper": 6439.50026496,
    "lower": 6428,
    "center": 6433.75013248
  },
  {
    "upper": 6439.50026496,
    "lower": 6428,
    "center": 6433.75013248
  },
  {
    "upper": 6439.50026496,
    "lower": 6428,
    "center": 6433.75013248
  },
  {
    "upper": 6439.50026496,
    "lower": 6429.2,
    "center": 6434.35013248
  },
  {
    "upper": 6439.50026496,
    "lower": 6430.5,
    "center": 6435.00013248
  },
  {
    "upper": 6441.8,
    "lower": 6430.5,
    "center": 6436.15
  },
  {
    "upper": 6441.8,
    "lower": 6430.5,
    "center": 6436.15
  },
  {
    "upper": 6441.8,
    "lower": 6428.5,
    "center": 6435.15
  },
  {
    "upper": 6441.8,
    "lower": 6428.3,
    "center": 6435.05
  },
  {
    "upper": 6441.8,
    "lower": 6428,
    "center": 6434.9
  },
  {
    "upper": 6441.8,
    "lower": 6428,
    "center": 6434.9
  },
  {
    "upper": 6441.8,
    "lower": 6428,
    "center": 6434.9
  },
  {
    "upper": 6443,
    "lower": 6428,
    "center": 6435.5
  },
  {
    "upper": 6450.2,
    "lower": 6428,
    "center": 6439.1
  },
  {
    "upper": 6450.9,
    "lower": 6428,
    "center": 6439.45
  },
  {
    "upper": 6452.21967118,
    "lower": 6428,
    "center": 6440.109835589999
  }
]

class PCTest(unittest.TestCase):
  def test_add(self):
    indicator = PC([20, 1])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
