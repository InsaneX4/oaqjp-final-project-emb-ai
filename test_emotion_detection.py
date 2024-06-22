#Task 5
#1. To run unit tests, create a new file, test_emotion_detection.py that calls the required application function from the package and tests it for the following statements and dominant emotions.
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        key = 'dominant_emotion'
        #Statement: I am glad this happened
        #Dominant Emotion: joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1[key], 'joy')
        #Statement: I am really mad about this
        #Dominant Emotion: anger
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2[key], 'anger')
        #Statement: I feel disgusted just hearing about this
        #Dominant Emotion: disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3[key], 'disgust')
        #Statement: I am so sad about this
        #Dominant Emotion: sadness
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4[key], 'sadness')

unittest.main()