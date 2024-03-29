#!/usr/bin/env python3

"""mapper.py"""

import sys
import json
import re

pronoun = ["han","hen","hon","den","det","denna","denne"]

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    try:
        tweets = json.loads(line)
        if 'retweeted_status' in tweets:
            if retweeted_status!='':
                continue
        #print ('Unique_Tweets', 1)
        print ('%s\t%s' % ('Unique_Tweets', 1))

        text = tweets["text"]

    	#flag = 0

        for word in pronoun:
            text_match = re.compile(r"\b%s\b" %(word), re.IGNORECASE)
            if text_match.search(text):
                print ('%s\t%s' % (word, 1))
                #flag = 1

#if flag == 1:
#print('keywords_unique',1)
    except:
        pass

