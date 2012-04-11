jTransliterate - [Hirag/Katak]ana to Latin/English & Back
===========================================================================
Sometimes you may want to convert from Hiragana to Katakana, or back again, or...
I dunno, maybe you wanna get the English pronunciation of these words. I'll
be honest and say it's of no concern or interest to me, but I needed this in
Python and so I ported it, figured I'd release it.

It's MIT licensed. Credit for much of this also belongs to Kim Ahlström and
his linguistics/etc work on **[Ve](https://github.com/Kimtaro/ve/blob/master/lib/providers/japanese_transliterators.rb)**.


Installation
---------------------------------------------------------------------------
    pip install jTransliterate


Examples && Documentation
---------------------------------------------------------------------------
``` python
# -*- coding: utf-8 -*-

from jTransliterate import JapaneseTransliterator

# Transliterate from Latin/English to [Hirag/Katak]ana
x = JapaneseTransliterator('kanazawa')
print x.transliterate_from_latn_to_hrkt()
# Should print "かなざわ"

# Transliterate from Hiragana to Latin/English
b = JapaneseTransliterator('かなざわ')
print b.transliterate_from_hira_to_latn()
# Should print "kanazawa"

# Transliterate from either Hiragana or Katakana to Latin/English
print b.transliterate_from_hrkt_to_latn(text = 'カナザワ')
# Should print "kanazawa"

# Transliterate from Katakan to Hiragana (You... probably never need to do this)
print b.transliterate_from_kana_to_hira(text = 'キットカート')
# Should print "きっとかーと"

# Transliterate from Hiragana to Katakana
print b.transliterate_from_hira_to_kana(text = 'かなざわ')
# Should print "カナザワ" 

# If you want to convert between half/full width kana, you can use the following
# functions. I didn't care enough to do demos here. ;|
b.transliterate_from_halfwidth_to_fullwidth()
b.transliterate_from_fullwidth_to_halfwidth()
```

Questions, Comments, Complaints and/or etc
---------------------------------------------------------------------------
Hit me up on them Twitters or find me on them internets at the links below.

Twitter: **[@ryanmcgrath](http://twitter.com/ryanmcgrath/)**  
Web: **[Veno Designs](http://venodesigns.net/)**  