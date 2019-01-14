
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import TSI

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
  {
    "v": 100,
    "signal": 100
  },
  {
    "v": 97.83081856147155,
    "signal": 99.69011693735308
  },
  {
    "v": 96.09561123887346,
    "signal": 99.17661612328456
  },
  {
    "v": 94.33413941078031,
    "signal": 98.48483373578395
  },
  {
    "v": 92.86997281309559,
    "signal": 97.68271074682848
  },
  {
    "v": 91.64292756186009,
    "signal": 96.81988457754728
  },
  {
    "v": 90.59311202079135,
    "signal": 95.93034564086787
  },
  {
    "v": 89.69399615500116,
    "signal": 95.03943857145833
  },
  {
    "v": 88.91742295958501,
    "signal": 94.1648649126193
  },
  {
    "v": 88.24153281310898,
    "signal": 93.31867461268926
  },
  {
    "v": 87.65151617273509,
    "signal": 92.50908054983867
  },
  {
    "v": 87.09042732748053,
    "signal": 91.73498723235895
  },
  {
    "v": 86.59889096876861,
    "signal": 91.0012591947032
  },
  {
    "v": 86.10854376208215,
    "signal": 90.3022998471859
  },
  {
    "v": 85.68208187335505,
    "signal": 89.6422687080672
  },
  {
    "v": 85.15174197120271,
    "signal": 89.00076488851515
  },
  {
    "v": 84.67720151872123,
    "signal": 88.38311297854459
  },
  {
    "v": 84.25902201034529,
    "signal": 87.7939571259447
  },
  {
    "v": 83.76186182370843,
    "signal": 87.21794351133953
  }
]

class TSITest(unittest.TestCase):
  def test_add(self):
    indicator = TSI([25, 13, 13])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
