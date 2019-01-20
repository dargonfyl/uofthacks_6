import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


# takes chunks of text and uses google cloud to keep only sentences with key words in them
def keySentences(text):
    """
    Takes a large chunk of text and returns a list of sentences from it that contain the
    key words of the paragraph.

    :param text: The text to clean up
    :type text:  String
    :return:     The key sentences of the original text
    :rtype:      List of Strings
    """
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    keywords = []

    # currently arbitrary threshold 0.05 to determine importantce
    for entity in entities:
        if entity.salience > 0.05:
            keywords.append(entity.name)

    sentences = text.split('.')
    keysentences = []

    for sentence in sentences:
        for keyword in keywords:
            if keyword in sentence:
                keysentences.append(sentence)
                break

    return keysentences


def remove_some_text(text):
    """
    Removes determinants and adverbs from the text

    :param text: text representing a sentence
    :type text:  String
    :return:     the shortened sentence
    :rtype:      String
    """
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects syntax in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    tokens = client.analyze_syntax(document).tokens

    # part-of-speech tags from enums.PartOfSpeech.Tag
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')
    # DET, ADJ, ADV

    shortenedsentence = ""

    for token in tokens:
        if pos_tag[token.part_of_speech.tag] not in ["DET", "ADV", "PUNCT"]:
            shortenedsentence = shortenedsentence + " " + token.text.content
        elif pos_tag[token.part_of_speech.tag] == 'PUNCT':
            shortenedsentence = shortenedsentence + token.text.content
    return shortenedsentence.strip()


def make_bullet_points(sentences):
    """
    Modifies a list of strings representing sentences and shortens every one to a bullet point

    :param sentences: sentences
    :type sentences:  list of strings
    :return:          void
    :rtype:           none
    """
    for i in range(len(sentences)):
        sentences[i] = remove_some_text(sentences[i])


if __name__ == '__main__':
    sentences = keySentences(
        "The Meiji period, or Meiji era, is a Japanese era which extended from October 23, 1868, to July 30, 1912. This period represents the first half of the Empire of Japan, during which Japanese society moved from being an isolated feudal society to a Westernised form. Fundamental changes affected its social structure, internal politics, economy, military and foreign relations. The period corresponded to the reign of Emperor Meiji and was succeeded upon the accession of Emperor Taishō by the Taishō period.")
    make_bullet_points(sentences)
    print(sentences)
