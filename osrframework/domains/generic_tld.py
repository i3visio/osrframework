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
    ".academy", # academic institutes
    ".accountant", # accountants and accounting firms
    ".accountants", # accountants and accounting firms
    ".active", # general
    ".actor", # actors
    ".adult", # adult entertainment (pornography)
    ".aero", # air-transport industry
    ".agency", # business associations
    ".airforce", # defense contractors
    ".apartments", # apartments
    ".app", # Phone apps
    ".archi", # architects and architect firms[42]
    ".army", # defense contractors
    ".associates", # business associations
    ".attorney", # attorneys and legal organizations
    ".auction", #
    ".audio", # stereo/sound systems, music
    ".autos", #
    ".band", #
    ".bar", # Bars and related industry
    ".bargains", # coupons and online sellers
    ".beer", # breweries and beer aficionados
    ".best", #
    ".bid", # auctions
    ".bike", # bicycles
    ".bingo", # bingo
    ".bio", # biodiversity, biographies
    ".biz", # business
    ".black", # those who like the color black[47]
    ".blackfriday", # Black Friday, retail
    ".blog", # Blogs
    ".blue", # those who like the color blue[49]
    ".boo", # ghosts and spooky business
    ".boutique", # specialized businesses
    ".build", # construction industry
    ".builders", # construction workers
    ".business", # businesses
    ".buzz", # marketing and social networking
    ".cab", # cabs and taxi companies
    ".camera", # camera-related businesses
    ".camp", # camps and camping
    ".cancerresearch", # Organizations, research institutes and individuals interested in ending cancer through research [51]
    ".capital", # financial firms
    ".cards", # general
    ".care", # healthcare industry
    ".career", #
    ".careers", # Employment
    ".cash", # financial
    ".casino", # casinos
    ".catering", # Food service
    ".center", # general
    ".ceo", # CEOs
    ".channel", #
    ".chat", # online chat
    ".cheap", # Resellers
    ".christmas", # Christmas
    ".church", # churches
    ".city", # general
    ".claims", # retail, auctions
    ".cleaning", # Cleaning services
    ".click", #
    ".clinic", # healthcare clinics
    ".clothing", # Apparel
    ".cloud", #
    ".club", # groups, organizations, assemblies, communities, general
    ".coach", # travel (flights and motor coaches)
    ".codes", # computer and/or encryption code enthusiasts
    ".coffee", # cafés and coffee aficionados
    ".college", # Educational
    ".community", # social groups, neighborhoods
    ".company", # business associations
    ".computer", # Technology
    ".condos", # Real estate
    ".construction", # Construction industry
    ".consulting", # hired advisors
    ".contractors", # Remodeling and independent businesses
    ".cooking", # sharing recipes
    ".cool", # General interests
    ".coop", # cooperatives
    ".country", # general
    ".coupons", # coupons
    ".credit", # Financial institutions
    ".creditcard", # Financial institutions
    ".cricket", # cricket
    ".cruises", # cruise businesses and travel
    ".dad", # families
    ".dance", # Dance studios and companies
    ".date", # online dating
    ".dating", # online dating
    ".day", # general
    ".deals", # online shopping and couponing
    ".degree", # general
    ".delivery", # general
    ".democrat", # Democratic Party politics
    ".dental", # dentists
    ".dentist", # dentists
    ".design", # graphic art and fashion
    ".diamonds", # diamond and jewelry industry
    ".diet", #
    ".digital", # general
    ".direct", # general
    ".directory", # general directory
    ".discount", # general
    ".dog", # dog stores and owners
    ".domains", # domain registries
    ".download", # technology
    ".eat", # restaurants and foodies
    ".education", # educational institutes
    ".email", # email
    ".energy", # energy industry and marketing
    ".engineer", # engineers and engineering firms
    ".engineering", # engineering firms
    ".equipment", # equipment-related businesses
    ".esq", # lawyers, law firms, legal professionals
    ".estate", # real estate businesses
    ".events", # happenings
    ".exchange", # generic trade
    ".expert", # generic expertise
    ".exposed", # general interest
    ".express", # shipping
    ".fail", # general
    ".faith", # religion and churches
    ".family", # families
    ".fans", # general
    ".farm", # farms and agriculture
    ".fashion", # clothing industry
    ".feedback", #
    ".finance", # financial
    ".financial", # financial
    ".fish", # fishing businesses, sports, and interests
    ".fishing", # fishing businesses, sports, and interests
    ".fit", # Fitness and exercise
    ".fitness", # Fitness and exercise
    ".flights", # airline businesses and travel
    ".florist", # florists
    ".flowers", # florists and gardens
    ".fly", # travel
    ".foo", # web development
    ".football", # soccer and American football
    ".forsale", # online retail
    ".foundation", # charitable organizations
    ".fund", # financial
    ".furniture", # furniture businesses
    ".fyi", # "for your information"
    ".gallery", # photo and art galleries
    ".garden", # gardening
    ".gift", # gift-giving
    ".gifts", # gift-giving
    ".gives", # charities and gift-giving
    ".glass", # window sales and repairs
    ".global", # general
    ".gold", # gold and luxury
    ".golf", # golf
    ".gop", # Republican Party politics
    ".graphics", # graphics
    ".green", # the environmentally-focused
    ".gripe", # opinion sites
    ".guide", # help sites
    ".guitars", # Guitars
    ".guru", # generic expertise
    ".healthcare", # healthcare industry
    ".help", # help sites
    ".here", # generic geographic
    ".hiphop", # Hip hop culture
    ".hiv", # AIDS and HIV
    ".hockey", # hockey
    ".holdings", # real estate or financial business
    ".holiday", # holiday gift industry
    ".homes", # individuals interested in real estate and home improvement
    ".horse", # horse-related businesses and interest
    ".host", # network companies
    ".hosting", #
    ".house", # real estate and construction businesses
    ".how", # how-to guides
    ".info", # information
    ".ing", # Verbal suffix: e.g., "jump.ing".
    ".ink", # creative printing or tattooing[61]
    ".institute[62]", #
    ".insure", # Insurance companies
    ".international", # international entities
    ".investments", # financial
    ".jewelry", # jewelry stores
    ".jobs", # Employment
    ".kim", # people named Kim (given name)
    ".kitchen",
    ".land", # real estate
    ".lawyer", # lawyers and legal organizations
    ".lease", # financing
    ".legal", # lawyers and legal organizations
    ".lgbt", # the lesbian, gay, bisexual and transgender community
    ".life", # general
    ".lighting", # lighting
    ".limited", # general
    ".limo", # limousine businesses
    ".link", # connecting to information[65]
    ".loan", # banks and lenders
    ".loans", # banks and lenders
    ".lol", # LOL: laughing out loud
    ".lotto", #
    ".love", # dating sites
    ".luxe", #
    ".luxury", # businesses catering to the wealthy
    ".management", # business management
    ".market", # marketing services and retailers
    ".marketing", # marketing services
    ".markets", # financial and stock markets
    ".mba", # Masters in Business Administration
    ".media", # general media interests
    ".meet", # social gatherings, meeting new people
    ".meme", # Internet memes
    ".memorial", # memorial sites
    ".men", # men
    ".menu", # restaurants
    ".mobi", # mobile devices
    ".moe", # Japanese otaku culture
    ".money",
    ".mortgage", # mortgage lenders
    ".motorcycles", # motorcycles
    ".mov", # Digital video
    ".movie", # movies and cinemas
    ".museum", # museums
    ".name", # individuals, by name
    ".navy", # defense contractors
    ".network", # general
    ".new", # general
    ".news", # news sites
    ".ngo", # Non-governmental organizations.
    ".ninja",
    ".one", # general
    ".ong", # Non-governmental organizations.
    ".onl",
    ".online", # generic
    ".ooo", # general
    ".organic", # organic gardeners, farmers, foods, etc.
    ".partners", # businesses
    ".parts", # manufacturing and consumer auto
    ".party", # nightclubs and social gatherings
    ".pharmacy", # pharmacies
    ".photo", # photography and photo-sharing
    ".photography", # photography and photo-sharing
    ".photos", # photography and photo-sharing
    ".physio", # physical therapists
    ".pics", # photography and photo-sharing
    ".pictures", # photography and photo-sharing
    ".pid", #
    ".pink", # those who like the color pink
    ".pizza", # pizza parlors
    ".place", # general
    ".plumbing", # plumbing businesses
    ".plus", # generic
    ".poker", # Poker players and sites
    ".porn", # adult entertainment (pornography)
    ".post", # postal services
    ".press", # publishing and journalism
    ".pro", # professions/professionals
    ".productions", # studio/art businesses
    ".prof", # Professors, teachers and learning
    ".properties", # real estate
    ".property", # real estate
    ".qpon", # coupons
    ".racing", # racing
    ".recipes", # recipes and cooking
    ".red", # those who like the color red[74]
    ".rehab",
    ".ren", # Renren users
    ".rent",
    ".rentals", # short-term ownership
    ".repair", # general repair/maintenance businesses
    ".report", # business services
    ".republican", # Republican Party politics
    ".rest", # Restaurants and related industry
    ".review", # public reviews
    ".reviews", # public reviews
    ".rich", # businesses catering to the wealthy
    ".rip", # memorial sites[76]
    ".rocks", # general
    ".rodeo", # Rodeo interest
    ".rsvp", # Invitations and replies
    ".run", # running and jogging
    ".sale", # retail
    ".school", # schools
    ".science", # science-related sites
    ".services", # business services
    ".sex", # adult entertainment (pornography)
    ".sexy", # adult entertainment
    ".shoes", # shoes
    ".show", # entertainment and vlogs
    ".singles", # online dating
    ".site", # general
    ".soccer", # soccer
    ".social", # general interest
    ".software", # computer software
    ".solar", # solar-power
    ".solutions", # business services
    ".space", # as a creative space
    ".studio", # art, fitness, & entertainment
    ".style", # fashion
    ".sucks", # gripe sites
    ".supplies", # manufacturing industries
    ".supply", # manufacturing industries
    ".support", # help pages
    ".surf", # surfing
    ".surgery", # healthcare industry
    ".systems", # technology
    ".tattoo", # tattoo aficionados
    ".tax", # financial
    ".taxi", # taxi services
    ".team", # team sports
    ".tech", # technology
    ".technology", # technology
    ".tel", # Internet communication services
    ".tennis", # tennis
    ".theater", # theaters and cinemas
    ".tips", # general help topics
    ".tires", # tire manufacturers
    ".today", # general
    ".tools", # manufacturing industries
    ".top", # general
    ".tours", # tourism
    ".town", # generic geographic
    ".toys", # toy businesses
    ".trade", # businesses
    ".training", # training and how-tos
    ".travel", # travel and tourism industry related sites
    ".university", # young adults, university life
    ".vacations", # travel
    ".vet", # veterans and veterinarians
    ".video", # video sharing
    ".villas", # real estate and/or travel businesses
    ".vision", # eye-care businesses
    ".vodka", # Vodka-related businesses and interest
    ".vote", # democratic elections and campaign websites
    ".voting", # polling sites
    ".voyage", # travel
    ".wang", # general
    ".watch",
    ".webcam", # Web cam shows and video sharing
    ".website", # general
    ".wed", # engaged couples and wedding-oriented businesses
    ".wedding", # wedding-oriented businesses
    ".whoswho", # general
    ".wiki", # wikis
    ".win", # games, Microsoft Windows
    ".wine", # Wine
    ".work", # general
    ".works", # general
    ".world", # general
    ".wtf", # general
    ".xxx", # adult entertainment (pornography)
    ".xyz", # general
    ".yoga", # yoga
    ".zone", # general
    ".maison", # "house"
    ".abogado", # "lawyer"
    ".gratis", # "free"
    ".futbol", # soccer
    ".juegos", # "games"
    ".soy", # "I am"
    ".tienda",
    ".uno", # "one", for websites targeting Spanish speaking consumers
    ".viajes", # "travel"
    ".haus", # "house"
    ".immobilien", # "real estate"
    ".jetzt", # "now"
    ".kaufen", # "buy"
    ".reise", # "travel"
    ".reisen", # "traveling"
    ".schule", # "school"
    ".versicherung", # "insurance"
    ".desi", # Hindi for the peoples and cultures of South Asia
    ".shiksha",
    ".casa", # "house"
    ".cafe", # "café", "coffee shop", "coffee"
    ".immo", # French, German, Dutch[citation needed], and Italian abbreviation for "real estate"
    ".moda", # "fashion"
    ".voto", # "vote", for election and campaign websites
    ".bar", # bars and pubs
    ".bank", # banks
    ".coop", # cooperatives
    ".enterprises", # business associations
    ".industries", # industrial businesses
    ".institute", # established business associations
    ".ltda", # companies in South America
    ".pub", # bars and pubs
    ".realtor", # realtors
    ".reit", # real estate investment trusts
    ".rest", # restaurants
    ".restaurant", # restaurants
    ".sarl", # Société à responsabilité limitée, Francophone Limited liability company
    ".ventures", # funding for start-ups
    ".xn--4gbrim", # موقع.
    ".xn--ngbc5azd", # شبكة.
    ".xn--mgbab2bd", # بازار.
    ".xn--q9jyb4c", # .みんな
    ".xn--3ds443g", # .在线
    ".xn--fiq228c5hs",
    ".xn--6frz82g",
    ".xn--ses554g", # .网址
    ".xn--io0a7i", # .网络
    ".xn--55qx5d", # .公司
    ".xn--czru2d", # .商城
    ".xn--nqv7f", # .机构
    ".xn--6qq986b3xl", # .我爱你
    ".xn--czr694b", # .商标
    ".xn--rhqv96g", # .世界
    ".xn--3bst00m", # .集团
    ".xn--d1acj3b", # .дети
    ".xn--80asehdb", # .онлайн
    ".xn--c1avg", # .орг
    ".xn--80aswg", # .сайт
    ".xn--i1b6b1a6a2e", # .संगठन
}
