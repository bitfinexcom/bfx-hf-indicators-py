
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import DC

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
  {
    "upper": 6439.50026496,
    "middle": 6402.75013248,
    "lower": 6366
  },
  {
    "upper": 6439.50026496,
    "middle": 6402.75013248,
    "lower": 6366
  },
  {
    "upper": 6439.50026496,
    "middle": 6422.75013248,
    "lower": 6406
  },
  {
    "upper": 6439.50026496,
    "middle": 6429.75013248,
    "lower": 6420
  },
  {
    "upper": 6439.50026496,
    "middle": 6433.75013248,
    "lower": 6428
  },
  {
    "upper": 6439.50026496,
    "middle": 6433.75013248,
    "lower": 6428
  },
  {
    "upper": 6439.50026496,
    "middle": 6433.75013248,
    "lower": 6428
  },
  {
    "upper": 6439.50026496,
    "middle": 6434.35013248,
    "lower": 6429.2
  },
  {
    "upper": 6439.50026496,
    "middle": 6435.00013248,
    "lower": 6430.5
  },
  {
    "upper": 6441.8,
    "middle": 6436.15,
    "lower": 6430.5
  },
  {
    "upper": 6441.8,
    "middle": 6436.15,
    "lower": 6430.5
  },
  {
    "upper": 6441.8,
    "middle": 6435.15,
    "lower": 6428.5
  },
  {
    "upper": 6441.8,
    "middle": 6435.05,
    "lower": 6428.3
  },
  {
    "upper": 6441.8,
    "middle": 6434.9,
    "lower": 6428
  },
  {
    "upper": 6441.8,
    "middle": 6434.9,
    "lower": 6428
  },
  {
    "upper": 6441.8,
    "middle": 6434.9,
    "lower": 6428
  },
  {
    "upper": 6443,
    "middle": 6435.5,
    "lower": 6428
  },
  {
    "upper": 6450.2,
    "middle": 6439.1,
    "lower": 6428
  },
  {
    "upper": 6450.9,
    "middle": 6439.45,
    "lower": 6428
  },
  {
    "upper": 6452.21967118,
    "middle": 6440.109835589999,
    "lower": 6428
  },
  {
    "upper": 6452.4,
    "middle": 6440.2,
    "lower": 6428
  }
]

class DCTest(unittest.TestCase):
  def test_add(self):
    indicator = DC([20])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
