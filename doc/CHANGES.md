OSRFramework Changelog
======================

For more information, check the README.md in <http://github.com/i3visio/osrframework>. For the ToDo list and the known issues, scroll down till the end of this file.

0.15.0, 2016/12/31 -- New major release. Add new wrappers to usufy, mailfy and domainfy. Fix important bugs.
- Add feature #190: Add a new error message to angel.co.
- Add feature #189: Add protonmail.ch as a new mailfy wrapper.
- Add feature #186: Add translate.hola.org as a new usufy wrapper.
- Add feature #185: Add meteor.com as a new platform.
- Add feature #174: Add emoneyspace as a new platform.
- Add feature #161: Making osrfconsole use config values in <OSRFrameworkHOME>/general.cfg.
- Add feature #77: Add Blogmarks as a new platform.
- Add feature #76: Add Smugmug as a new platform.
- Add feature #75: Add Typepad as a new platform.
- Add feature #17: Addition of Gravatar.
- Add feature: Add Buddypic wrapper.
- Add feature: Add Carder wrapper.
- Add feature: Add Csu wrapper.
- Add feature: Add Realcarders wrapper.
- Add feature: Add SingleTrackWorld wrapper.
- Add feature: Add TranslateHola wrapper.
- Add feature: Add Warrior wrapper.                                                    
- Add feature: Add me.com, icloud.com and seznam.cz to mailfy.
- Add feature: Add second level TLDs to domainfy for CCTLD *.nz, *.pe, *.py and *.uk.
- Add feature: Custom errors for OSRFramework.
- Add feature: Some new structures for the usufy fuzzer.
- Add feature: Let users configure the connections to an HTTP and an HTTPS proxy.
- Fix issue #200: Deactivate Youku usufy wrapper
- Fix issue #199: Deactivate Gytorrents usufy wrapper
- Fix issue #198: Change Web.tv error message
- Fix issue #197: Change Metacafe error message
- Fix issue #188: Capture exceptions when errors are found in the configuration files bug deployment.
- Fix issue #182: Cannot install in virtualenv.
- Fix issue #169: searchfy.py --maltego doesn't disable banner.
- Fix issue #121 by urlencoding each and every parameter provided to usufy, searchfy and phonefy. Indirectly fixes issue #91.
- Fix issue: Remove Nubelo wrapper.
- Fix issue: Remove libero.it from mailfy as it is no longer working.
- Fix issue: Deactivate false positives in mailfy for aaathats3as.com, cocaine.ninja, cock.lu, cock.email, firemail.cc, getbackinthe.kitchen, hitler.rocks, memeware.net and waifu.club from cock.li server as well as other false positives in mailfy for noob.com and wp.pl.

0.14.5, 2016/12/09 -- Add Zotero, Leakforums, CardingHispano, MercadoLibre, Angel, Forospyware, Bubok, etc. (up to 22 new wrappers). 
- Add feature #148: Adding Inkonsky as a new platform.
- Add feature #142: Adding angel.co as a new usufy platform.
- Add feature #111: Adding Zotero as a new wrapper.
- Add feature #110: Adding Bitrated.me as a new platform.
- Add feature #109: Adding Spreaker as a new platform.
- Add feature #97: Adding ripenear.me as a new platform.
- Add feature #96: Adding warriorforum as a new platform with usufy.
- Add feature #94: Adding cartodb.com as a platform with usufy.
- Add feature #85: Add muetorrent as a new wrapper. Renamed as a gytorrents.
- Add feature: Add bubok wrapper.
- Add feature: Add cardingmx wrapper.
- Add feature: Add ccm wrapper.
- Add feature: Add espaciolinux wrapper.
- Add feature: Add forocompraventa wrapper.
- Add feature: Add foroptc wrapper.
- Add feature: Add foros24h wrapper.
- Add feature: Add forosspyware wrapper.
- Add feature: Add htcmania wrapper.
- Add feature: Add losviajeros wrapper.
- Add feature: Add leakforums wrapper.
- Add feature: Add cardinghispano wrapper.
- Add feature: Add mercadolibre wrapper.
- Add __author__ and __version__ to the wrappers template.
- Fix issue #183: Web.tv has changed its error.
- Fix issue #180: Artician wrapper is not working. Moved to pending.
- Put in quarantine: unsystem and forominecraft.
- Fix issue: Grab database error in anarchy101.py wrapper.
- Issue #181, required no action.

0.14.4, 2016/11/06 -- Fix issues #178 and #179 with connectingsingles.com.
- Fix issue #178: Mailfy not working on Windows.
- Fix issue #179: Connecting singles has changed its error.

0.14.3, 2016/11/04 -- Fix important issue when deploying on Windows after 0.14.0.
- Fix issue #177. Found an issue when installing on Windows 0.14.2.
- Removed temporary files from /tmp when thet are created.

