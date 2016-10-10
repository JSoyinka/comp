from datetime import date
from PIL import Image

class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError


# TODO: Define an Article class that extends the Content class
class Article(Content):

    def __init__(self, year, month, day, contributors, headline, content):
        # Set headline
        Content.__init__(self, year, month, day, contributors)
        self.headline = headline

        # Set string repres of content of the article
        self.content = content

    # Show propertiesb
    def show(self):
        print "Headline: {0}".format(self.headline)
        print "Contributors: {0}".format(", ".join(self.contributors))
        print "Date: {0}".format(self.creation_date.strftime("%B %d, %Y"))
        print "Content: {0}".format(self.content)

article_example = Article(2016, 9, 16, ["Jarele Soyinka", "Harambe", "Kanye West"], "Dank Maymays", "Are you ready to #FeelTheBern?")
article_example.show()


# TODO: Define a Picture class that extends the Content class
class Picture(Content):

    def __init__(self, year, month, day, contributors, title, caption, path):
        # Set title
        Content.__init__(self, year, month, day, contributors)
        self.title = title

        # Set catpotion
        self.caption = caption

        # Set path for picture
        self.path = path

    # Show properties
    def show(self):
        print "Title: {0}".format(self.title)
        print "Contributors: {0}".format(", ".join(self.contributors))
        print "Date: {0}".format(self.creation_date.strftime("%B %d, %Y"))
        Image.open(self.path).show()
        print "Caption: {0}".format(self.caption)

picture_example = Picture(2016, 9, 16, ["Jarele Soyinka", "Harambe", "Kanye West"], 
    "Dank Maymays", "Ain't that a sexy gif!", "sexy.gif")
picture_example.show()
