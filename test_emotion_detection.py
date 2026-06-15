"""Unit tests for emotion detection module."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector function."""

    def test_emotion_detector(self):
        """Test that emotion_detector returns all required keys."""
        result = emotion_detector("I love this new technology.")
        self.assertIn('anger', result)
        self.assertIn('disgust', result)
        self.assertIn('fear', result)
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('dominant_emotion', result)


if __name__ == '__main__':
    unittest.main()