0.14.2, 2016/10/21 -- Add features #106 and #107 and fix #176.
- Add feature #107: Add keybase.io as a new platform.
- Add feature #106: Add freekabcer as a new platform.
- Fix issue #176: Fix Fanpop error message.

0.14.1, 2016/10/15 -- Fix issues related to the installation procedure and adding some new platforms.
- Add feature #95: Nairaland forum has usufy.
- Add feature #108: Adding coinbase.com as a new platform.
- Fix issue #173: Setup.py requires being in the sudoers list even when installing for a single user.
- Patch issue #175: Moved Naver to pending.
- Patched an issue in usufy.py that may throw errors when None is returned by getPageWrapper (which should just not happen).

0.14.0, 2016/09/30 -- Added domainfy as a tool to verify the existence of domains and first release of osrfconsole, a console GUI similar to msfconsole.
- Add domainfy.py application to check the existence of several domains using socket.gethostbyname().
- Add osrfconsole script to control de utilities in the framework to address issue #158.
- Add general.cfg to address issue #92 and, indirectly, issue #156.
- Modify the shebang of alias_generator, domainfy, entify, enumeration, mailfy, osrfconsole, phonefy, searchfy and usufy to `#!/usr/bin/env python2`.
- Fix issue #172: Remove ummahforum platform.
- Fix issue #171: Dnspython module does not work in Windows.
- Add feature #170: Add OneName as a new usufy platform.
- Fix issue #166: The PLATFORMS variable in osrfconsole does not accept various entries.
- Fix issue #165: Osrfconsole back command exists instead of unloading.
- Add feature #163: Adding tip.me as a new platform.
- Add feature #159: Adding a Console UI to help beginners. Osrfconsole.py is released.
- Add feature #158: Complementing domain search using whois info in domain finder script.
- Add feature #157: Adding domain search in a new script.

0.13.2, 2016/07/23 -- Fixed issue #154: OSRFramework 0.13.1 is installed but throws an error when launching usufy.py.
- Evilzone and Thepiratebay wrappers have been moved to pending as they are conflicting with Skype.
- Some changes performed in the way in which Skype logs the messages in the console.

0.13.1, 2016/07/20 -- Fixed a deployment issue with versions which are older than 0.13.0.
- Relevant hotfix deployed to remove any trace of deprecated installations of the framework during the setup. New installs will not perceive the difference.

0.13.0, 2016/07/19 -- Added the possibility of dinamically adding user-defined modules under the configuration folder. Fixed issues #150, #151, #152, #153.
- Fixed issue #146. Letting the user create new usufy wrappers in its home folder.
- Fixed issue #147. Letting the user create new entify regexps in its home folder.
- Fixed issue #150. Ruby-forum.com has changed its base URL.
- Fixed issue #151. Foodspotting is returning false positives when the first character is a number bug usufy.
- Fixed issue #152. Bucketlistly is returning false positives when the first character is a number bug usufy.
- Fixed issue #153. Sample files (wrapper.py.sample and pattern.py.sample) are not copied during the installation. Added a recursive-include clause to MANIFEST.in to collect the sample files in the config/plugins.
- Addressed issue #149. Bookmarky.com seems not to be working (moved to pending).
- Updated the process of compiling the regular expressions to validate the usernames for each platform.
- Fixed a bug that was not capable of setting properly the api_keys.cfg.
- Modified the configuration file.
- Removed old wrappers which had been removed.
- Added a pending folder with wrappers which need to be fixed. They will not be imported.
- Implemented __eq__ for both wrappers and patterns.

0.12.1, 2016/07/07 -- Fixed issues in Favstar and mailfy.py.
- Fixed issue #145. Favstar platform returns false positives in usufy when looking for long usernames.
- Fixed issue #144. mailfy.py returns error with specific domains. The error seemed to be a problem when no mail was loaded.
- Fixed issue #130. Removing obsolete warning of not properly working in Windows mailfy.

0.12.0, 2016/06/12 -- Fixed issues in 8 platforms when making use of usernames with a ".". URL can be automatically opened in the current web browser. Added 3 new mailfy platforms.
- Important change in the way of validating the nicknames. Valid expressions are matched now as ".+".
- Addressed issue #129: Open found URL in the current webbrowser.
- Fixed issue #141: Btinternet.com as new mailfy platform.
- Fixed issue #140: Libero.it as new mailfy platform.
- Fixed issue #139: Ya.ru as new mailfy platform.
- Fixed issue #138: Causes platform does NOT accept the character "." in the username.
- Fixed issue #137: Nubelo platform does NOT accept the character "." in the username.
- Fixed issue #136: Bucketlistly platform does NOT accept the character "." in the username.
- Fixed issue #135: Burdastyle platform does NOT accept the character "." in the username.
- Fixed issue #134: Askfm platform does NOT accept the character "." in the username.
- Fixed issue #133: Gogobot platform does NOT accept the character "." in the username.
- Fixed issue #132: Rankia platform does NOT accept the character "." in the username.
- Fixed issue #131: Twitpic platform does NOT accept the character "." in the username.

