import json
import xml.etree.ElementTree as ET

# Given JSON data
json_data = {
    "ad": {
        "country": "Andorra",
        "ISO2": "ad",
        "countryCode": "376"
    },
    "ae": {
        "country": "United Arab Emirates",
        "ISO2": "ae",
        "countryCode": "971"
    },
    "af": {
        "country": "Afghanistan",
        "ISO2": "af",
        "countryCode": "93"
    },
    "ag": {
        "country": "Antigua and Barbuda",
        "ISO2": "ag",
        "countryCode": "1268"
    },
    "ai": {
        "country": "Anguilla",
        "ISO2": "ai",
        "countryCode": "1264"
    },
    "al": {
        "country": "Albania",
        "ISO2": "al",
        "countryCode": "355"
    },
    "am": {
        "country": "Armenia",
        "ISO2": "am",
        "countryCode": "374"
    },
    "an": {
        "country": "Netherlands Antilles",
        "ISO2": "an",
        "countryCode": "599"
    },
    "ao": {
        "country": "Angola",
        "ISO2": "ao",
        "countryCode": "244"
    },
    "ar": {
        "country": "Argentina",
        "ISO2": "ar",
        "countryCode": "54"
    },
    "at": {
        "country": "Austria",
        "ISO2": "at",
        "countryCode": "43"
    },
    "au": {
        "country": "Australia",
        "ISO2": "au",
        "countryCode": "61"
    },
    "aw": {
        "country": "Aruba",
        "ISO2": "aw",
        "countryCode": "297"
    },
    "az": {
        "country": "Azerbaijan",
        "ISO2": "az",
        "countryCode": "994"
    },
    "ba": {
        "country": "Bosnia and Herzegovina",
        "ISO2": "ba",
        "countryCode": "387"
    },
    "bb": {
        "country": "Barbados",
        "ISO2": "bb",
        "countryCode": "1246"
    },
    "bd": {
        "country": "Bangladesh",
        "ISO2": "bd",
        "countryCode": "880"
    },
    "be": {
        "country": "Belgium",
        "ISO2": "be",
        "countryCode": "32"
    },
    "bf": {
        "country": "Burkina Faso",
        "ISO2": "bf",
        "countryCode": "226"
    },
    "bg": {
        "country": "Bulgaria",
        "ISO2": "bg",
        "countryCode": "359"
    },
    "bh": {
        "country": "Bahrain",
        "ISO2": "bh",
        "countryCode": "973"
    },
    "bi": {
        "country": "Burundi",
        "ISO2": "bi",
        "countryCode": "257"
    },
    "bj": {
        "country": "Benin",
        "ISO2": "bj",
        "countryCode": "229"
    },
    "bm": {
        "country": "Bermuda",
        "ISO2": "bm",
        "countryCode": "1441"
    },
    "bn": {
        "country": "Brunei",
        "ISO2": "bn",
        "countryCode": "673"
    },
    "bo": {
        "country": "Bolivia",
        "ISO2": "bo",
        "countryCode": "591"
    },
    "br": {
        "country": "Brazil",
        "ISO2": "br",
        "countryCode": "55"
    },
    "bs": {
        "country": "Bahamas",
        "ISO2": "bs",
        "countryCode": "1242"
    },
    "bt": {
        "country": "Bhutan",
        "ISO2": "bt",
        "countryCode": "975"
    },
    "bw": {
        "country": "Botswana",
        "ISO2": "bw",
        "countryCode": "267"
    },
    "by": {
        "country": "Belarus",
        "ISO2": "by",
        "countryCode": "375"
    },
    "bz": {
        "country": "Belize",
        "ISO2": "bz",
        "countryCode": "501"
    },
    "ca": {
        "country": "Canada",
        "ISO2": "ca",
        "countryCode": "1"
    },
    "cd": {
        "country": "Democratic Republic of the Congo",
        "ISO2": "cd",
        "countryCode": "243"
    },
    "cf": {
        "country": "Central African Republic",
        "ISO2": "cf",
        "countryCode": "236"
    },
    "cg": {
        "country": "Republic of the Congo",
        "ISO2": "cg",
        "countryCode": "242"
    },
    "ch": {
        "country": "Switzerland",
        "ISO2": "ch",
        "countryCode": "41"
    },
    "ci": {
        "country": "Ivory Coast",
        "ISO2": "ci",
        "countryCode": "225"
    },
    "ck": {
        "country": "Cook Islands",
        "ISO2": "ck",
        "countryCode": "682"
    },
    "cl": {
        "country": "Chile",
        "ISO2": "cl",
        "countryCode": "56"
    },
    "cm": {
        "country": "Cameroon",
        "ISO2": "cm",
        "countryCode": "237"
    },
    "cn": {
        "country": "Republic of China",
        "ISO2": "cn",
        "countryCode": "86"
    },
    "co": {
        "country": "Colombia",
        "ISO2": "co",
        "countryCode": "57"
    },
    "cr": {
        "country": "Costa Rica",
        "ISO2": "cr",
        "countryCode": "506"
    },
    "cu": {
        "country": "Cuba",
        "ISO2": "cu",
        "countryCode": "53"
    },
    "cv": {
        "country": "Cape Verde",
        "ISO2": "cv",
        "countryCode": "238"
    },
    "cx": {
        "country": "Christmas Island",
        "ISO2": "cx",
        "countryCode": "61"
    },
    "cy": {
        "country": "Cyprus",
        "ISO2": "cy",
        "countryCode": "357"
    },
    "cz": {
        "country": "Czech Republic",
        "ISO2": "cz",
        "countryCode": "420"
    },
    "de": {
        "country": "Germany",
        "ISO2": "de",
        "countryCode": "49"
    },
    "dj": {
        "country": "Djibouti",
        "ISO2": "dj",
        "countryCode": "253"
    },
    "dk": {
        "country": "Denmark",
        "ISO2": "dk",
        "countryCode": "45"
    },
    "dm": {
        "country": "Dominica",
        "ISO2": "dm",
        "countryCode": "1767"
    },
    "do": {
        "country": "Dominican Republic",
        "ISO2": "do",
        "countryCode": "1809"
    },
    "dz": {
        "country": "Algeria",
        "ISO2": "dz",
        "countryCode": "213"
    },
    "ec": {
        "country": "Ecuador",
        "ISO2": "ec",
        "countryCode": "593"
    },
    "ee": {
        "country": "Estonia",
        "ISO2": "ee",
        "countryCode": "372"
    },
    "eg": {
        "country": "Egypt",
        "ISO2": "eg",
        "countryCode": "20"
    },
    "er": {
        "country": "Eritrea",
        "ISO2": "er",
        "countryCode": "291"
    },
    "es": {
        "country": "Spain",
        "ISO2": "es",
        "countryCode": "34"
    },
    "et": {
        "country": "Ethiopia",
        "ISO2": "et",
        "countryCode": "251"
    },
    "fi": {
        "country": "Finland",
        "ISO2": "fi",
        "countryCode": "358"
    },
    "fj": {
        "country": "Fiji",
        "ISO2": "fj",
        "countryCode": "679"
    },
    "fk": {
        "country": "Falkland Islands",
        "ISO2": "fk",
        "countryCode": "500"
    },
    "fm": {
        "country": "Micronesia",
        "ISO2": "fm",
        "countryCode": "691"
    },
    "fo": {
        "country": "Faroe Islands",
        "ISO2": "fo",
        "countryCode": "298"
    },
    "fr": {
        "country": "Réunion",
        "ISO2": "fr",
        "countryCode": "262"
    },
    "ga": {
        "country": "Gabon",
        "ISO2": "ga",
        "countryCode": "241"
    },
    "gb": {
        "country": "United Kingdom",
        "ISO2": "gb",
        "countryCode": "44"
    },
    "gd": {
        "country": "Grenada",
        "ISO2": "gd",
        "countryCode": "1473"
    },
    "ge": {
        "country": "Georgia",
        "ISO2": "ge",
        "countryCode": "995"
    },
    "gh": {
        "country": "Ghana",
        "ISO2": "gh",
        "countryCode": "233"
    },
    "gi": {
        "country": "Gibraltar",
        "ISO2": "gi",
        "countryCode": "350"
    },
    "gl": {
        "country": "Greenland",
        "ISO2": "gl",
        "countryCode": "299"
    },
    "gm": {
        "country": "Gambia",
        "ISO2": "gm",
        "countryCode": "220"
    },
    "gn": {
        "country": "Guinea",
        "ISO2": "gn",
        "countryCode": "224"
    },
    "gq": {
        "country": "Equatorial Guinea",
        "ISO2": "gq",
        "countryCode": "240"
    },
    "gr": {
        "country": "Greece",
        "ISO2": "gr",
        "countryCode": "30"
    },
    "gt": {
        "country": "Guatemala",
        "ISO2": "gt",
        "countryCode": "502"
    },
    "gw": {
        "country": "Guinea-Bissau",
        "ISO2": "gw",
        "countryCode": "245"
    },
    "gy": {
        "country": "Guyana",
        "ISO2": "gy",
        "countryCode": "592"
    },
    "hk": {
        "country": "Hong Kong",
        "ISO2": "hk",
        "countryCode": "852"
    },
    "hn": {
        "country": "Honduras",
        "ISO2": "hn",
        "countryCode": "504"
    },
    "hr": {
        "country": "Croatia",
        "ISO2": "hr",
        "countryCode": "385"
    },
    "ht": {
        "country": "Haiti",
        "ISO2": "ht",
        "countryCode": "509"
    },
    "hu": {
        "country": "Hungary",
        "ISO2": "hu",
        "countryCode": "36"
    },
    "id": {
        "country": "Indonesia",
        "ISO2": "id",
        "countryCode": "62"
    },
    "ie": {
        "country": "Ireland",
        "ISO2": "ie",
        "countryCode": "353"
    },
    "il": {
        "country": "Israel",
        "ISO2": "il",
        "countryCode": "972"
    },
    "in": {
        "country": "India",
        "ISO2": "in",
        "countryCode": "91"
    },
    "io": {
        "country": "Diego Garcia",
        "ISO2": "io",
        "countryCode": "246"
    },
    "iq": {
        "country": "Iraq",
        "ISO2": "iq",
        "countryCode": "964"
    },
    "ir": {
        "country": "Iran",
        "ISO2": "ir",
        "countryCode": "98"
    },
    "it": {
        "country": "Italy",
        "ISO2": "it",
        "countryCode": "39"
    },
    "jm": {
        "country": "Jamaica",
        "ISO2": "jm",
        "countryCode": "1876"
    },
    "jo": {
        "country": "Jordan",
        "ISO2": "jo",
        "countryCode": "962"
    },
    "jp": {
        "country": "Japan",
        "ISO2": "jp",
        "countryCode": "81"
    },
    "ke": {
        "country": "Kenya",
        "ISO2": "ke",
        "countryCode": "254"
    },
    "kg": {
        "country": "Kyrgyzstan",
        "ISO2": "kg",
        "countryCode": "996"
    },
    "kh": {
        "country": "Cambodia",
        "ISO2": "kh",
        "countryCode": "855"
    },
    "ki": {
        "country": "Kiribati",
        "ISO2": "ki",
        "countryCode": "686"
    },
    "km": {
        "country": "Comoros",
        "ISO2": "km",
        "countryCode": "269"
    },
    "kn": {
        "country": "St. Kitts and Nevis",
        "ISO2": "kn",
        "countryCode": "1869"
    },
    "kp": {
        "country": "North Korea",
        "ISO2": "kp",
        "countryCode": "850"
    },
    "kr": {
        "country": "South Korea",
        "ISO2": "kr",
        "countryCode": "82"
    },
    "kw": {
        "country": "Kuwait",
        "ISO2": "kw",
        "countryCode": "965"
    },
    "ky": {
        "country": "Cayman Islands",
        "ISO2": "ky",
        "countryCode": "1345"
    },
    "kz": {
        "country": "Kazakhstan",
        "ISO2": "kz",
        "countryCode": "7"
    },
    "la": {
        "country": "Laos",
        "ISO2": "la",
        "countryCode": "856"
    },
    "lb": {
        "country": "Lebanon",
        "ISO2": "lb",
        "countryCode": "961"
    },
    "lc": {
        "country": "St. Lucia",
        "ISO2": "lc",
        "countryCode": "1758"
    },
    "li": {
        "country": "Liechtenstein",
        "ISO2": "li",
        "countryCode": "423"
    },
    "lk": {
        "country": "Sri Lanka",
        "ISO2": "lk",
        "countryCode": "94"
    },
    "lr": {
        "country": "Liberia",
        "ISO2": "lr",
        "countryCode": "231"
    },
    "ls": {
        "country": "Lesotho",
        "ISO2": "ls",
        "countryCode": "266"
    },
    "lt": {
        "country": "Lithuania",
        "ISO2": "lt",
        "countryCode": "370"
    },
    "lu": {
        "country": "Luxembourg",
        "ISO2": "lu",
        "countryCode": "352"
    },
    "lv": {
        "country": "Latvia",
        "ISO2": "lv",
        "countryCode": "371"
    },
    "ly": {
        "country": "Libya",
        "ISO2": "ly",
        "countryCode": "218"
    },
    "ma": {
        "country": "Morocco",
        "ISO2": "ma",
        "countryCode": "212"
    },
    "mc": {
        "country": "Monaco",
        "ISO2": "mc",
        "countryCode": "377"
    },
    "md": {
        "country": "Moldova",
        "ISO2": "md",
        "countryCode": "373"
    },
    "me": {
        "country": "Montenegro",
        "ISO2": "me",
        "countryCode": "382"
    },
    "mg": {
        "country": "Madagascar",
        "ISO2": "mg",
        "countryCode": "261"
    },
    "mh": {
        "country": "Marshall Islands",
        "ISO2": "mh",
        "countryCode": "692"
    },
    "mk": {
        "country": "Macedonia",
        "ISO2": "mk",
        "countryCode": "389"
    },
    "ml": {
        "country": "Mali",
        "ISO2": "ml",
        "countryCode": "223"
    },
    "mm": {
        "country": "Burma",
        "ISO2": "mm",
        "countryCode": "95"
    },
    "mn": {
        "country": "Mongolia",
        "ISO2": "mn",
        "countryCode": "976"
    },
    "mo": {
        "country": "Macau",
        "ISO2": "mo",
        "countryCode": "853"
    },
    "mp": {
        "country": "Mariana Island",
        "ISO2": "mp",
        "countryCode": "1670"
    },
    "mr": {
        "country": "Mauritania",
        "ISO2": "mr",
        "countryCode": "222"
    },
    "ms": {
        "country": "Montserrat",
        "ISO2": "ms",
        "countryCode": "1664"
    },
    "mt": {
        "country": "Malta",
        "ISO2": "mt",
        "countryCode": "356"
    },
    "mu": {
        "country": "Mauritius",
        "ISO2": "mu",
        "countryCode": "230"
    },
    "mv": {
        "country": "Maldives",
        "ISO2": "mv",
        "countryCode": "960"
    },
    "mw": {
        "country": "Malawi",
        "ISO2": "mw",
        "countryCode": "265"
    },
    "mx": {
        "country": "Mexico",
        "ISO2": "mx",
        "countryCode": "52"
    },
    "my": {
        "country": "Malaysia",
        "ISO2": "my",
        "countryCode": "60"
    },
    "mz": {
        "country": "Mozambique",
        "ISO2": "mz",
        "countryCode": "258"
    },
    "na": {
        "country": "Namibia",
        "ISO2": "na",
        "countryCode": "264"
    },
    "nc": {
        "country": "New Caledonia",
        "ISO2": "nc",
        "countryCode": "687"
    },
    "ne": {
        "country": "Niger",
        "ISO2": "ne",
        "countryCode": "227"
    },
    "ng": {
        "country": "Nigeria",
        "ISO2": "ng",
        "countryCode": "234"
    },
    "ni": {
        "country": "Nicaragua",
        "ISO2": "ni",
        "countryCode": "505"
    },
    "nl": {
        "country": "Netherlands",
        "ISO2": "nl",
        "countryCode": "31"
    },
    "no": {
        "country": "Norway",
        "ISO2": "no",
        "countryCode": "47"
    },
    "np": {
        "country": "Nepal",
        "ISO2": "np",
        "countryCode": "977"
    },
    "nr": {
        "country": "Nauru",
        "ISO2": "nr",
        "countryCode": "674"
    },
    "nu": {
        "country": "Niue",
        "ISO2": "nu",
        "countryCode": "683"
    },
    "nz": {
        "country": "New Zealand",
        "ISO2": "nz",
        "countryCode": "64"
    },
    "om": {
        "country": "Oman",
        "ISO2": "om",
        "countryCode": "968"
    },
    "pa": {
        "country": "Panama",
        "ISO2": "pa",
        "countryCode": "507"
    },
    "pe": {
        "country": "Peru",
        "ISO2": "pe",
        "countryCode": "51"
    },
    "ph": {
        "country": "Philippines",
        "ISO2": "ph",
        "countryCode": "63"
    },
    "pk": {
        "country": "Pakistan",
        "ISO2": "pk",
        "countryCode": "92"
    },
    "pl": {
        "country": "Poland",
        "ISO2": "pl",
        "countryCode": "48"
    },
    "pm": {
        "country": "Saint-Pierre and Miquelon",
        "ISO2": "pm",
        "countryCode": "508"
    },
    "pr": {
        "country": "Puerto Rico",
        "ISO2": "pr",
        "countryCode": "1"
    },
    "ps": {
        "country": "Palestine",
        "ISO2": "ps",
        "countryCode": "970"
    },
    "pt": {
        "country": "Portugal",
        "ISO2": "pt",
        "countryCode": "351"
    },
    "pw": {
        "country": "Palau",
        "ISO2": "pw",
        "countryCode": "680"
    },
    "py": {
        "country": "Paraguay",
        "ISO2": "py",
        "countryCode": "595"
    },
    "qa": {
        "country": "Qatar",
        "ISO2": "qa",
        "countryCode": "974"
    },
    "ro": {
        "country": "Romania",
        "ISO2": "ro",
        "countryCode": "40"
    },
    "rs": {
        "country": "Serbia",
        "ISO2": "rs",
        "countryCode": "381"
    },
    "ru": {
        "country": "Russia",
        "ISO2": "ru",
        "countryCode": "7"
    },
    "rw": {
        "country": "Rwanda",
        "ISO2": "rw",
        "countryCode": "250"
    },
    "sa": {
        "country": "Saudi Arabia",
        "ISO2": "sa",
        "countryCode": "966"
    },
    "sb": {
        "country": "Solomon Islands",
        "ISO2": "sb",
        "countryCode": "677"
    },
    "sc": {
        "country": "Seychelles",
        "ISO2": "sc",
        "countryCode": "248"
    },
    "sd": {
        "country": "Sudan",
        "ISO2": "sd",
        "countryCode": "249"
    },
    "se": {
        "country": "Sweden",
        "ISO2": "se",
        "countryCode": "46"
    },
    "sg": {
        "country": "Singapore",
        "ISO2": "sg",
        "countryCode": "65"
    },
    "sh": {
        "country": "St. Helena",
        "ISO2": "sh",
        "countryCode": "290"
    },
    "si": {
        "country": "Slovenia",
        "ISO2": "si",
        "countryCode": "386"
    },
    "sk": {
        "country": "Slovakia",
        "ISO2": "sk",
        "countryCode": "421"
    },
    "sl": {
        "country": "Sierra Leone",
        "ISO2": "sl",
        "countryCode": "232"
    },
    "sm": {
        "country": "San Marino",
        "ISO2": "sm",
        "countryCode": "378"
    },
    "sn": {
        "country": "Senegal",
        "ISO2": "sn",
        "countryCode": "221"
    },
    "so": {
        "country": "Somalia",
        "ISO2": "so",
        "countryCode": "252"
    },
    "sr": {
        "country": "Surinam",
        "ISO2": "sr",
        "countryCode": "597"
    },
    "st": {
        "country": "São Tomé and Príncipe",
        "ISO2": "st",
        "countryCode": "239"
    },
    "sv": {
        "country": "El Salvador",
        "ISO2": "sv",
        "countryCode": "503"
    },
    "sy": {
        "country": "Syria",
        "ISO2": "sy",
        "countryCode": "963"
    },
    "sz": {
        "country": "Swaziland",
        "ISO2": "sz",
        "countryCode": "268"
    },
    "tc": {
        "country": "Turks and Caicos Islands",
        "ISO2": "tc",
        "countryCode": "1649"
    },
    "td": {
        "country": "Chad",
        "ISO2": "td",
        "countryCode": "235"
    },
    "tg": {
        "country": "Togo",
        "ISO2": "tg",
        "countryCode": "228"
    },
    "th": {
        "country": "Thailand",
        "ISO2": "th",
        "countryCode": "66"
    },
    "tj": {
        "country": "Tajikistan",
        "ISO2": "tj",
        "countryCode": "992"
    },
    "tl": {
        "country": "East Timor",
        "ISO2": "tl",
        "countryCode": "670"
    },
    "tm": {
        "country": "Turkmenistan",
        "ISO2": "tm",
        "countryCode": "993"
    },
    "tn": {
        "country": "Tunisia",
        "ISO2": "tn",
        "countryCode": "216"
    },
    "to": {
        "country": "Tonga",
        "ISO2": "to",
        "countryCode": "676"
    },
    "tr": {
        "country": "Turkey",
        "ISO2": "tr",
        "countryCode": "90"
    },
    "tt": {
        "country": "Trinidad and Tobago",
        "ISO2": "tt",
        "countryCode": "1868"
    },
    "tv": {
        "country": "Tuvalu",
        "ISO2": "tv",
        "countryCode": "688"
    },
    "tw": {
        "country": "Taiwan",
        "ISO2": "tw",
        "countryCode": "886"
    },
    "tz": {
        "country": "Tanzania",
        "ISO2": "tz",
        "countryCode": "255"
    },
    "ua": {
        "country": "Ukraine",
        "ISO2": "ua",
        "countryCode": "380"
    },
    "ug": {
        "country": "Uganda",
        "ISO2": "ug",
        "countryCode": "256"
    },
    "us": {
        "country": "United States",
        "ISO2": "us",
        "countryCode": "1"
    },
    "uy": {
        "country": "Uruguay",
        "ISO2": "uy",
        "countryCode": "598"
    },
    "uz": {
        "country": "Uzbekistan",
        "ISO2": "uz",
        "countryCode": "998"
    },
    "va": {
        "country": "Vatican City",
        "ISO2": "va",
        "countryCode": "39"
    },
    "vc": {
        "country": "St. Vincent and the Grenadines",
        "ISO2": "vc",
        "countryCode": "1784"
    },
    "ve": {
        "country": "Venezuela",
        "ISO2": "ve",
        "countryCode": "58"
    },
    "vg": {
        "country": "British Virgin Islands",
        "ISO2": "vg",
        "countryCode": "1284"
    },
    "vi": {
        "country": "Virgin Islands",
        "ISO2": "vi",
        "countryCode": "1340"
    },
    "vn": {
        "country": "Vietnam",
        "ISO2": "vn",
        "countryCode": "84"
    },
    "vu": {
        "country": "Vanuatu",
        "ISO2": "vu",
        "countryCode": "678"
    },
    "wf": {
        "country": "Wallis and Futuna",
        "ISO2": "wf",
        "countryCode": "681"
    },
    "ws": {
        "country": "Samoa",
        "ISO2": "ws",
        "countryCode": "685"
    },
    "xk": {
        "country": "Kosovo",
        "ISO2": "xk",
        "countryCode": "381"
    },
    "ye": {
        "country": "Yemen",
        "ISO2": "ye",
        "countryCode": "967"
    },
    "za": {
        "country": "South Africa",
        "ISO2": "za",
        "countryCode": "27"
    },
    "zm": {
        "country": "Zambia",
        "ISO2": "zm",
        "countryCode": "260"
    },
    "zw": {
        "country": "Zimbabwe",
        "ISO2": "zw",
        "countryCode": "263"
    }
}

# Create root element for the XML document
root = ET.Element('countries')

# Iterate through JSON data and add elements to the XML document
for iso, country_data in json_data.items():
    country_element = ET.SubElement(root, 'country')
    country_element.set('ISO2', country_data['ISO2'])
    
    country_name = ET.SubElement(country_element, 'countryName')
    country_name.text = country_data['country']
    
    country_code = ET.SubElement(country_element, 'countryCode')
    country_code.text = country_data['countryCode']

# Create and save the XML document
xml_tree = ET.ElementTree(root)
xml_tree.write('countries.xml', encoding='utf-8', xml_declaration=True)
