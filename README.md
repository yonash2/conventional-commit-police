# conventional-commit-police

Git hook to check for [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) rules

# Usage
To setup the local githook

`make install`

Then in the repo where you want to add the hook, simply rerun

`git init`


# Examples

```
# Install
git clone git@github.com:yonash2/conventional-commit-police.git
cd conventional-commit-police
make install

cd ~/.prezi/<repo>
git init

git commit -m "Doing shady commits...."

        It's the Conventional Commit Police!!!
        You are under arrest!
        Please follow the rules: http://href.prezi.com/ccp

        Example commit message:
        fix(authentication): refresh session cookie for paywalls

        Available categories: feat, fix, docs, style, refactor, test, chore

git commit -m "fix(behaviour): Fixed my outliar mentality, following the rules from now on"
Inspection finished, you are free to go now.
...

# Reinitialize all repos under ~/.prezi
find ~/.prezi -not -name "\.*" -type d -depth 1 | xargs -n1 git init
```