0.11.7, 2016/06/03 -- Critical bug addressed in the installation process identified as #122. Other minor issues addressed too.
- Fixed issue #126: Periscope has changed its error message.

0.11.6, 2016/06/03 -- Critical bug addressed in the installation process identified as #122. Other minor issues addressed too.
- Fixed issue #125: Ibosocial has changed its error for non-existing websites... Changed the error message.
- Fixed issue #124: Freebase wrapper does not work...
- Fixed issue #123: Arto has closed its service... :(. Platform removed.
- Fixed issue with thepiratebay.mk. Added a new message to find platforms which are no longer available.
- Removed other non working platforms that were maintained unnecessarily.

0.11.5, 2016/05/15 -- Added 16 new email providers for mailfy.py.
- The following email providers have been whitelisted in mailfy.py: aaathats3as.com, cocaine.ninja, cock.lu, cock.email, firemail.cc, getbackinthe.kitchen, hitler.rocks, lycos.com, memeware.net, rediffmail.com, tuta.io, tutamail.com, tutanota.com, tutanota.de, waifu.club and zoho.com.
- Some updates done in the mailfy.py blacklists.
- Addressed isue #120: Xat.com platform has changed its usufy URL. The wrapper has been deactivated.

0.11.4, 2016/04/28 -- Corrected a fix #116 in mailfy.py after breaking a thing before committing...
- Fixed issue #116: Mailfy.py is now throwing an error message when the email does not exist.

