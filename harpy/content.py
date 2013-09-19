class Content(object):

    def __init__(self, raw):
        self.raw = raw

        self.size = self.raw["size"]

        for field in ["compression", "mimeType", "text",
                      "encoding", "comment"]:
            setattr(self, field, self.raw.get(field, ""))
