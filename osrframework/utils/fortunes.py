################################################################################
#
#    Copyright 2015-2020 Félix Brezo and Yaiza Rubio
#
#   This program is part of OSRFramework. You can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import osrframework.utils.configuration as configuration


messages = [
    "-- OSINT is not fingerprinting. OSINT is Open Sources Intelligence. -- ",
    "-- Social Engineering is not OSINT! -- ",
    "-- AGPLv3 enforces that any app using OSRFramework SHOULD also be free software. --",
    "-- Exclude a wrapper using '-x'. E. g.: 'usufy -n i3visio -x facebook'. --",
    "-- You can export data to formats like gml, xls, etc. E. g.: '-e xls gml'. --",
    "-- Use 'alias_generator' to create aliases based on known info. --",
    "-- Launch 'usufy' against a list of aliases in a file (1 per line) using '-l'. --",
    "-- With 'searchfy' you can find profiles using full names or other data. --",
    "-- With 'phonefy' you can guess if a given phone number is linked to spam. --",
    "-- To automagically open the collected results in the browser use '-w'. --",
    "-- You can find different emails using an alias with 'mailfy -n <alias>'. --",
    "-- If you want to verify infomation about an email, use 'mailfy -m <email>'. --",
    "-- When you reach an email pattern, try 'checkfy' to find candidate emails. --",
    "-- Use 'domainfy -n <alias> -t all' to find domain names using that alias. --",
    "-- Use '-t global cc' to narrow the verifications launched by domainfy. --",
    "-- Use checkfy to find emails matching using a nick that match a pattern. --",
    "-- With '--extra-words hack', 'alias_generator' will add 'hack' to the nicks. --",
    "-- In 'alias_generator', '--common-words' adds words like `xxx', 'real'… --",
    "-- Use '--leet' with 'alias_generator' to build h4x0r n1ckn4m3s. --",
    "-- In 'domainfy', use '-t cc' to find domains resolving to ccTLDs. --",
    "-- In 'usufy', you can add several nicks to '-n'. E. g.: '-n felix yaiza'. --",
    "-- In 'domainfy', you may use several words with '-n'. E. g.: '-n felix yaiza'. --",
    "-- If you have a file with brand names (1 per line), use 'domainfy' with '-N'. --",
    "-- In OSRF CLI apps, you can set a different output folder with '-o'. --",
    "-- Hey! '--help' is your friend, pal! --",
    "-- With '--whois' in 'domainfy' you can find WhoIs info about a domain. --",
    "-- You can get information about an email using 'mailfy -m john@example.com'. --",
    "-- With 'mailfy' you can make reverse Whois queries with ViewDNS.info. --",
    "-- Troy Hunt's Have I Been Pwned is no longer free to use! :( --",
    "-- A Reverse Whois query gets domains registed by a person. --",
    "-- Run 'osrf upgrade' to upgrade OSRFramework to the latest version in PyPI. --",
    "-- Use 'osrf upgrade --only-check' to check for newer versions in PyPI. --",
    "-- Use 'osrf upgrade --use-development' to grab development versions. --",
    "-- The 'osrf' tool will list all the tools as subcommands. --",
    "-- 'osrf usufy -n i3visio ' and 'usufy -n i3visio' has the same effect. --",
    "-- Config files live in '{configuration.get_config_path['appPath']}'. --",
    "-- FAQ at <https://github.com/i3visio/osrframework/blob/master/doc/FAQ.md>! --"
]