0.11.3, 2016/04/28 -- Several fixes addressed (#116, #115, #114, #113, #112) regarding with obsolete platforms.
- Fixed issue #115: Worldcarfans is no longer working bug usufy. Removed.
- Fixed issue #114: Relatious.com platform is broken bug usufy. Removed.
- Fixed issue #113: Thecarcommunity platform is broken. Removed.
- Fixed issue #112: New error message in stumbleupon. Removed, the page is now entirely loaded usin javascript.
- Fixed other issues which were not identified originally: metacafe, youku.

0.11.2, 2016/04/01 -- Fixed issue #105: Error in mailfy, line 238.
- Fixed issue #105: Error en mailfy (linea 238) bug mailfy. There was a typo in mailfy.py that showed a wrongly modified variable. Removed the "2015" as stated by Pepepy did the trick.

0.11.1, 2016/03/25 -- Issues related to usufy.py platforms that were throwing false positives.
- Fixed issue #101: Changed the error for gsmspain forums. They had changed the error message.
- Fixed issue #102: Adtriboo is no longer a valid platform. Removed.
- Addressed issue #104: Evilzone has been deactivated until we find the new usufy structure.

0.11.0, 2016/03/14 -- Adding configuration files so as to let the user configure credentials and API keys, as well as making the Maltego transforms work with the current architecture.
- Fixed issue #51: settings for credentials, API keys and connectivity are now stored in the user's home.
- Fixed issue #65: add threading to mailfy.py to allow parallel queries.
- Fixed issue #84: fix Maltego installation using the content_scripts. The creation of the Maltego configuration file is currently done by the setup.py script.
- Fixed issue #88: ods, xls, xlsx are no longer appending results to previously found files. A change in the API now returns only an array of arrays if there is only one sheet.
- Fixed issue #90: added new documentation files as AUTHORS.md, INSTALL.md and HACKING.md.
- Fixed issue #93: Issue when installing in Windows v0.11.x. An exception has been added in the general.changePermissionsRecursively function to deal with os.chown issues when running on Windows.
- Fixed issue #98: Configuration files seem not to be copied correctly in the installation process. In Windows there was a problem with the direction of the slashes. Updated the configuration.py file to address it.
- Fixed issue #100: With the new installation procedure, networkx should be installed in the system. Added a osrframework/utils/configuration.py file.
- Transforms adjusted to use a copy of the scripts stored in the transforms folder inside the configuration directory to fix an issue when trying to run the scripts from Maltego, which seems not to be capable of launching them otherwise making calls in the "python usufy.py..." way in Windows systems.
- Added a MANIFEST.in file to include static files in the ./config folder and the configuration of the transforms.
- Commented logging text in usufy.py.
- Added the missing script config_api_keys.py which was previously ignored.
- Changed the maximum number of threads to be opened by OSRFramework transforms in Maltego as this could lead to problems with the applications.
- Fixed gsmspain.py wrapper for usufy which was not capable of returning a result properly.
- Deactivated identi.ca and couchsurfing because the platforms seems to be unstable.
- Added a browser.cfg to let the user configure OSRFramework browser settings such as the way in which it gets connected to the internet or the user agent.
- Added an api_keys.cfg file to the configuration file where all the API keys will be stored.
- Added three new dependencies pyopenssl, ndg-httpsclient, pyasn1 to deal with InsecurePlatformWarning when calling the Twitter API.
- Removed obsolete functions from osrframework/utils/general.py.
- Removed the logo.png references.

0.10.5, 2016/02/13 -- Fixed issue #86, Metacafe is returning false positives.
- Fixed issue #86: Metacafe was returning false positives and the error was updated.
- Updated a dependency for pyexcel_text package. OSRFramework now works with the latest version.

0.10.4, 2016/02/06 -- Some improvements in the alias generator to address issues #79, #80 and #81. Skype link error message defined as a warning now.
- Fixed issue #79: some new rules to be added to alias_generator.py.
- Fixed issue #80: moving the traditional profilesquatting changes to alias_generator.py. Removed the option from usufy.py.
- Fixed issue #81: all options inserted are now lowercased in alias_generator.
. Modified the Skype warning message to show what is happening and that a Skype session should be opened by the user.
- The interactive interface is now aligned and looks better.
- The birthyear is now the 4th option after the information about the profile.
- README.md brought back as README.md.

0.10.3, 2016/02/06 -- Fixes in mailfy and some searchfy platforms that got outdated.
- Fixed issue #83: alias_generator script is throwing an error related to where to find Python.
- Moved CHANGES.txt to CHANGES and README.md to README.
- Removed setup.cfg.

0.10.2, 2016/02/03 -- Fixes in mailfy and some searchfy platforms that got outdated.
- Fixed the searchfy search for the following platforms: facebook and youtube. The wrapper for twitter does NOT accept special characters such as the 'á', 'é', 'í', etc.
- Added more info to the output of the script to let the user know more info about what is happening.
- The number of domains to be searched is configurable now with the -d option.
- Added keemail.me to mailfy.py.
- Relaxing a requirement for a buggy version of pyexcel_text.

0.10.1, 2016/02/02 -- Two Bitcoin platforms added and a fix introduced to repair aporrealos.
- fanbitcoin and bitcointa have been added to the platform.
- A new error message has been added to aporrealos to avoid false positives when the platform throws errors.
- hotmail.com had to be deactivated from mailfy.py :(.

0.10.0, 2016/01/30 -- New release with several fixes.
- New platforms added to usufy: archive, ehow, gamesheep, hubpages, kanogames, newgrounds, nubelo, retailmenot, sidereel, thepiratebay, webtv, worldcarfans.
- Fixed issues linked to mailfy: #56, #57, #58 and #60.
- Fixed issue #53: adding tabulate dependency to the requirements.txt file.
- Fixed issue #52: fixed a crash when launching -p wikipedia only in usufy.py and some false positives associated to the platform.
- Fixed issue #64: foxmail.com has been removed from the list of secure domains.
- Fixed issue #67: infotelefonica.es has changed its error.
- Fixed issue #73: more convenient packaging solution with pip. Added osrframework scritps to path.
- Fixed issue #69: the new installation process has been detailed.
- Fixes for mailfy platforms which have been deactivated: outlook.com (#69) and sina.com (#70).
- Different fixes linked to issues #33 (jamiiforums), #43 (qq), #42 (buzznet) and #44 (pixls substitutes rawtherapee).
- Fixes for about, forosperu, hellboundhackers, ivoox and linkedin.
- Addressed issue #61: usufy.py --fuzz sample.txt now uses as separator either a '\t' or a ' '.
- A fix has been introduced in the --fuzz option of usufy.py so as not to stop when a matching pattern has been found.
- Added a new phonefy platform: kimatel (quienera.es).
- Removed unused files such as requirements.txt, utils/export.py, utils/timeout.py.
- Update in the README file.

0.9.14, 2016/01/21 -- Mitigation of several fixes.
- Fix to issues #46, #47, #48, #49. Mitigating #40, #42, #43, #44, 45.
- Modification of the Welcome banner for the different utilities. Back to normal.

0.9.13, 2015/11/26 -- Modifications for the Cybercamp.
- Modification of the Welcome banner for the different utilities.
- Changed the default extension to .xls as stated in the help.
- Added a new phonefy platform: infotelefonica.es.
- Modified the name of the listaspam platform from "listspam" to "listaspam".

0.9.12, 2015/11/18 -- Addition of Periscope.
- Addition of a wrapper for Periscope.
- Imported in the setup.py the local osrframework folder to grab the current version number.
- Fixed some errors in the messages displayed.

0.9.11, 2015/11/13 -- Addition of a new searchfy platform to look for PGP keys, as well as new platforms for mailfy.
- Added the search in the PGP public key repository by the MIT.
- Fixed a change in garage4hackers platform.
- Added new wikipediafr and wikipediapt user search.
- The platform thehoodup now waits for credentials.
- Added the sina.com email provider to mailfy.py.
- Added a message to urge the users to report any issue to <https://github.com/i3visio/osrframework/issues>.
- Added a message in mailfy.py when being run under Windows systems to let them know that the app. may behave unexpectedly.
- Corrected a mistake related to matplotlib.
- Added a banner text to each script of the framework showing the current version of the libraries.

0.9.10, 2015/10/26 -- Updated the error messages of burbuja.info in response to issue #32.
- Fixed in the burbuja platform which were confirmed to be working wrongly.
- Updated a new ebay error message just to try to confirm the reported malfunctioning by some users.
- Temporally deactivation of jamiiforums platform to try to fix this issue further.
- Throwing a Warning message when using Twitter API with old versions of ouath library.

0.9.9, 2015/10/18 -- Updated the number of email accounts that con be searched with mailfy.py.
- We have added a series of email providers in which the emailahoy library is also working:  "yeah.net".
- Added badges to the README.md file.

0.9.8, 2015/10/15 -- Updated the number of email accounts that con be searched with mailfy.py.
- We have added a series of email providers in which the emailahoy library is also working:  "126.com", "163.com", "189.cn", "foxmail.com", "qq.com", "yandex.com".

0.9.7, 2015/09/29 -- Updated the enumeration.py file and corrected the slashdot wrapper.
- Corrected the slashdot wrapper which was showing the existence of platforms which in fact didn't exist.
- Commented some references to an old logger in enumeration.py.

0.9.6, 2015/09/22 -- Corrected some installations misconfigurations.
- Fixed an issue when creating the twitter_api which now will try to grab the api_key in compilation time.
- A .csv file will be created by default now in usufy, entify, searchfy, mailfy and phonefy.
- Added a dependency for networkx in requirements.txt.
- Fixes in the installation instructions.

0.9.5, 2015/09/13 -- Corrected some errors in entify.py.
- Corrected some errors in entify.py when looking for entities in a folder.
- Corrected an error when looking for Spanish DNI.

0.9.4, 2015/09/12 -- API integration added to extract information, changes in the export files and added the Twitter API wrapper.
- Created a osrframework/api folder where all the wrappers to each platform will be included.
- Considered in platforms.py the chance of using the API if, both, a wrapper exists and the appropriate authentication methods have been provided.
- Added a Twitter API wrapping the credentials in config_api_credentials.py to make use of Tweepy API.
- Added networkx library to store the information in a graph format: png and gml have been added.
- A hack has been used to avoid encoding problems when exporting data.
- An issue has been detected: python-networkx and python-decorator in Debian-based OS is a problem because they are not up-to-date. Installation from pip is required.
- Changed the export modules to change the starting "@" in the attributes to a "_" and the "i3visio." headers to "i3visio_" for usability reasons when loading future versions of visualization apps.

0.9.3, 2015/08/28 -- Storing the information of mailfy, entify and phonefy files.
- Updating the export primitives of the entify, mailfy and phonefy files.
- Showing some extra text at the beginning of the applications.
- Fix in the extraction of the i3visio.fullname from Twitter.
- Fix in the URIs returned from searchfy (previously, '//' was used in twitter and github wrappers).

0.9.2, 2015/08/25 -- Dealing with export issues linked to localization.
- Dealing with an issue when printing unicode characters in the terminal (specially, in right-to-left languages). A message error will be displayed in the terminal though the information will be stored safely).
- Back to creation of .xls output files by default. An issue has been detected when creating .ods using Unicode characters. We will wait to test the utility.
- About.me platform temporally deactivated as it requires javascript.

0.9.1, 2015/08/20 -- Fixes in the export using experimental versions of pyexcel. Release version.
- Fix an issue linked to the export of Unicode characters in this library. It needs to install an experimental library though.
- Usufy will display now additional details when being launched: start and end messages as well as time consumed.

0.9.0rc5, 2015/08/19 -- Extraction of attributes reconfigured.
- Added youtube and github to searchfy.
- The searchfy file now operates using uri and parsing them.
- Added a new global variable to be able to apply different types of URLs for the profiles in a platform.
- Fix in the csv export that overwrote previous files.

0.9.0rc4, 2015/08/18 -- Extraction of attributes reconfigured.
- Fix in the extraction of Twitter fields.
- Fix in Twitter and Skype wrappers to return an i3visio.uri.homepage entity for the URIs found in the profiles. Previous approach overrode the profile's URI.

0.9.0rc3, 2015/08/18 -- Extraction of attributes reconfigured.
- The extraction of attributes from the profiles has been reincluded.
- The Twitter wrapper recovers now the i3visio.location of a user in usufy mode even when the profile is locked.
- Fixed the usufy launcher to show the icon.
- Fixed compatibiliy of the installer for Windows systems.

0.9.0rc2, 2015/08/16 -- Minor changes linked to redistribution.
- Updating the help texts to include the references to the official repository.
- The .desktop files do not include now a reference to pantheon-terminal.
- Updating the publication process.
- Modification of the regular expressions of the nicks for the following platforms: twitpic, tumblr, rankia, gogobot, buzznet, causes.
- Added about me wrapper to usufy (removed wefollow).

0.9.0rc1, 2015/08/13 -- First DEB, RPM, compiled version of 0.9.0.
- Updating setup.py to include some data files in /usr/bin/.
- Accomdation of the .mtz Maltego file.
- Creation of .deb, .rpm packages.
- Updating the README.
- Creation of .ods output files by default.
- Addition of icons and desktop launchers for Linux systems (.desktop files).

0.9.0b7, 2015/08/12 -- Fixes in the Maltego transforms.
- Added Maltego transform: searchfy on Twitter.
- Added Maltego transform: searchfy on Facebook.
- Added Maltego transform: searchfy on Skype.
- Modified Maltego transform: aliasToKnownMails is now operative.
- The i3visio.location.city entity is extracted correctly when calling ip-api.com API.
- If the number of entities returned are too many a message will be displayed in the Transform output tab.
- Debug windows are not shown in production thanks to a new utility included in configure_maltego.py.
- Fix in Skype wrapper to avoid showing errors messages that make Maltego crash.
- Remove PIP dependencies: only pip will be required. The other dependencies will be checked when installed and included to be manually installed by the user.
- Update on the version number from v0.9.0 to 0.9.0 format (without the 'v').

v0.9.0b6, 2015/07/15 -- Minor fix in hi5 that needs credentials right now.
- Hi5 wrapper has been modified to request credentials.

v0.9.0b5, 2015/07/15 -- Added searchfy platforms for skype, facebook and twitter.
- Added the searchfy functionality.
- Fixed the returned objects in usufy (now, it's always a list).
- Facesaerch and ahmia have been temporally deactivated.
- The generated output now does not override the file if it already exists. Instead, it reads the previous data and appends the new information.

v0.9.0b4, 2015/07/13 -- Fixed the output when too much information is displayed.
- The printed table appearing in the terminal will only show values linked to i3visio.alias, i3visio.platform, i3visio.uri and i3visio.fullname. The rest of the information will be printed to the output files.
- Minor change in the Skype entity previously returned as i3visio.person which now is returned as i3visio.fullname.

v0.9.0b3, 2015/07/13 -- Fixes in tuporno and fanpop.
- Fixed tupono, fanpop.
- Setting .csv files as default output extension for usufy.py.

v0.9.0b2, 2015/07/10 -- Notably improved the export capabilities.
- Fixed an error in the generation of the .csv for usufy.
- New export formats included in usufy: .ods, text, .xls, .xlsx.

v0.9.0b, 2015/06/24 -- Major restructuration of the internal tool. Addition of new platforms and links.
- Moved platforms to wrappers and changed platforms.py to utils.
- Inclusion of old darkfy searches to look for information in Tor platforms.
- Inclusion of regular expression rules to choose valid names.
- Inclusion of a new mailfy.py app that verifies whether an email is known as a valid email using emailahoy.
- Inclusion of a new searchfy.py app that recovers the URL of a search in different platforms.
- Generation of aliases from a person using alias_generator.py
- Inclusion of all the variables to include phonefy, usufy and searchfy search in all platforms.
- Inclusion of plain calls to the different third party API in the main folder.
- Removed phonefy and usufy folders for structural simplicity.
- Added a proof of concept option to access all the users of a given platform.
- Added a facesaerch.py module to look for images.
- Added an alias to IP platform that tries to resolve the location of a user in Skype.
- Added a uriToGoogleCacheUri transform.
- Changed usufy-launcher.py and phonefy-launcher.py to usufy.py and phonefy.py.
- Changed maltfy folder to transforms.
- Opening .onion URI using onion.cab service.
- Updated transforms to match the new distribution.
- Added BeautifulSoup as a needed llibrary for the installation.
- Fixed bladna, breakcom, twicsy, spotify, spoj.
- Deactivating friendsfeed, hellboundhackers and ukdebate (services unavailable for different reasons) and twitch.
- The Skype platform now returns an i3visio.platform entity as expected.

v0.8.3, 2015/04/09 -- Changed the structure of the returned csv files.
- Adding the possibility of creating a csv output file.

v0.8.2, 2015/04/08 -- Changed the structure of the returned json files.
- Fixed an issue that created up to n different json files.
- The returned json is a list of i3visio.objects and the list returned is now ordered and no longer linked to the nickname searched.

v0.8.1, 2015/04/08 -- Minor fixes on certain platforms which were not working.
- Fixed the self.notFoundText in: cafemom, pearltreesspoj.
- Added the self.foundText in: spoj.
- ResearchGate needs credential now.

v0.8.0, 2015/04/03 -- Improvements in the entity generation and an extensive ip-api.com support.
- Added Maltego transform: coordinatesToGoogleMapsBrowser.
- Added Maltego transform: coordinatesToTwitterBrowser.
- Added Maltego transform: domainToIp_ApiInfo.
- Added Maltego transform: ipToIp_ApiInfo.
- Added default fields to every Maltego Entity.
- Modified Maltego transform: aliasToAllProfiles.
- Modified Maltego transform: aliasToFamousPlatforms.
- Modified Maltego transform: aliasToSkypeAccounts.
- Modified Maltego transform: bitcoinAddressToBlockchainDetails.
- Modified Maltego transform: domainToGoogleSearchUriWithEmails.
- Modified Maltego transform: domainToTld.
- Modified Maltego transform: emailToAlias.
- Modified Maltego transform: emailToBreachAccounts.
- Modified Maltego transform: emailToDomain.
- Modified Maltego transform: emailToSkypeAccounts.
- Modified Maltego transform: expandPropertiesFromI3visioEntity.
- Modified Maltego transform: hashToMD5crackDotCom.
- Modified Maltego transform: ipToIp_ApiInformation.
- Modified Maltego transform: phoneToPerson.
- Modified Maltego transform: phoneToMoreInfo.
- Modified Maltego transform: textToGoogleSearchUri.
- Modified Maltego transform: textToEntities.
- Modified Maltego transform: uriToBrowser.
- Modified Maltego transform: uriToDomain.
- Modified Maltego transform: uriToEntities.
- Modified Maltego transform: uriToPort.
- Modified Maltego transform: uriToProtocol.
- Fixed errors in cafemom.com and activerain.trulia.com platforms.
- Requesting credentials for Pokerstrategy and Flixter platforms.
- Addition of a method to recursively extract the information of the fields and attributes, even when it exceeds the maximum number of queries performed for the free version.
- Change in the returnOutput methods of MaltegoEntity and MaltegoTransform to make use of an auxiliar getOutputText method.
- Creation of two new methods in maltfy.lib.maltego to create new entities.
- Reorganization of ip-api.com json objects returned by the API to display i3visio-like objects.
- Inclusion of thirdparties.pipl script to perform queries on usernames and emails.
- Appending a '/' to URL that do not have it when extracting domains or ports.
- Minor change in the way of grabbing md5crack.com API Key in config_api_keys.py.sample.
- Reorganization of network transforms onto i3visio.network set.
- Added new categories: i3visio.location.geo, i3visio.ipv4.
- Changed the i3visio.protocol icon and moved the i3visio.breach entity to i3visio.person group.
- Fixed some issues regarding the way of showing the License on each file.
- Various identation fixes from 't' to '    '.
- Fixed an error with Trulia platform. A missing pair of quoting marks.

v0.7.1, 2015/01/17 -- Release of v0.7.1.
- Fix in the domainToGoogleSearchUriWithEmails transform which was wrongly coded.

v0.7.0, 2015/01/17 -- Release of v0.7.0.
- Added Maltego transform: uriToBrowser.
- Added Maltego transform: uriToBitcoinAddressEntities.
- Added Maltego transform: uriToDniEntities.
- Added Maltego transform: uriToDogecoinAddressEntities.
- Added Maltego transform: uriToEmailEntities.
- Added Maltego transform: uriToIPv4Entities.
- Added Maltego transform: uriToLitecoinAddressEntities.
- Added Maltego transform: uriToMD5Entities.
- Added Maltego transform: uriToNamecoinAddressEntities.
- Added Maltego transform: uriToPeercoinAddressEntities.
- Added Maltego transform: uriToSHA1Entities.
- Added Maltego transform: uriToSHA256Entities.
- Added Maltego transform: uriToUriEntities.
- Added Maltego transform: textToBitcoinAddressEntities.
- Added Maltego transform: textToDniEntities.
- Added Maltego transform: textToDogecoinAddressEntities.
- Added Maltego transform: textToEmailEntities.
- Added Maltego transform: textToIPv4Entities.
- Added Maltego transform: textToLitecoinAddressEntities.
- Added Maltego transform: textToMD5Entities.
- Added Maltego transform: textToNamecoinAddressEntities.
- Added Maltego transform: textToPeercoinAddressEntities.
- Added Maltego transform: textToSHA1Entities.
- Added Maltego transform: textToSHA256Entities.
- Added Maltego transform: textToUriEntities.
- Added Maltego transform: domainToGoogleSearchUriWithEmails.
- Added Maltego transform: textToPhoneDetails.
- Removed Maltego transform: phoneToPerson.
- Reorganization of transforms in different thematic sets.
- Refactoring of uriToEntities.py and textToEntities.py python codes to accept a platform parameter in the transform.
- Changed the name of the Maltego Configuration folder to remove the version in the name.
- Fix the i3visio.surname2 which was wrongly referred as i3visio.surnme2.
- Added different entity categories such as: i3visio.hash, i3visio.location, i3visio.person, i3visio.phone, i3visio.web.

v0.6.1, 2015/01/15 -- Correction of a couple of issues in the entities.
- Added properties by default to i3visio.person.
- Corrected a reference to a i3visio.phone in infobel_com package (it was identified wrongly as i3visio.location.phone)

v0.6.0, 2015/01/14 -- Creation of Phonefy architecture.
- Added a Google Search wrapper based on Mario Vilas approach.
- Added Maltego transform: phoneToPerson.
- Added Maltego transform: textToGoogleSearchURI.
- Added Maltego transform: uriToProtocol.
- Added Maltego transform: uriToPort.
- Added Maltego transform: uriToDomain.
- Added Maltego transform: domainToTLD.
- Added tld, person, fullname, name, surname1, surname2, location.postalcode and location.address entities.
- Changed the main path for the configuration files

v0.5.0, 2015/01/13 -- Creation of Phonefy architecture.
- Added Maltego transform: phoneToMoreInfoListspam.
- Restructuration of phonefy package.
- Change in uriToEntities.py to use an i3visio Browser.
- Fix in i3visio.location.province icon.

v0.4.0, 2015/01/11 -- Added the usufy package onto OSRFramework.
- Added Maltego transform: aliasToAllProfiles.
- Added Maltego transform: aliasToFamousProfiles.
- Inclusion of i3visiotools global files as osrframework.utils.
- Change in old displaying format of usufy entities.
- Change inheritance of i3visio.uri to i3visio.text (rather than i3visio.object).
- Change icon of i3visio.platform.

v0.3.0, 2015/01/11 -- Added the extraction of regular expression with entify.
- Added Maltego transform: textToAllEntities.
- Added Maltego transform: uriToAllEntities.
- Added Maltego transform: emailToAlias.
- Added Maltego transform: emailToDomain.
- Inclusion of a --quiet option.
- Inclusion of transforms related to the extraction of entities.
- Minor changes in the name of entify transforms and i3visio.url has been moved to i3visio.uri.
- Changed the url.py module to uri.py. References changed everywhere.
- Added a simple transformation of foo[at]bar[dot]com mails to be foo@bar.com.
- Fix on i3visio.object entity which was not being imported correctly.
- Edit configuration of configure_maltego to update also default paths for the transforms.

v0.2.0, 2015/01/07 -- Added Maltego transforms.
- Added Maltego transform: aliasToSkypeAccounts.
- Added Maltego transform: bitcoinAddressToBlockchainDetails.
- Added Maltego transform: emailToBreachedAccounts.
- Added Maltego transform: emailToSkypeAccounts.
- Added Maltego transform: hashToMD5crackDotCom.
- Added Maltego transform: expandPropertiesFromI3visioEntity.
- Added entities and logos for Peercoin and Namecoin addresses.
- Removed i3visio.bitcoin, i3visio.litecoin, i3visio.dogecoin entities, as the i3visio.bitcoin.address (et al.) will be used.
- Added entities for i3visio.port, i3visio.domain and i3visio.protocol.
- Changed icon for i3visio.dni.
- Added an autoconfiguration file for Maltego Transforms.

v0.1.0, 2014/12/31 -- Initial release.
- Added a third-party API wrapper for Skype: checkIPDetails.
- Added a third-party API wrapper for md5crack.com: checkIPDetails.
- Added a third-party API wrapper for ip-api.com: checkIPDetails.
- Added a third-party API wrapper for haveibeenpwned.com: checkIfEmailWasHacked.
- Added a third-party API wrapper for blockchain.info: getBitcoinAddressDetails.
- Initial release.


[TO-DO]
Long term:
- Usage of mashape.com API linked to email verification.
- Usage of mashape.com API linked to image verification.
- Inclusions of email verification transforms.
- Inclusion of a call to pipl.com API.
- Full normalization of fields.
- Create Facesaerch and Tor search transforms in Maltego.
- Recover the logging functions.

[Known issues]
- Text to deep web search is broken.
- Recursive expansion of attributes when the cap is reached in Maltego.
- There is an issue in Maltego Chlorine CE when exporting a transform with the transform.local.parameters popup marked as True: <Property name="transform.local.parameters" type="string" popup="true"></Property>. However, when importing the created .mtz file the popup attribute is not correctly updated not requesting the user who imported the transform the value unless he/she clicks on configure and manually update this value, something which may not be trivial for some users. This issue affects the transform aliasToSelectedPlatforms which will throw an error if not manually configured by the user instead of asking the user to insert the deliberately missing parameters. This is not an OSRFramework issue and has conveniently be notified to Paterva with date of 2015/08/12.
