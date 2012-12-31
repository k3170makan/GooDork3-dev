The gooLib guide for developers and python freaks!

If you are going to contribute to the GooDork project please read through these instructions carefully and
make sure any code you write is done according to these rules.


	There are important things to remember when developing goo_ objects and functions:
			*Exceptions: For now we handle exceptions as they are handled in and goo_config,goo_operator
					Please stick to this style of throwing exceptions, and make sure that all exceptions
					thrown are done by the goo_ scripts, we must be able to cater to any situation and inform
					out user in a more intiutive way than python does.
			*Config:
					This version of GooDork has more robust configuration handling, it does this by passing a copy
					of the config object, please make sure that any operations you do on behalf of the user
					are down with respect to the properties set in this object. Please see goo_config for instructions
					on how to check and set configuration properties
			*Commandline Switches:
					See the HELP.txt for decsription of the switches being included in GooDork3 at the time that this file was
					written. Switches conform to a naming convetion: you can add any switch name you want aslong as its not already
					in use and the nmemonic you use---e.g a for inanchor regex---makes sense.
			*Output:
				before printing anything to the screen make sure you add an if statement to check the verbosity level
				you don`t need to actually adhere to printing somethings based on the verbosity level because as yet
				there is no specification for GooDork`s verbosity levels. Before releasing I`ll handle verbosity spec
				and sort out the output.
			
for questions don`t be afraid to deny me sleep over this
please log any issues or questions on the GooDork3-dev repo

Keith (k3170makan) Makan
