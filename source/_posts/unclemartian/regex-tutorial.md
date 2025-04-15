---
title: 【Tech】 Regular Expression Learning Notes
category: unknown
tags: technology
comments: true
date: 2015-05-24 00:00:00
---



1. \d	any Digit

1. .	any Character

1. \.	Period

1. [abc]	Only a, b, or c

1. [^abc]	Not a, b, nor c

1. [a-z]	Characters a to z

1. [0-9]	Numbers 0 to 9

1. {m}	m Repetitions

1. {m,n}	m to n Repetitions

    eg. a{1,} means __>=1 occurance of a__

1. \*	Zero or more repetitions

1. \+	One or more repetitions

    eg. [abc]+ means __>=1 occurance of a or b or c__

1. ?	Optional

    eg. ab?c matches __abc or ac__

1. \s	any Whitespace

1. \t	any tab

1. \n	any new line

1. ^…$	Starts and ends

1. ()	capture Group

1. (a(bc))	capture Sub group

    eg. ^(IMG\d+)\.png$ matches __an image file name__

1. (.*)	capture Variable content

1. (a|b)	Matchs a or b

1. metacharacters

    1. \w	any Alphanumeric character

    1. \W	any Non-alphanumeric character

    1. \d	any Digit

    1. \D	any Non-digit character

    1. \s	any Whitespace

    1. \S	any Non-whitespace character

1. Last but not least: __.* matches anything__
