import sys
import json
from watson_developer_cloud import VisualRecognitionV3
from building.getwikipediaarticle import WikiPage
"""
Input the url link of a picture and get_word will return the best classifier word
for what the picture shows.
"""


def get_word(url):
    """
    Gets the 1-word descriptor of the image of the url
    :param url: the url of the image
    :type url: str
    :return: a 1-word descriptor of the image
    :rtype: str
    """
    visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        iam_apikey='G_vhnFiNCnhp97Uew544e5aF0NfcNzkL-FRWcZ-L_uAq')

    classes_result = visual_recognition.classify(url=url).get_result()
    image = json.dumps(classes_result, indent=2)
    return image.splitlines()[9].strip()[10:-2]


# Testing
if __name__ == "__main__":
    word = get_word(sys.argv[1])
    page = WikiPage(word)
