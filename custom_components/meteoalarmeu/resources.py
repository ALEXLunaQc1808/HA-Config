ui_countries_list = [
    "Bosnia I Hercegovína",
    "België,Belgique",
    "България",
    "Suisse,Schweiz,Svizzera",
    "Κύπρος",
    "Česko",
    "Deutschland",
    "Danmark",
    "Eesti",
    "España",
    "Suomi,Finland",
    "France",
    "Ελλάς",
    "Hrvatska",
    "Magyarország",
    "Ireland",
    "ישראל",
    "Ísland",
    "Italia",
    "Lietuva",
    "Luxembourg,Luxemburg",
    "Latvija",
    "Moldova",
    "Црна Гора",
    "Северна Македонија",
    "Malta",
    "Nederland",
    "Norge",
    "Österreich",
    "Polska",
    "Portugal",
    "România",
    "Србија",
    "Sverige",
    "Slovenija",
    "Slovensko",
    "United Kingdom",
]
ui_languages_list = [
    "bosanski",
    "български",
    "čeština",
    "dansk",
    "deutsch",
    "eesti keel",
    "english",
    "español",
    "français",
    "עברית",
    "Ελληνικά",
    "hrvatski",
    "italiano",
    "íslenska",
    "latviešu",
    "lietuviu",
    "magyar",
    "македонски",
    "malti",
    "nederlands",
    "norsk",
    "polski",
    "português",
    "româna",
    "српски",
    "slovenčina",
    "slovenščina",
    "suomi",
    "svenska",
]
countries_map = {
    "AT": "Österreich",
    "BA": "Bosnia I Hercegovína",
    "BE": "België,Belgique",
    "BG": "България",
    "CH": "Suisse,Schweiz,Svizzera",
    "CY": "Κύπρος",
    "CZ": "Česko",
    "DE": "Deutschland",
    "DK": "Danmark",
    "EE": "Eesti",
    "ES": "España",
    "FI": "Suomi,Finland",
    "FR": "France",
    "GR": "Ελλάς",
    "HR": "Hrvatska",
    "HU": "Magyarország",
    "IE": "Ireland",
    "IL": "ישראל",
    "IS": "Ísland",
    "IT": "Italia",
    "LT": "Lietuva",
    "LU": "Luxembourg,Luxemburg",
    "LV": "Latvija",
    "MD": "Moldova",
    "ME": "Црна Гора",
    "MK": "Северна Македонија",
    "MT": "Malta",
    "NL": "Nederland",
    "NO": "Norge",
    "PL": "Polska",
    "PT": "Portugal",
    "RO": "România",
    "RS": "Србија",
    "SE": "Sverige",
    "SI": "Slovenija",
    "SK": "Slovensko",
    "UK": "United Kingdom",
    "Österreich": "AT",
    "Bosnia I Hercegovína": "BA",
    "België,Belgique": "BE",
    "България": "BG",
    "Suisse,Schweiz,Svizzera": "CH",
    "Κύπρος": "CY",
    "Česko": "CZ",
    "Deutschland": "DE",
    "Danmark": "DK",
    "Eesti": "EE",
    "España": "ES",
    "Suomi,Finland": "FI",
    "France": "FR",
    "Ελλάς": "GR",
    "Hrvatska": "HR",
    "Magyarország": "HU",
    "Ireland": "IE",
    "ישראל": "IL",
    "Ísland": "IS",
    "Italia": "IT",
    "Lietuva": "LT",
    "Luxembourg,Luxemburg": "LU",
    "Latvija": "LV",
    "Moldova": "MD",
    "Црна Гора": "ME",
    "Северна Македонија": "MK",
    "Malta": "MT",
    "Nederland": "NL",
    "Norge": "NO",
    "Polska": "PL",
    "Portugal": "PT",
    "România": "RO",
    "Србија": "RS",
    "Sverige": "SE",
    "Slovenija": "SI",
    "Slovensko": "SK",
    "United Kingdom": "UK",
}
languages_map = {
    "bs": "bosanski",
    "dk": "dansk",
    "de": "deutsch",
    "et": "eesti keel",
    "en": "english",
    "es": "español",
    "fr": "français",
    "hr": "hrvatski",
    "it": "italiano",
    "lv": "latviešu",
    "lt": "lietuviu",
    "hu": "magyar",
    "mk": "македонски",
    "mt": "malti",
    "nl": "nederlands",
    "no": "norsk",
    "pl": "polski",
    "pt": "português",
    "ro": "româna",
    "sk": "slovenčina",
    "sl": "slovenščina",
    "fi": "suomi",
    "sv": "svenska",
    "is": "íslenska",
    "cs": "čeština",
    "el": "Ελληνικά",
    "sr": "српски",
    "bg": "български",
    "he": "עברית",
    "bosanski": "bs",
    "dansk": "dk",
    "deutsch": "de",
    "eesti keel": "et",
    "english": "en",
    "español": "es",
    "français": "fr",
    "hrvatski": "hr",
    "italiano": "it",
    "latviešu": "lv",
    "lietuviu": "lt",
    "magyar": "hu",
    "македонски": "mk",
    "malti": "mt",
    "nederlands": "nl",
    "norsk": "no",
    "polski": "pl",
    "português": "pt",
    "româna": "ro",
    "slovenčina": "sk",
    "slovenščina": "sl",
    "suomi": "fi",
    "svenska": "sv",
    "íslenska": "is",
    "čeština": "cs",
    "Ελληνικά": "el",
    "српски": "sr",
    "български": "bg",
    "עברית": "he",
}


def cmap(country):
    """Transform 'country' local <-> iso."""
    return countries_map.get(country)


def lmap(language):
    """Transform 'language' local <-> iso."""
    return languages_map.get(language)
