
import unittest
import sys
import json

sys.path.append('../')
from tests.util import assertFloatEqual
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
    "v": -100,
    "signal": -100
  },
  {
    "v": -59.38018815717329,
    "signal": -94.19716973673906
  },
  {
    "v": -30.162236656779434,
    "signal": -85.04932215388769
  },
  {
    "v": -9.338338767481606,
    "signal": -74.23346738440111
  },
  {
    "v": 3.587801686876255,
    "signal": -63.11614323136149
  },
  {
    "v": 12.413760846076368,
    "signal": -52.32615693458465
  },
  {
    "v": 19.08394520180659,
    "signal": -42.12471377224305
  },
  {
    "v": 25.12767179613261,
    "signal": -32.517230119617956
  },
  {
    "v": 29.96692154584753,
    "signal": -23.590922738837175
  },
  {
    "v": 33.68044991901565,
    "signal": -15.409298073429632
  },
  {
    "v": 37.35054107060119,
    "signal": -7.872178195710943
  },
  {
    "v": 40.185471181239826,
    "signal": -1.0067997132894053
  },
  {
    "v": 42.21448404834032,
    "signal": 5.1676693955148405
  },
  {
    "v": 42.94672357007991,
    "signal": 10.564677134738421
  },
  {
    "v": 43.92652445016242,
    "signal": 15.330655322656135
  },
  {
    "v": 43.41637750354782,
    "signal": 19.342901348497804
  },
  {
    "v": 43.42675211961122,
    "signal": 22.783451458656863
  },
  {
    "v": 42.082589420761785,
    "signal": 25.540471167529
  },
  {
    "v": 41.84997500462164,
    "signal": 27.87040028711366
  },
  {
    "v": 41.72363550036174,
    "signal": 29.849433889006242
  },
  {
    "v": 40.74012724168249,
    "signal": 31.40524722510285
  },
  {
    "v": 39.94870334303947,
    "signal": 32.625740956236655
  },
  {
    "v": 38.37449878776919,
    "signal": 33.44699207502702
  },
  {
    "v": 35.12329456164076,
    "signal": 33.686463858828986
  },
  {
    "v": 32.43655228777558,
    "signal": 33.50790506296422
  },
  {
    "v": 29.647052902872833,
    "signal": 32.95635475437974
  },
  {
    "v": 28.580840971009795,
    "signal": 32.33128135675546
  },
  {
    "v": 27.70256374597887,
    "signal": 31.67003598378738
  },
  {
    "v": 28.583453134246533,
    "signal": 31.229095576710115
  },
  {
    "v": 25.36976103871073,
    "signal": 30.39204778556735
  },
  {
    "v": 20.534687699964753,
    "signal": 28.983853487624124
  },
  {
    "v": 16.547208521079522,
    "signal": 27.207189920974898
  },
  {
    "v": 13.715136859057367,
    "signal": 25.279753769272393
  },
  {
    "v": 11.013092096000475,
    "signal": 23.241659244519266
  },
  {
    "v": 10.169517218918113,
    "signal": 21.374210383719102
  },
  {
    "v": 13.762775317285763,
    "signal": 20.28686251708577
  },
  {
    "v": 18.797867718701983,
    "signal": 20.07414897445952
  },
  {
    "v": 22.762650826018856,
    "signal": 20.458220667539422
  },
  {
    "v": 26.156489514200327,
    "signal": 21.272259074205266
  },
  {
    "v": 28.70715337578699,
    "signal": 22.334386831574086
  },
  {
    "v": 30.744864789241827,
    "signal": 23.53588368266948
  },
  {
    "v": 32.511021112868846,
    "signal": 24.81804617269796
  },
  {
    "v": 33.996900571548004,
    "signal": 26.1293110868194
  },
  {
    "v": 35.84766399077184,
    "signal": 27.517647215955463
  }
]

class TSITest(unittest.TestCase):
  def test_add(self):
    indicator = TSI([25, 13, 13])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      assertFloatEqual(self, indicator.v(), expected[i], 'candles[%d]' % i)

if __name__ == '__main__':
    unittest.main()
  
