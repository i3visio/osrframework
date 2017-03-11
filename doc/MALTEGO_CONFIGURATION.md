Maltego Configuration Instructions
==================================

OSRFramework was conceived to interact with third party applications. One of the
first approaches was to be compatible with Maltego.


Maltego Installation
--------------------

Maltego is a Java application developed by Paterva that tries to make OSINT
easier for the analyst. Although it is not a free software project, there is a
Community Version that can be used without commercial purposes. It can be
downloaded for your current OS directly from Paterva's website:
```
http://www.paterva.com/web6/products/download2.php
```
Follow the instructions there. Afterwards, you will be able to launch the app
and use the different tools developed by third parties.

Configuring Maltego to Work with OSRFramework Transforms and entities
---------------------------------------------------------------------

Although others have opted for deploying transforms in the cloud in Maltego
transform hubs, OSRFramework transforms are deployed locally. They are Python
scripts that convert OSRFramework conventional output to a Maltego-like format
that can be interpreted by the client conveniently.

The entities and transforms created ad-hoc are shipped within the setup script.
It will create a .mtz file in the OSRFramework home and under the default folder
inside the application folder (just in case a disaster happends ;)).
```
# Under Linux...
~/osrframework-maltego-settings_<VERSION>.mtz
~/.config/OSRFramework/default/osrframework-maltego-settings_<VERSION>.mtz
```

Once you have located it, you will then have to import this file in Maltego by
clicking the `Menu --> Import --> Import configuration`. You might have to
manually check all the types in the installer assistant.
