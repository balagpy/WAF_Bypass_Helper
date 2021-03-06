import re
from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.UNIVERSAL
__priority__ = PRIORITY.LOW
__specified_name__ = "CVE-2016-3714 ImageMagick ImageTragick"

def tamper(payload, **kwargs):
    """
    change case

    >>> tamper("")
    '<IMG SRC=JaVaScRiPt:alert('XSS')>'
    """
    string=re.sub(r"\w*",convert_this,str(payload))
            


    return (string) if payload else payload

def convert_this(string):
    i=0
    string=string.group()
    new_word=''
    for leter in string:
        if i%2==0:
            new_word=new_word+leter.upper()
        else:
            new_word=new_word+leter.lower()
        i+=1
    return new_word