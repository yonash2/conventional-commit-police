#!/usr/bin/env python
import sys, re


regex = "(feat|fix|docs|style|refactor|test|chore)(.*):(.+)"

commit_message_file = open(sys.argv[1]) #The first argument is the file
commit_message = commit_message_file.read().strip()

if re.search(regex, commit_message) is None:
    print("""
        It's the Conventional Commit Police!!!
        You are under arrest!
        Please follow the rules: https://www.conventionalcommits.org/en/v1.0.0/
    """)
    sys.exit(1)

print("Inspection finished, you are free to go now.")
sys.exit(0)
