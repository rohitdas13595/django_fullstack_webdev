import re

def multi_re_files(patterns,phrase):
    for pat in patterns:

        print("Seaching for patterns {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase= 'sdsd..sssddd..sdddsddd..dsds..dssssss'
