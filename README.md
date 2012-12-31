GooDork3-dev

The GooDork3 development reposititory, this is a non-operational copy of GooDork3 and the
pieces of code that will soon be pull together to create the new version.

As soon as all the Goals for this version of GooDork are met the working copy with be commited to the
main GooDork repo.

You guys are welcome to help out ;)

Please see the TODO file for more details on contributing to the code.
Before contributing or adding code with the purpose of merging it to the main GooDork repository
please read the README.md file in the gooLib directory

Direcory structure:
		gooData --- external data crucial to operation, e.g User-Agent strings, Server domain lists
		gooLib --- all scripts crucial to the operation of GooDork besides GooDork.py itself
				I may adopt this as the folder for goo_xml,goo_html,goo_csv,goo_JOSN,---and generally and other output parsers---,goo_rcfile
		gooCore --- not in use at the moment, I may adopt this as the folder for goo_operator,goo_config,goo_results and goo_netlib
