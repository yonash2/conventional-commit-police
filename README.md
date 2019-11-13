# conventional-commit-police

Git hook to check for [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) rules

# Usage
To setup the local githook

`make install`

Then in the repo where you want to add the hook, simply rerun

`git init`


# Examples

```
git commit -m "Doing shady commits...."

        It's the Conventional Commit police!!!
        You are under arrest!
        Please follow the rules: https://www.conventionalcommits.org/en/v1.0.0/

git commit -m "fix(behaviour): Fixed my outliar mentality, following the rules from now on"
Inspection finished, you are free to go now.
...
```
