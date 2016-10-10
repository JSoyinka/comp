from models import Content, Article, Picture
import json


def to_json():
    """
    Write Content.existing_content using json into dump.txt
    for retrieval later.
    """
    # A list of all the content objects serialized into dictionaries
    all_content_dicts = []

    # do for every existing Content object
    for obj in Content.existing_content:
        # Our dictionary (we'll reassign this later in an if statement)
        d = {}
        if isinstance(obj, Article):
            # put all the attributes into a dtionary
            d = {
                'type': 'Article',
                'year': obj.creation_date.year,
                'month': obj.creation_date.month,
                'day': obj.creation_date.day,
                'headline': obj.headline,
                'content': obj.content,
                'contributors': obj.contributors
            }

        elif isinstance(obj, Picture):
            # put all the attributes into a dtionary
            d = {
                'type': 'Picture',
                'year': obj.creation_date.year,
                'month': obj.creation_date.month,
                'day': obj.creation_date.day,
                'title': obj.title,
                'caption': obj.caption,
                'path': obj.path,
                'contributors': obj.contributors
            }

        else:
            # if it's not either of these, continue quietly.
            continue

        all_content_dicts.append(d)

    dump_file = open('dump.txt', 'w')

    # list of dictionaries gets turned into JSON here
    json_string = json.dumps(all_content_dicts)
    dump_file.write(json_string)
    dump_file.close()


def from_json():
    """
    Load all content from dump.txt into Content.existing_content
    """
    dump_file = open('dump.txt', 'r')

    # read JSON string from dump_file
    json_string = dump_file.read()
    dump_file.close()

    # parse the JSON string into a list of dictionaries
    all_content_dicts = json.loads(json_string)

    # loop over list
    for d in all_content_dicts:
        if d['type'] == 'Article':
            # this automatically adds the Article or Picture to
            # Content.existing_content
            Article(year=d['year'],
                    month=d['month'],
                    day=d['day'],
                    headline=d['headline'],
                    content=d['content'],
                    contributors=d['contributors'])

        elif d['type'] == 'Picture':
            Picture(year=d['year'],
                    month=d['month'],
                    day=d['day'],
                    title=d['title'],
                    caption=d['caption'],
                    path=d['path'],
                    contributors=d['contributors'])
        else:
            # pass quietly
            continue

from_json()
to_json()