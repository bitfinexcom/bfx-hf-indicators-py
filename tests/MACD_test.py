
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import MACD

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
  {
    "macd": 0,
    "signal": 0,
    "histogram": 0
  },
  {
    "macd": 23.05045314643874,
    "signal": 4.610090629287749,
    "histogram": 18.440362517150994
  },
  {
    "macd": 18.100253229871512,
    "signal": 7.308123149404501,
    "histogram": 10.792130080467011
  },
  {
    "macd": 14.32894710253396,
    "signal": 8.712287940030393,
    "histogram": 5.6166591625035664
  },
  {
    "macd": 7.5971272213147,
    "signal": 8.489255796287255,
    "histogram": -0.8921285749725545
  },
  {
    "macd": 2.1562982287775085,
    "signal": 7.222664282785305,
    "histogram": -5.066366054007797
  },
  {
    "macd": -2.0051166275838597,
    "signal": 5.377108100711473,
    "histogram": -7.382224728295332
  },
  {
    "macd": -5.329907652281975,
    "signal": 3.2357049501127833,
    "histogram": -8.565612602394758
  },
  {
    "macd": -7.832149994455346,
    "signal": 1.0221339611991573,
    "histogram": -8.854283955654504
  },
  {
    "macd": -9.661308800152945,
    "signal": -1.114554591071263,
    "histogram": -8.546754209081682
  },
  {
    "macd": -10.979864753788917,
    "signal": -3.087616623614794,
    "histogram": -7.8922481301741225
  },
  {
    "macd": -11.630684790241162,
    "signal": -4.796230256940068,
    "histogram": -6.834454533301094
  },
  {
    "macd": -12.329396363641166,
    "signal": -6.302863478280289,
    "histogram": -6.0265328853608775
  },
  {
    "macd": -12.236943112787708,
    "signal": -7.489679405181773,
    "histogram": -4.747263707605935
  },
  {
    "macd": -12.3986369440246,
    "signal": -8.47147091295034,
    "histogram": -3.927166031074261
  },
  {
    "macd": -11.487682879107357,
    "signal": -9.074713306181742,
    "histogram": -2.412969572925615
  },
  {
    "macd": -11.566778677145328,
    "signal": -9.573126380374461,
    "histogram": -1.9936522967708665
  },
  {
    "macd": -11.490373846808748,
    "signal": -9.956575873661318,
    "histogram": -1.5337979731474292
  },
  {
    "macd": -10.793752895441811,
    "signal": -10.124011278017417,
    "histogram": -0.6697416174243944
  },
  {
    "macd": -10.748111590006843,
    "signal": -10.248831340415302,
    "histogram": -0.49928024959154094
  }
]

class MACDTest(unittest.TestCase):
  def test_add(self):
    indicator = MACD([12, 26, 9])
    for i in range(len(expected)):
      indicator.add(candles[i]['vol'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
