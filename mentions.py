import pandas as pd

mention_map = {
    #make pairs of phonenumbers and your aliases
  }
  
def replace_mentions(mentions_column):
    return [
        [mention_map.get(number, number) for number in mention_list]
        for mention_list in mentions_column
    ]