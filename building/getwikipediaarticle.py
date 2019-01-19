# Takes word and gets the wikipedia article of it

# Takes wikipedia article and extracts all important text from it

import wikipedia


class WikiPage:
    """
    Gets wikipedia page information wiht wikipedia api
    """

    def __init__(self, entry_name: str):
        self.entry_name = entry_name
        try:
            self.entry = self.parse_page(entry_name)
        except Exception:
            raise WikiPageException("Wikipedia Article Error!")
        self.summary_paragraph_counter = 0

    def parse_page(self, entry_name):
        """
        If entry is ambiguous, always choose first option
        """
        try:
            entry = wikipedia.page(entry_name)
        except wikipedia.exceptions.DisambiguationError as e:
            entry = wikipedia.page(e.options[0])
        except wikipedia.exceptions.PageError as e:
            print(e)
            raise e
        except wikipedia.exceptions.RedirectError as e:
            print(e)
            raise e
        except wikipedia.exceptions.HTTPTimeoutError as e:
            print(e)
            raise e
        except Exception as e:
            print(e)
            raise e
        return entry

    def get_summary_full(self):
        """
        Return summary of wiki article
        """
        return self.entry.summary.strip()

    def get_summary_first_paragraph(self):
        """
        Return first paragraph of wiki article
        """
        self.summary_paragraph_counter += 1
        return self.entry.summary.split("\n")[0]

    def get_summary_next_paragraph(self):
        """
        Returns paragraph number self.summary_paragraph_counter
        """
        max = len(self.entry.summary.split("\n"))
        if self.summary_paragraph_counter < max:
            ret = self.entry.summary.split("\n")[self.summary_paragraph_counter]
            while len(ret) == 0:
                self.summary_paragraph_counter += 1
                ret = self.entry.summary.split("\n")[self.summary_paragraph_counter]
            self.summary_paragraph_counter += 1
            return ret
        else:
            return "****     END OF SUMMARY -------- *********************"

    def get_url(self):
        """
        Returns url of wiki article
        """
        return self.entry.url

    def get_img_url(self):
        """
        Gets image url. Empty string if no images
        """
        return self.entry.images[0] if len(self.entry.images) > 0 else ""

    def get_img_list(self):
        """
        Return a list of images urls found on the page.
        """
        return self.entry.images if len(self.entry.images) > 0 else ""


class WikiPageException(Exception):
    """"uguu we made a fucky wucky"""
    pass


if __name__ == "__main__":
    w = WikiPage("Table")
    print(w.get_img_url())
    print(w.get_summary_next_paragraph())
    print(w.get_summary_next_paragraph())
    print(w.get_summary_next_paragraph())
    print(w.get_summary_next_paragraph())
    print(w.get_summary_next_paragraph())
    print(w.get_summary_next_paragraph())
    print(w.get_summary_next_paragraph())
    print(w.get_summary_next_paragraph())
    print(w.get_summary_next_paragraph())
    print(w.get_summary_next_paragraph())
    print(w.get_summary_next_paragraph())
    # print(w.entry.content)
    # print(w.entry.section())
    # print(w.entry.sections)
