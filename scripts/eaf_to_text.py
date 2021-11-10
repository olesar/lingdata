import os
import re
from lxml.etree import ElementTree


BASE_PATH = "./_latest-eaf"
for dirpath, dirnames, filenames in os.walk(BASE_PATH):
    for filename in filenames:
        if filename.endswith(".eaf"):
            et = ElementTree(file=os.path.join(dirpath, filename))
            tiers = [
                tier for tier in et.xpath('//TIER')
                if re.match(r'^(?:@\w{1,8}-text|text@\w{1,8})$', tier.attrib['TIER_ID'])
            ]
            annotations = [annotation.text for tier in tiers for annotation in tier.iterdescendants() if annotation.tag == 'ANNOTATION_VALUE']
            with open("output.txt", "a", encoding="utf-8") as f:
                print(" ".join(x for x in annotations if x is not None), file=f)
