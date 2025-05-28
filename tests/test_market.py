import unittest
from mexc.market import get_eth_price, get_market_sentiment

class TestMarketFunctions(unittest.TestCase):
    def test_get_eth_price(self):
        price = get_eth_price()
        self.assertIsInstance(price, float)
        self.assertGreater(price, 0)

    def test_get_market_sentiment(self):
        sentiment = get_market_sentiment()
        self.assertIn(sentiment, ["bullish", "bearish", "neutral"])

if __name__ == "__main__":
    unittest.main()
