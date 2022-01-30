import argparse
import re

msg_text = \
    "/test arg1 arg2=1 arg3=hello " \
    "arg4=\"hello world\" arg5=\"7\" arg6=\"hello \"test\" world\" arg7=\"value\""
p = re.compile(r'(?:"(?:\\"|.)*?"|\S)*')
arglist = list(filter(None, re.findall(p, msg_text)))
print(arglist)
