# Takes word and gets the wikipedia article of it

# Takes wikipedia article and extracts all important text from it

import wikipedia


class WikiPage:
    """
    Gets wikipedia page information wiht wikipedia api
    """

    def __init__(self, entry_name: str):
        self.entry_name = entry_name
        self.success = 0
        self.entry = self.parse_page(entry_name)

    def parse_page(self, entry_name):
        """
        If entry is ambiguous, always choose first option
        """
        try:
            entry = wikipedia.page(entry_name)
            self.success = 1
        except wikipedia.exceptions.DisambiguationError as e:
            entry = wikipedia.page(e.options[0])
            self.success = 1
        except wikipedia.exceptions.PageError as e:
            print(e)
            return None
        except wikipedia.exceptions.RedirectError as e:
            print(e)
            return None
        except wikipedia.exceptions.HTTPTimeoutError as e:
            print(e)
            return None
        except Exception as e:
            print(e)
            return None
        return entry

    def get_summary_full(self):
        """
        Return summary of wiki article
        """
        if self.success == 1:
            return self.entry.summary.strip()
        else:
            return "Wikipedia Article Error!"

    def get_url(self):
        """
        Returns url of wiki article
        """
        if self.success == 1:
            return self.entry.url
        else:
            return "Wikipedia Article Error!"

    def get_img_url(self):
        """
        Gets image url
        """
        if self.success == 1:
            return self.entry.images[0]
        else:
            return "Wikipedia Article Error!"


# testing
# if __name__ == "__main__":
#     w = WikiPage("Mercury")
#     print(w.get_img_url())