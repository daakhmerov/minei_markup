from bs4.formatter import XMLFormatter
from bs4.dammit import EntitySubstitution

def _a(str: str):
    return EntitySubstitution.substitute_xml(str.strip().replace("\n", " "))

class UnsortedAttributes(XMLFormatter):
    def __init__(self, *args, **kwargs):
        return super(XMLFormatter, self).__init__(
            entity_substitution=_a)

    def attributes(self, tag):
        for k, v in tag.attrs.items():
            yield k, v