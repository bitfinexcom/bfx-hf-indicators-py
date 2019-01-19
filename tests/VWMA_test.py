
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import VWMA

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
  6386.583403978712,
  6388.612489771417,
  6423.818801303632,
  6429.581929873887,
  6436.373123301532,
  6436.224030236286,
  6436.080346902601,
  6436.089198400303,
  6435.907291935543,
  6435.863033220089,
  6436.353271800077,
  6436.031144391555,
  6435.804705746815,
  6435.384962200233,
  6434.808716919904,
  6434.341755348134,
  6432.912124039422,
  6433.904772495749,
  6434.815270968256,
  6435.422313110946,
  6435.811016946274
]

class VWMATest(unittest.TestCase):
  def test_add(self):
    indicator = VWMA([20])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
