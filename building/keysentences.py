import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# takes chunks of text and uses google cloud to keep only sentences with key words in them
def keySentences(text):
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

    # the list of keywords with salience above 0
    keywords = []

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

# removes unnecessary words from sentences to strip it down as much as possible


# return a list of strings


if __name__ == '__main__':
    print(keySentences("The Meiji period, or Meiji era, is a Japanese era which extended from October 23, 1868, to July 30, 1912. This period represents the first half of the Empire of Japan, during which Japanese society moved from being an isolated feudal society to a Westernised form. Fundamental changes affected its social structure, internal politics, economy, military and foreign relations. The period corresponded to the reign of Emperor Meiji and was succeeded upon the accession of Emperor Taishō by the Taishō period. "))
