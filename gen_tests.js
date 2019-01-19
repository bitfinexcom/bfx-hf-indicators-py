const fs = require('fs')
const indicators = require('bfx-hf-indicators')

const SAMPLE_SIZE = 20
const sampleData = JSON.parse(fs.readFileSync('./tests/btc_candle_data.json'))
  .map(([mts, open, close, high, low, vol, symbol]) => 
    ({mts, open, close, high, low, vol, symbol: 'tBTCUSD', tf: '1min'}))

function main() {
  const toSkip = ['Indicator', 'Aroon', 'ADX']
  const toTest = Object.keys(indicators).filter(i => toSkip.indexOf(i) === -1)
  const testClassNames = toTest.map(name => createTestCase(name))
  create__init__(testClassNames)
}

function createTestCase(name) {
  const indicator = indicators[name]
  const initArgs = indicator.args.map((arg) => arg.default)
  const i = new indicator(initArgs)
  const indicatorName = i.constructor.name
  const values = sampleData
    .slice(0, i.getSeedPeriod() + SAMPLE_SIZE)
    .map(row => i.add(i.getDataType() === 'candle' ? row : row.close))

  const body = `
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import ${indicatorName}

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

expected = ${JSON.stringify(values, null, 2).replace(/null/g, 'None')}

class ${indicatorName}Test(unittest.TestCase):
  def test_add(self):
    indicator = ${indicatorName}([${initArgs.join(', ')}])
    for i in range(len(expected)):
      indicator.add(${i.getDataType() === 'candle' ? 'candles[i]' : `candles[i]['close']`})
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
`
  fs.writeFileSync(`tests/${indicatorName}_test.py`,  body)
  return indicatorName
}

function create__init__(testClassNames) {
  const __init__body = `
name = 'tests'

${testClassNames.map(cn => `from tests.${cn}_test import ${cn}Test`).join('\n')}
`

  fs.writeFileSync('tests/__init__.py', __init__body)
}

main()