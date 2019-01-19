
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import CMF

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
  -0.5038499805507273,
  -0.5728014611030653,
  -0.34277592287173075,
  -0.28233746969172197,
  0.23987056575170584,
  0.2734615997600808,
  0.2972801576387625,
  0.28186894835207377,
  0.031010505592867207,
  -0.036975692108663735,
  0.06216839181734157,
  0.16710584483448948,
  0.14786712236227106,
  0.08536912470975525,
  0.12544366326974118,
  0.07048516128787449,
  -0.3536656212872664,
  -0.38811324273419257,
  -0.42296533671737935,
  -0.4087166268553259,
  -0.4027683416748519
]

class CMFTest(unittest.TestCase):
  def test_add(self):
    indicator = CMF([20])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
