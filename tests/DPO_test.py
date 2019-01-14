
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import DPO

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
  2.988201482857143,
  -16.63718297047619,
  -12.395644385238096,
  -19.284218841428572,
  -8.09618009238095,
  -19.676146442857142,
  -19.669560936190475,
  -13.352349688571428,
  -21.212542774761904
]

class DPOTest(unittest.TestCase):
  def test_add(self):
    indicator = DPO([21])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
