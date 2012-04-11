# -*- coding: utf-8 -*-

from __init__ import JapaneseTransliterator

# Transliterate from Latin/English to [Hirag/Katak]ana
x = JapaneseTransliterator('kanazawa')
print x.transliterate_from_latn_to_hrkt()
# Should print "かなざわ"

# Transliterate from Hiragana to Latin/English
b = JapaneseTransliterator('かなざわ')
print b.transliterate_from_hira_to_latn()
# Should print "kanazawa"

# Transliterate from either Hiragana or Katakana to Latin/English
print b.transliterate_from_hrkt_to_latn(text = u'(ストロベリー)')
# Should print "kanazawa"

# Transliterate from Katakan to Hiragana (You... probably never need to do this)
#print b.transliterate_from_kana_to_hira(text = 'キットカート')
# Should print "きっとかーと"

# Transliterate from Hiragana to Katakana
#print b.transliterate_from_hira_to_kana(text = 'かなざわ')
# Should print "カナザワ" 

# If you want to convert between half/full width kana, you can use the following
# functions. I didn't care enough to do demos here. ;|
#b.transliterate_from_halfwidth_to_fullwidth()
#b.transliterate_from_fullwidth_to_halfwidth()
