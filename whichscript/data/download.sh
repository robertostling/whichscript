#!/bin/sh

rm -f PropertyValueAliases.txt Scripts.txt Unihan.zip Unihan_Variants.txt \
      Unihan_OtherMappings.txt
wget http://www.unicode.org/Public/UNIDATA/PropertyValueAliases.txt
wget http://www.unicode.org/Public/UNIDATA/Scripts.txt
wget http://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip
unzip Unihan.zip Unihan_OtherMappings.txt

