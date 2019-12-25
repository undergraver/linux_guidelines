#!/bin/sh

H1=heading1.txt
HSUB=subheading.txt
FINAL_TOC=final_toc.txt

grep -nE "^\-\-\-" README.md -B1 | grep -vE "^\-\-" | grep -vE "\-\-\-" > $H1 
grep -nE "^##" README.md > $HSUB

cat $H1 $HSUB | sort -n | sed -E 's/^[0-9]+[\:-]//' > $FINAL_TOC 
rm -f $H1 $HSUB
