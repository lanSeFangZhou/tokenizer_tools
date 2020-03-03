## The Detail Introduction
### 1. conll
conll is a special structrue of corpus text, it has been not
supported anymore.
```
The following is an example of conll:

3 c
4 d

31 c1
41 d1

Every row has two space between members, and there is an
empty row between two sections.
```
***

### 2. conllx
Like conll, but conllx has difference with conll.
```text
for example:
#  aaaa
1  a
2  b

#  bbb
11 a1
21 b1

#  ccc
a  guojia


#  dddd
11  11
c   11

There is an row contains '#' at the top of every section.
```
***
### 3. conllz
Like conllx, but the top is more convenient.
```text
#	{"id": "SID-1"}
char-1	tag-1
char-2	tag-2

#	{"id": "SID-2"}
char-1	tag-1
char-2	tag-2
```
***
### 4. the structures of corpus
Corpus is consist of different member, and have different relations.
```text
The hierarchical relationship:

span -->>  spanset --> sequence -->  document -->  corpus

```
##### (1) span
```text
span has five params:

start         the begin of
end
entity
value
normal_value
```



