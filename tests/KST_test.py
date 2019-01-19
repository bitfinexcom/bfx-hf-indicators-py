
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import KST

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
    "v": 0.8135116240261576,
    "signal": 0.09039018044735085
  },
  {
    "v": 0.6409155280115051,
    "signal": 0.16160301689307366
  },
  {
    "v": 0.47718857550834715,
    "signal": 0.21462396972733444
  },
  {
    "v": 0.3732069166013645,
    "signal": 0.25609140490526383
  },
  {
    "v": 0.2974208283650136,
    "signal": 0.28913816361248756
  },
  {
    "v": 0.261281073466648,
    "signal": 0.3181693939976707
  },
  {
    "v": 0.4158506383783419,
    "signal": 0.36437502048415316
  },
  {
    "v": 0.6131224137815969,
    "signal": 0.4324997331265528
  },
  {
    "v": 0.8352081675292657,
    "signal": 0.5253006406298045
  },
  {
    "v": 1.0118335342921159,
    "signal": 0.5473364084371332
  },
  {
    "v": 1.2682433324075277,
    "signal": 0.6170394978144691
  },
  {
    "v": 1.5754735640738626,
    "signal": 0.7390711632106375
  },
  {
    "v": 1.886851188089103,
    "signal": 0.9072538600426083
  },
  {
    "v": 2.186404048093756,
    "signal": 1.117140884456913
  },
  {
    "v": 2.534127243779749,
    "signal": 1.3696793478250353
  },
  {
    "v": 2.6148570259511272,
    "signal": 1.6140133908886785
  },
  {
    "v": 2.5918617653249356,
    "signal": 1.8338733188379384
  },
  {
    "v": 2.649762023801279,
    "signal": 2.0354904139792733
  },
  {
    "v": 2.676439036923101,
    "signal": 2.220446580938271
  },
  {
    "v": 2.691963561560622,
    "signal": 2.3786377175108373
  },
  {
    "v": 2.7049816720983584,
    "signal": 2.504138618402448
  },
  {
    "v": 2.6772504021572647,
    "signal": 2.59196075329891
  },
  {
    "v": 2.542962651141183,
    "signal": 2.631578375859735
  },
  {
    "v": 2.463089355275181,
    "signal": 2.623685277137005
  },
  {
    "v": 2.44732452364339,
    "signal": 2.6050705546583677
  },
  {
    "v": 2.4075305650376313,
    "signal": 2.5845893101820008
  },
  {
    "v": 2.3318998600545484,
    "signal": 2.54927129198792
  },
  {
    "v": 2.355743997806086,
    "signal": 2.5136385098638074
  },
  {
    "v": 2.4675786508768427,
    "signal": 2.488706853121165
  },
  {
    "v": 2.5587421059573594,
    "signal": 2.4724580124388322
  },
  {
    "v": 2.6580288963775436,
    "signal": 2.4703222895744186
  },
  {
    "v": 2.7541567100938362,
    "signal": 2.4937882961247135
  },
  {
    "v": 2.938056693339835,
    "signal": 2.546562444798563
  },
  {
    "v": 3.09018510147979,
    "signal": 2.6179913978914966
  },
  {
    "v": 3.175292337849494,
    "signal": 2.7032982615372596
  }
]

class KSTTest(unittest.TestCase):
  def test_add(self):
    indicator = KST([10, 15, 20, 30, 10, 10, 10, 15, 9])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
