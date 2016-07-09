Contributing to OSRFramework
============================

Reporting issues, bugs and fresh ideas
--------------------------------------

The way in which we track the issues regarding the software is by means of the issues page in Github's project site, which can be found here: <https://github.com/i3visio/osrframework/issues>.
Whether you have experimented problems with the installation, you have found a bug in a new platform or you feel that we can add a new functionality, you can find the place to report them there. The only "rule" is to notify one error per issue to be able to track the problems indepently, as well as trying to provide as much information as possible regarding the OS or version you are trying.

If you find that a transform in Maltego is not behaving as expected, we recommend you to set the debug mode as True. Go to Manage --> Manage Transforms, choose the transform and mark the "Set debug info" as True. Please, copy the information shown in the new tab in the issue so as to provide more information to debug it faster.

Extending OSRFramework
----------------------

This section will provide information about how to extend the different tools found in the framework.

### Creating new usufy.py wrappers as plugins

Since OSRFramework 0.13.0, we have added the possibility of creating new wrappers as plugins. 

The basic things you should know in order to create a new wrapper are:
* The structure of the URL that links to the profile.
* The part of the HTML code that says that the user does NOT exist.
* A valid nickname that has an active profile in the website.

For the example, we are going to use an invented socialnetwork: `http://example.com/james` is the URL of a user called `james` in that figured platform. The error returned is `<title>404 not found</title>`. 
Go to the `plugins/wrappers` folder in your home, copy and rename the `wrapper.py.sample` to `example.py`.
Thus you will have a template that you will be able to modify.

First, we'll change the name of the wrapper and the tags:
```
class Example(Platform):
    """ 
        A <Platform> object for Example.
    """
    def __init__(self):
        """ 
            Constructor... 
        """
        self.platformName = "Example"
        self.tags = ["test"]
```

We'll tell the framework, that this platform has usufy-style profile pages by setting to True the corresponding variable:
```
        ########################
        # Defining valid modes #
        ########################
        self.isValidMode = {}        
        self.isValidMode["phonefy"] = False
        self.isValidMode["usufy"] = True
        self.isValidMode["searchfy"] = False   
```

We will provide the URL patern:
```
        ######################################
        # Search URL for the different modes #
        ######################################
        # Strings with the URL for each and every mode
        self.url = {}        
        #self.url["phonefy"] = "http://anyurl.com//phone/" + "<phonefy>"
        self.url["usufy"] = "https://example.com/" + "<usufy>"       
        #self.url["searchfy"] = "http://anyurl.com/search/" + "<searchfy>"  
```

We will know tell if the platform needs credentials to work:
```
        ######################################
        # Whether the user needs credentials #
        ######################################
        self.needsCredentials = {}        
        #self.needsCredentials["phonefy"] = False
        self.needsCredentials["usufy"] = False
        #self.needsCredentials["searchfy"] = False 
```

In some platforms, we may now that the usernames always match a given regular expression (for instance, Twitter does not allow '.' in a username). If this is the case, we can modify the `validQuery` attribute:
```
        #################
        # Valid queries #
        #################
        # Strings that will imply that the query number is not appearing
        self.validQuery = {}
        # The regular expression '.+' will match any non-empty query.
        #self.validQuery["phonefy"] = re.compile(".+")
        self.validQuery["usufy"] = re.compile(".+")   
        #self.validQuery["searchfy"] = re.compile(".+")
```

The last part, is telling the framework which is the message that appears when the user is not present. This is an array, so more than one message can be used here.
```
        ###################
        # Not_found clues #
        ###################
        # Strings that will imply that the query number is not appearing
        self.notFoundText = {}
        #self.notFoundText["phonefy"] = []
        self.notFoundText["usufy"] = ["<title>404 not found</title>"]
        #self.notFoundText["searchfy"] = []  
```

And that's almost all. You can now test OSRFramework as usual. A new option will be available the next time you run the application.

Contributing code
-----------------

If you want us to include your own wrapper, you will be able to extend the whole framework. Think about the wrapper
Whether you want to add a new wrapper or fix a bug, the basic instructions to contribute and perform a pull request on Github are the following (we assume that you have installed Git by yourself, so please follow the instructions in the project's website to install it on your system <https://git-scm.com/downloads>). We will assume that the username for this test is `osrframework_contributor`.

First of all, logged in Github and fork the repository by pressing the corresponding button in <https://github.com/i3visio/osrframework>. This will create a copy of the repository under your profile (i. e.: `https://github.com/osrframework_contributor/osrframework`).

You can clone your forked repository now:
```
# This is an example! Change "osrframework_contributor" for your nick!
git clone https://github.com/osrframework_contributor/osrframework
cd osrframework
```

Then, you can modify any file you want, for example, adding the new wrapper that you have created in the previous case.
```
# Copying the file to the wrappers folder
mv ~/.config/OSRFramework/plugins/wrappers/example.py ./osrframework/wrappers/
```

Whenever you want, you can add the changes performed to the Git index to keep track of what you have changed and prepar it for the commit. 
```
# Add one file
git add ./osrframework/wrappers/example.py
# Or adding all the files modified... Just be a little bit more careful
# git add -A
```

Once you are happy with the changes (and you have tested them!), you can commit the changes with a descriptive message.
```
git commit -m "Adding a new wrapper as example.py."
```

You have to push the changes to your Github project.
```
git push origin
```

You're almost there. You can now go to your project's website (`http://github.com/osrframework_contributor/osrframework`) and click in the `Pulls` tab or going directly to it by appending `pulls` to your forked URL, something similar to `https://github.com/osrframework_contributor/osrframework/pulls`. Then provide there as much detail as you can about the contents of the pull request and shortly we will evaluate the changes and pushed it upstream.

NOTE: a similar procedure can be performed to add new patterns to entify.py.

Style guide
-----------

Just a few things to be taken into account:
* Use four spaces '    ' instead of a tab for identing blocks.
* Provide useful and not trivial comments in English to the code you write.
* Classes should start with a capitalised initial letter.
* As a convention, wrappers inside the `platform_selection.py` should be in alphabetical order. Anyone wants to find things easily!

Licensing
---------

The only thing we expect from other authors'code is to use a GPL-compatible license for their code, preferably GPLv3+ itself. We hope that anybody can use this tool for free (as in Free Software Foundation's four freedoms, not as in *free beer*), so help us to do it.

