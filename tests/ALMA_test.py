
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import ALMA

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
  6436.315492726009,
  6436.568195974886,
  6436.699859274552,
  6436.844822498113,
  6436.796550373987,
  6436.29990160522,
  6435.659104229977,
  6434.824352086071,
  6434.394359507538,
  6434.10537482829,
  6434.52244225582,
  6434.465694283258,
  6433.95760796234,
  6433.256488509599,
  6432.505866590178,
  6431.601457733116,
  6431.071699302555,
  6431.921871769848,
  6433.9767971400615,
  6436.61390723641,
  6439.647515302738
]

class ALMATest(unittest.TestCase):
  def test_add(self):
    indicator = ALMA([20, 0.86, 6])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
