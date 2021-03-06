# -*- coding: utf-8 -*-

data = """0 ,	115878
1 ,	117932
2 ,	117126
3 ,	117959
4 ,	117323
5 ,	121939
6 ,	118812
7 ,	117296
8 ,	115844
9 ,	115227
10 ,	111478
11 ,	111213
12 ,	109628
13 ,	106775
14 ,	102713
15 ,	103068
16 ,	101333
17 ,	103533
18 ,	104915
19 ,	109623
20 ,	117610
21 ,	126403
22 ,	131931
23 ,	138372
24 ,	142132
25 ,	144757
26 ,	138720
27 ,	137158
28 ,	131326
29 ,	130452
30 ,	128274
31 ,	124410
32 ,	122021
33 ,	122756
34 ,	121610
35 ,	125573
36 ,	122217
37 ,	118600
38 ,	120349
39 ,	121831
40 ,	126462
41 ,	131896
42 ,	129852
43 ,	131978
44 ,	131756
45 ,	128466
46 ,	126219
47 ,	131506
48 ,	137682
49 ,	138550
50 ,	138591
51 ,	137863
52 ,	128174
53 ,	122028
54 ,	117809
55 ,	116144
56 ,	116193
57 ,	115464
58 ,	116269
59 ,	116124
60 ,	113747
61 ,	110925
62 ,	113003
63 ,	111434
64 ,	109538
65 ,	113621
66 ,	116632
67 ,	119621
68 ,	119458
69 ,	119599
70 ,	117113
71 ,	113419
72 ,	104443
73 ,	94357
74 ,	81837
75 ,	76379
76 ,	74708
77 ,	69855
78 ,	64245
79 ,	60290
80 ,	55244
81 ,	51049
82 ,	47728
83 ,	46168
84 ,	42990
85 ,	40316
86 ,	35432
87 ,	32881
88 ,	28370
89 ,	25109
90 ,	21851
91 ,	18170
92 ,	14806
93 ,	11550
94 ,	9636
95 ,	7567
96 ,	4485
97 ,	3016
98 ,	2070
99 ,	1316
100 ,	1896 """

lst = []

for line in data.split('\n'):
    arr = line.split(',')
    year = int(arr[0])
    pop = int(arr[1])
    lst.append(pop)

# average voter
summa = 0
population = 0
for year in range(18,101):
    summa += year * lst[year]
    population += lst[year]
assert round(1.0 * summa / population,2) == 49.14

# weighted
summa = 0
population = 0
a = [0]*18
for year in range(18,101):
    y = year # min(100,year)
    summa += y * y * lst[year]
    population += y * lst[year]
    a.append(y * lst[year])
assert round(1.0 * summa / population, 2) == 56.58

# pensionärers andel av röstmassan
assert round(1.0 * sum(lst[65:]) / sum(lst[18:]), 4) == 0.2488
assert round(1.0 * sum(a[65:]) / sum(a[18:]), 4) == 0.3788
