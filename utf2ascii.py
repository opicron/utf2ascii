#------------------------------------------------------------------------------
# utf codes to ascii
#------------------------------------------------------------------------------
def utf_to_ascii( s ):
    
    dictionary = {
        '\xe2\x96\x80':chr(223),
        '\xe2\x96\x84':chr(220),
        '\xe2\x96\x88':chr(219),
        '\xe2\x96\x91':chr(176),
        '\xe2\x96\x92':chr(177),
        '\xe2\x96\x93':chr(178),
        '\xe2\x80\x99':"'",
        '\xe2\x80\x90':'-',
        '\xe2\x80\x91':'-',
        '\xe2\x80\x92':'-',
        '\xe2\x80\x93':'-',
        '\xe2\x80\x94':'-',
        '\xe2\x80\x94':'-',
        '\xe2\x80\x98':"'",
        '\xe2\x80\x9b':"'",
        '\xe2\x80\x9c':'"',
        '\xe2\x80\x9c':'"',
        '\xe2\x80\x9d':'"',
        '\xe2\x80\x9e':'"',
        '\xe2\x80\x9f':'"',
        '\xe2\x80\xa6':'...',
        '\xe2\x80\xb2':"'",
        '\xe2\x80\xb3':"'",
        '\xe2\x80\xb4':"'",
        '\xe2\x80\xb5':"'",
        '\xe2\x80\xb6':"'",
        '\xe2\x80\xb7':"'",
        '\xe2\x81\xba':"+",
        '\xe2\x81\xbb':"-",
        '\xe2\x81\xbc':"=",
        '\xe2\x81\xbd':"(",
        '\xe2\x81\xbe':")",

        '\xc3\xa9':chr(130), # é
        '\xc2\xa1':chr(173), # ¡ INVERTED EXCLAMATION MARK
        '\xc2\xa2':chr(155), # ¢ CENT SIGN
        '\xc2\xa3':chr(156), # £ POUND SIGN
        #'\xc2\xa4':chr() ¤ CURRENCY SIGN
        '\xc2\xa5':chr(157), # ¥ YEN SIGN
        '\xc2\xa6':'|', # ¦ BROKEN BAR
        # '\xc2\xa7' § SECTION SIGN
        '\xc2\xa8':'"', # ¨ DIAERESIS
        '\xc2\xa9':'(C)', # © COPYRIGHT SIGN
        # '\xc2\xaa' ª FEMININE ORDINAL INDICATOR
        '\xc2\xab':chr(174), # « LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
        '\xc2\xac':chr(170), # ¬ NOT SIGN
        '\xc2\xad':'-', # ­ SOFT HYPHEN
        '\xc2\xae':'(R)', # ® REGISTERED SIGN
        '\xc2\xaf':'-', # ¯ MACRON
        '\xc2\xb0':chr(248), # ° DEGREE SIGN
        '\xc2\xb1':chr(241), # ± PLUS-MINUS SIGN
        '\xc2\xb2':chr(253), # ² SUPERSCRIPT TWO
        # '\xc2\xb3' ³ SUPERSCRIPT THREE
        '\xc2\xb4':"'", # ´ ACUTE ACCENT
        '\xc2\xb5':chr(230), # µ MICRO SIGN
        # '\xc2\xb6' ¶ PILCROW SIGN
        '\xc2\xb7':chr(249), # · MIDDLE DOT
        '\xc2\xb8':chr(250), # ¸ CEDILLA
        # '\xc2\xb9' ¹ SUPERSCRIPT ONE
        # '\xc2\xba' º MASCULINE ORDINAL INDICATOR
        '\xc2\xbb':'>>', # » RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
        '\xc2\xbc':chr(172), # ¼ VULGAR FRACTION ONE QUARTER
        '\xc2\xbd':chr(171), # ½ VULGAR FRACTION ONE HALF
        # '\xc2\xbe' ¾ VULGAR FRACTION THREE QUARTERS
        '\xc2\xbf':chr(168), # ¿ INVERTED QUESTION MARK

        '\xc3\x80':chr(133), # À LATIN CAPITAL LETTER A WITH GRAVE
        '\xc3\x81':chr(160), # Á LATIN CAPITAL LETTER A WITH ACUTE
        '\xc3\x82':chr(131), # Â LATIN CAPITAL LETTER A WITH CIRCUMFLEX
        '\xc3\x83':chr(131), # Ã LATIN CAPITAL LETTER A WITH TILDE
        '\xc3\x84':chr(142), # Ä LATIN CAPITAL LETTER A WITH DIAERESIS
        '\xc3\x85':chr(143), # Å LATIN CAPITAL LETTER A WITH RING ABOVE
        '\xc3\x86':chr(146), # Æ LATIN CAPITAL LETTER AE
        '\xc3\x87':chr(128), # Ç LATIN CAPITAL LETTER C WITH CEDILLA
        '\xc3\x88':chr(144), # È LATIN CAPITAL LETTER E WITH GRAVE
        '\xc3\x89':chr(144), # É LATIN CAPITAL LETTER E WITH ACUTE
        '\xc3\x8a':chr(136), # Ê LATIN CAPITAL LETTER E WITH CIRCUMFLEX
        '\xc3\x8b':chr(137), # Ë LATIN CAPITAL LETTER E WITH DIAERESIS
        '\xc3\x8c':chr(141), # Ì LATIN CAPITAL LETTER I WITH GRAVE
        '\xc3\x8d':chr(161), # Í LATIN CAPITAL LETTER I WITH ACUTE
        '\xc3\x8e':chr(140), # Î LATIN CAPITAL LETTER I WITH CIRCUMFLEX
        '\xc3\x8f':chr(139), # Ï LATIN CAPITAL LETTER I WITH DIAERESIS
        '\xc3\x90':'D', # Ð LATIN CAPITAL LETTER ETH
        '\xc3\x91':chr(165), # Ñ LATIN CAPITAL LETTER N WITH TILDE
        '\xc3\x92':chr(149), # Ò LATIN CAPITAL LETTER O WITH GRAVE
        '\xc3\x93':chr(162), # Ó LATIN CAPITAL LETTER O WITH ACUTE
        '\xc3\x94':chr(147), # Ô LATIN CAPITAL LETTER O WITH CIRCUMFLEX
        '\xc3\x95':chr(153), # Õ LATIN CAPITAL LETTER O WITH TILDE
        '\xc3\x96':chr(153), # Ö LATIN CAPITAL LETTER O WITH DIAERESIS
        '\xc3\x97':'x', # × MULTIPLICATION SIGN
        '\xc3\x98':chr(237), # Ø LATIN CAPITAL LETTER O WITH STROKE
        '\xc3\x99':chr(151), # Ù LATIN CAPITAL LETTER U WITH GRAVE
        '\xc3\x9a':chr(163), # Ú LATIN CAPITAL LETTER U WITH ACUTE
        '\xc3\x9b':chr(150), # Û LATIN CAPITAL LETTER U WITH CIRCUMFLEX
        '\xc3\x9c':chr(154), # Ü LATIN CAPITAL LETTER U WITH DIAERESIS
        '\xc3\x9d':'Y', # Ý LATIN CAPITAL LETTER Y WITH ACUTE
        # '\xc3\x9e': Þ LATIN CAPITAL LETTER THORN
        '\xc3\x9f':chr(225), # ß LATIN SMALL LETTER SHARP S
        '\xc3\xa0':chr(133), # à LATIN SMALL LETTER A WITH GRAVE
        '\xc3\xa1':chr(160), # á LATIN SMALL LETTER A WITH ACUTE
        '\xc3\xa2':chr(131), # â LATIN SMALL LETTER A WITH CIRCUMFLEX
        '\xc3\xa3':'a', # ã LATIN SMALL LETTER A WITH TILDE
        '\xc3\xa4':chr(132), # ä LATIN SMALL LETTER A WITH DIAERESIS
        '\xc3\xa5':chr(134), # å LATIN SMALL LETTER A WITH RING ABOVE
        '\xc3\xa6':chr(145), # æ LATIN SMALL LETTER AE
        '\xc3\xa7':chr(134), # ç LATIN SMALL LETTER C WITH CEDILLA
        '\xc3\xa8':chr(138), # è LATIN SMALL LETTER E WITH GRAVE
        '\xc3\xa9':chr(138), # é LATIN SMALL LETTER E WITH ACUTE
        '\xc3\xaa':chr(136), # ê LATIN SMALL LETTER E WITH CIRCUMFLEX
        '\xc3\xab':chr(137), # ë LATIN SMALL LETTER E WITH DIAERESIS
        '\xc3\xac':chr(141), # ì LATIN SMALL LETTER I WITH GRAVE
        '\xc3\xad':chr(161), # í LATIN SMALL LETTER I WITH ACUTE
        '\xc3\xae':chr(140), # î LATIN SMALL LETTER I WITH CIRCUMFLEX
        '\xc3\xaf':chr(139), # ï LATIN SMALL LETTER I WITH DIAERESIS
        '\xc3\xb0':chr(235), # ð LATIN SMALL LETTER ETH
        '\xc3\xb1':chr(164), # ñ LATIN SMALL LETTER N WITH TILDE
        '\xc3\xb2':chr(149), # ò LATIN SMALL LETTER O WITH GRAVE
        '\xc3\xb3':chr(162), # ó LATIN SMALL LETTER O WITH ACUTE
        '\xc3\xb4':chr(147), # ô LATIN SMALL LETTER O WITH CIRCUMFLEX
        '\xc3\xb5':'o', # õ LATIN SMALL LETTER O WITH TILDE
        '\xc3\xb6':chr(148), # ö LATIN SMALL LETTER O WITH DIAERESIS
        '\xc3\xb7':chr(246), # ÷ DIVISION SIGN
        '\xc3\xb8':chr(237), # ø LATIN SMALL LETTER O WITH STROKE
        '\xc3\xb9':chr(164), # ù LATIN SMALL LETTER U WITH GRAVE
        '\xc3\xba':chr(164), # ú LATIN SMALL LETTER U WITH ACUTE
        '\xc3\xbb':'u', # û LATIN SMALL LETTER U WITH CIRCUMFLEX
        '\xc3\xbc':chr(129), # ü LATIN SMALL LETTER U WITH DIAERESIS
        '\xc3\xbd':'y', # ý LATIN SMALL LETTER Y WITH ACUTE
        # '\xc3\xbe' þ LATIN SMALL LETTER THORN
        '\xc3\xbf':chr(152), # ÿ LATIN SMALL LETTER Y WITH DIAERESIS

        '\xf9\xa4':'u',
        '\xc4\x99':'e',
        '\xc4\x97':'e',
        '\xc4\x93':'e'
    }

    #clearly i am a codepage noob for manually converting unicode to ascii. -sigh-
    #anybody got a better solution?

    #replace extended chars with ascii counterparts
    for key in dictionary.keys():
        p = re.compile(key,re.UNICODE)
        s = re.sub(p,dictionary[key],s) #or #s = re.sub(key,dictionary[key],s)

    # replace unfound regular expression with underscore    
    p1 = re.compile(ur'\xe2[\x00-\xFF][\x00-\xFF]',re.UNICODE) #"/[\x{2600}-\x{267F}]/u"  #in the range [\x{2600}-\x{267F}] (i.e. U+2600 to U+267F) # for future use
    p2 = re.compile(ur'\xc3[\x00-\xFF]',re.UNICODE)
    p3 = re.compile(ur'\xc2[\x00-\xFF]',re.UNICODE)

    # safety pattern to get rid of everything above hex c2
    p4 = re.compile(ur'[\xc2-\xd9][\x00-\xFF]',re.UNICODE)

    s = re.sub(p1,chr(249),s)
    s = re.sub(p2,chr(249),s)
    s = re.sub(p3,chr(249),s)
    s = re.sub(p4,chr(249),s)
    
    return s
#------------------------------------------------------------------------------
