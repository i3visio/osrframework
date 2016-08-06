# !/usr/bin/python
# -*- coding: utf-8 -*-
#
##################################################################################
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

tld = {
    ".ac", #  Ascension Island
    ".ad", #  Andorra
    ".ae", #  United Arab Emirates
    ".af", #  Afghanistan
    ".ag", #  Antigua and Barbuda
    ".ai", #  Anguilla
    ".al", #  Albania
    ".am", #  Armenia
    ".an", #  Netherlands Antilles
    ".ao", #  Angola
    ".aq", #  Antarctica
    ".ar", #  Argentina
    ".as", #  American Samoa
    ".at", #  Austria
    ".au", #  Australia
    ".aw", #  Aruba
    ".ax", #  Åland
    ".az", #  Azerbaijan
    ".ba", #  Bosnia and Herzegovina
    ".bb", #  Barbados
    ".bd", #  Bangladesh
    ".be", #  Belgium
    ".bf", #  Burkina Faso
    ".bg", #  Bulgaria
    ".bh", #  Bahrain
    ".bi", #  Burundi
    ".bj", #  Benin
    ".bm", #  Bermuda
    ".bn", #  Brunei
    ".bo", #  Bolivia
    ".bq", #  Bonaire
    ".br", #  Brazil
    ".bs", #  Bahamas
    ".bt", #  Bhutan
    ".bv", #  Bouvet Island
    ".bw", #  Botswana
    ".by", #  Belarus
    ".bz", #  Belize
    ".ca", #  Canada
    ".cc", #  Cocos (Keeling) Islands
    ".cd", #  Democratic Republic of the Congo
    ".cf", #  Central African Republic
    ".cg", #  Republic of the Congo
    ".ch", #   Switzerland
    ".ci", #  Côte d'Ivoire
    ".ck", #  Cook Islands
    ".cl", #  Chile
    ".cm", #  Cameroon
    ".cn", #  People's Republic of China
    ".co", #  Colombia
    ".cr", #  Costa Rica
    ".cu", #  Cuba
    ".cv", #  Cape Verde
    ".cw", #  Curaçao
    ".cx", #  Christmas Island
    ".cy", #  Cyprus
    ".cz", #  Czech Republic
    ".de", #  Germany
    ".dj", #  Djibouti
    ".dk", #  Denmark
    ".dm", #  Dominica
    ".do", #  Dominican Republic
    ".dz", #  Algeria
    ".ec", #  Ecuador
    ".ee", #  Estonia
    ".eg", #  Egypt
    ".eh", #  Western Sahara
    ".er", #  Eritrea
    ".es", #  Spain
    ".et", #  Ethiopia
    ".eu", #  European Union
    ".fi", #  Finland
    ".fj", #  Fiji
    ".fk", #  Falkland Islands
    ".fm", #  Federated States of Micronesia
    ".fo", #  Faroe Islands
    ".fr", #  France
    ".ga", #  Gabon
    ".gb", #  United Kingdom
    ".gd", #  Grenada
    ".ge", #  Georgia
    ".gf", #  French Guiana
    ".gg", #  Guernsey
    ".gh", #  Ghana
    ".gi", #  Gibraltar
    ".gl", #  Greenland
    ".gm", #  The Gambia
    ".gn", #  Guinea
    ".gp", #  Guadeloupe
    ".gq", #  Equatorial Guinea
    ".gr", #  Greece
    ".gs", #  South Georgia and the South Sandwich Islands
    ".gt", #  Guatemala
    ".gu", #  Guam
    ".gw", #  Guinea-Bissau
    ".gy", #  Guyana
    ".hk", #  Hong Kong
    ".hm", #  Heard Island and McDonald Islands
    ".hn", #  Honduras
    ".hr", #  Croatia
    ".ht", #  Haiti
    ".hu", #  Hungary
    ".id", #  Indonesia
    ".ie", #  Ireland
    ".il", #  Israel
    ".im", #  Isle of Man
    ".in", #  India
    ".io", #  British Indian Ocean Territory
    ".iq", #  Iraq
    ".ir", #  Iran
    ".is", #  Iceland
    ".it", #  Italy
    ".je", #  Jersey
    ".jm", #  Jamaica
    ".jo", #  Jordan
    ".jp", #  Japan
    ".ke", #  Kenya
    ".kg", #  Kyrgyzstan
    ".kh", #  Cambodia
    ".ki", #  Kiribati
    ".km", #  Comoros
    ".kn", #  Saint Kitts and Nevis
    ".kp", #  Democratic People's Republic of Korea
    ".kr", #  Republic of Korea
    ".kw", #  Kuwait
    ".ky", #  Cayman Islands
    ".kz", #  Kazakhstan
    ".la", #  Laos
    ".lb", #  Lebanon
    ".lc", #  Saint Lucia
    ".li", #  Liechtenstein
    ".lk", #  Sri Lanka
    ".lr", #  Liberia
    ".ls", #  Lesotho
    ".lt", #  Lithuania
    ".lu", #  Luxembourg
    ".lv", #  Latvia
    ".ly", #  Libya
    ".ma", #  Morocco
    ".mc", #  Monaco
    ".md", #  Moldova
    ".me", #  Montenegro
    ".mg", #  Madagascar
    ".mh", #  Marshall Islands
    ".mk", #  Macedonia
    ".ml", #  Mali
    ".mm", #  Myanmar
    ".mn", #  Mongolia
    ".mo", #  Macau
    ".mp", #  Northern Mariana Islands
    ".mq", #  Martinique
    ".mr", #  Mauritania
    ".ms", #  Montserrat
    ".mt", #  Malta
    ".mu", #  Mauritius
    ".mv", #  Maldives
    ".mw", #  Malawi
    ".mx", #  Mexico
    ".my", #  Malaysia
    ".mz", #  Mozambique
    ".na", #  Namibia
    ".nc", #  New Caledonia
    ".ne", #  Niger
    ".nf", #  Norfolk Island
    ".ng", #  Nigeria
    ".ni", #  Nicaragua
    ".nl", #  Netherlands
    ".no", #  Norway
    ".np", #    Nepal
    ".nr", #  Nauru
    ".nu", #  Niue
    ".nz", #  New Zealand
    ".om", #  Oman
    ".pa", #  Panama
    ".pe", #  Peru
    ".pf", #  French Polynesia
    ".pg", #  Papua New Guinea
    ".ph", #  Philippines
    ".pk", #  Pakistan
    ".pl", #  Poland
    ".pm", #  Saint-Pierre and Miquelon
    ".pn", #  Pitcairn Islands
    ".pr", #  Puerto Rico
    ".ps", #  Palestine[27]
    ".pt", #  Portugal
    ".pw", #  Palau
    ".py", #  Paraguay
    ".qa", #  Qatar
    ".re", #  Réunion
    ".ro", #  Romania
    ".rs", #  Serbia
    ".ru", #  Russia
    ".rw", #  Rwanda
    ".sa", #  Saudi Arabia
    ".sb", #  Solomon Islands
    ".sc", #  Seychelles
    ".sd", #  Sudan
    ".se", #  Sweden
    ".sg", #  Singapore
    ".sh", #  Saint Helena
    ".si", #  Slovenia
    ".sj", #  Svalbard and Jan Mayen Islands
    ".sk", #  Slovakia
    ".sl", #  Sierra Leone
    ".sm", #  San Marino
    ".sn", #  Senegal
    ".so", #  Somalia
    ".sr", #  Suriname
    ".ss", #  South Sudan
    ".st", #  São Tomé and Príncipe
    ".su", #  Soviet Union
    ".sv", #  El Salvador
    ".sx", #  Sint Maarten
    ".sy", #  Syria
    ".sz", #  Swaziland
    ".tc", #  Turks and Caicos Islands
    ".td", #  Chad
    ".tf", #  French Southern and Antarctic Lands
    ".tg", #  Togo
    ".th", #  Thailand
    ".tj", #  Tajikistan
    ".tk", #  Tokelau
    ".tl", #  East Timor
    ".tm", #  Turkmenistan
    ".tn", #  Tunisia
    ".to", #  Tonga
    ".tp", #  East Timor
    ".tr", #  Turkey
    ".tt", #  Trinidad and Tobago
    ".tv", #  Tuvalu
    ".tw", #  Taiwan
    ".tz", #  Tanzania
    ".ua", #  Ukraine
    ".ug", #  Uganda
    ".uk", #  United Kingdom
    ".us", #  United States of America
    ".uy", #  Uruguay
    ".uz", #  Uzbekistan
    ".va", #   Vatican City
    ".vc", #  Saint Vincent and the Grenadines
    ".ve", #  Venezuela
    ".vg", #  British Virgin Islands
    ".vi", #  United States Virgin Islands
    ".vn", #  Vietnam
    ".vu", #  Vanuatu
    ".wf", #  Wallis and Futuna
    # Needs extra processing to avoid false positives
    #".ws", #  Samoa
    ".ye", #  Yemen
    ".yt", #  Mayotte
    ".za", #  South Africa
    ".zm", #  Zambia
    ".zw", #  Zimbabwe
    ".xn--lgbbat1ad8j", # الجزائر.
    ".xn--y9a3aq", # .հայ
    ".xn--54b7fta0cc", # .বাংলা
    ".xn--90ais", # .бел
    ".xn--90ae", # .бг[38]
    # Needs extra processing to avoid false positives
    #".xn--fiqs8s", # .中国
    # Needs extra processing to avoid false positives
    #".xn--fiqz9s", # .中國
    ".xn--wgbh1c", # مصر.
    ".xn--e1a4c", # .ею
    ".xn--node", # .გე
    ".xn--qxam", # .ελ[38]
    ".xn--j6w193g", # .香港
    ".xn--h2brj9c", # .भारत
    ".xn--mgbbh1a71e", # بھارت.
    ".xn--fpcrj9c3d", # .భారత్
    ".xn--gecrj9c", # .ભારત
    ".xn--s9brj9c", # .ਭਾਰਤ
    ".xn--xkc2dl3a5ee0h", # .இந்தியா
    ".xn--45brj9c", # .ভারত
    #".ಭಾರತ", #  India
    #".ഭാരതം", #  India
    #".ভাৰত", #  India
    #".ଭାରତ", #  India
    ".xn--mgba3a4f16a", # ایران.
    ".xn--mgbtx2b", # عراق.
    ".xn--mgbayh7gpa", # الاردن.
    ".xn--80ao21a", # .қаз
    ".xn--mix082f", # .澳门
    ".xn--mix891f", # .澳門
    ".xn--d1alf", # .мкд
    ".xn--mgbx4cd0ab", # مليسيا.
    ".xn--l1acc", # .мон
    ".xn--mgbc0a9azcg", # المغرب.
    ".xn--mgb9awbf", # عمان.
    ".xn--mgbai9azgqp6j", # پاکستان.
    ".xn--ygbi2ammx", # فلسطين.
    ".xn--wgbl6a", # قطر.
    ".xn--p1ai", # .рф
    ".xn--mgberp4a5d4ar", # السعودية.
    ".xn--90a3ac", # .срб
    ".xn--yfro4i67o", # .新加坡
    ".xn--clchc0ea0b2g2a9gcd", # .சிங்கப்பூர்
    ".xn--3e0b707e", # .한국
    ".xn--fzc2c9e2c", # .ලංකා
    ".xn--xkc2al3hye2a", # .இலங்கை
    ".xn--mgbpl2fh", # سودان.
    ".xn--ogbpf8fl", # سورية.
    ".xn--kprw13d", # .台湾
    ".xn--kpry57d", # .台灣
    ".xn--o3cw4h", # .ไทย
    ".xn--pgbs0dh", # تونس.
    ".xn--j1amh", # .укр
    ".xn--mgbaam7a8h", # امارات.
    ".xn--mgb2ddes", # اليمن.
}
