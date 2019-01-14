
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import RVGI

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
  {
    "rvi": -0.7701863354037314,
    "signal": 0
  },
  {
    "rvi": -0.7960222016651246,
    "signal": 0
  },
  {
    "rvi": -0.8054316984191281,
    "signal": 0
  },
  {
    "rvi": -0.8112819639484881,
    "signal": 0
  },
  {
    "rvi": -0.8139619230738767,
    "signal": -0.7978426764410189
  },
  {
    "rvi": -0.8195736370729655,
    "signal": -0.8081705272455537
  },
  {
    "rvi": -0.8243404952600875,
    "signal": -0.8133766612873242
  },
  {
    "rvi": -0.8255008517516522,
    "signal": -0.8173089893323041
  },
  {
    "rvi": -0.8045112336666148,
    "signal": -0.8177169035677663
  },
  {
    "rvi": -0.7607364687398,
    "signal": -0.8133321333060408
  },
  {
    "rvi": -0.6462854568460251,
    "signal": -0.7884416871571077
  },
  {
    "rvi": -0.3845891422272648,
    "signal": -0.7234308997986244
  },
  {
    "rvi": -0.1802226403403874,
    "signal": -0.6331296208631088
  },
  {
    "rvi": -0.09158715985916989,
    "signal": -0.4856788044575916
  },
  {
    "rvi": -0.041318140427598224,
    "signal": -0.3028711937348213
  },
  {
    "rvi": 0.01976314942753317,
    "signal": -0.15140759886647437
  },
  {
    "rvi": 0.05131934463834452,
    "signal": -0.06578564937926318
  }
]

class RVGITest(unittest.TestCase):
  def test_add(self):
    indicator = RVGI([10])
    for i in range(len(expected)):
      indicator.add(candles[i])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
