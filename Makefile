
.PHONY: install
install:
	git config --global init.templatedir '~/.git-templates'
	mkdir -p ~/.git-templates/hooks
	ln -sf $$PWD/conventional-commit-police.py $$HOME/.git-templates/hooks/commit-msg
	chmod +x $$HOME/.git-templates/hooks/commit-msg

.PHONY: uninstall
uninstall:
	rm -rf $$HOME/.git-templates/hooks/commit-msg

.PHONY: update
update:
	git pull
