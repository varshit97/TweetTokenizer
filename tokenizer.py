import re

emoticons = r"""
    (?:[<>]?
      [:;=8]
      [\-o\*\']?
      [\)\]\(\[dDpP/\:\}\{@\|\\]
      |
      [\)\]\(\[dDpP/\:\}\{@\|\\]
      [\-o\*\']?
      [:;=8]
      [<>]?)
      """

tweetRegex = (
    #Emoticons
    emoticons
    ,    
    #Mentions
    r"""(?:@[\w_]+)"""
    ,
    #Hashtags
    r"""(?:\#+[\w_]+[\w\'_\-]*[\w_]+)"""
    ,
    #E-mail
    r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
    ,
    #IP
    r"""\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"""
    ,
    #Dates of the form year-month-date or year/month/date
    r"""\d{4}[-/]\d{2}[-/]\d{2}"""
    ,
    #URL's
    r"""
    http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
    """
    ,
    #Remaining words
    #1)For words with apostrophes etc
    #1)For numbers
    #3)For words without apostrophes etc
    #4)For ellipsis
    #5)All which are not whitespaces
    r"""
    (?:[a-z][a-z'\-_]+[a-z])
    |
    (?:[+\-]?\d+[,/.:-]\d+[+\-]?)
    |
    (?:[\w_]+)
    |
    (?:\.(?:\s*\.){1,})
    |
    (?:\S)
    """
    )

wordRegex = re.compile(r"""(%s)""" % "|".join(tweetRegex), re.VERBOSE | re.I | re.UNICODE)

with open('tweets-en.txt', 'r') as myFile:
    data = myFile.read()
result = data.split('RT ')

sentences = ["OMG!!! This is purely awesome..... I love it!.. :D"]
#for i in result:
#    sentences.append(i.replace('\n', ' '))
#sentences = filter(None, sentences)
for s in sentences:
    print s
    print
    words = wordRegex.findall(s.decode('utf-8'))
    for i in words:
        print i.encode('utf-8')
    print "----------------------------------------------------------------------------------"
    print
