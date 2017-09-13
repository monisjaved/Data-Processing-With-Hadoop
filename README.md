# Data-Processing-With-Hadoop

This repository contains data processing using Hadoop for MapReduce as a part of an academic project for data intensive computing. There were 4 activites in the projects. They were:
* WordCount and WordCloud on tweets to find trending mentions
* Word co-occurrence for the tweets collected
* Word Count on Classical Latin Text
* Word co-occurrence among multiple documents

### WordCount and WordCloud

This activity involved running a simple mapreduce job to find the count of all hashtags in a tweet and visualize it in the form of a wordcloud.

The output looked like this
![alt-text](https://raw.githubusercontent.com/monisjaved/Data-Processing-With-Hadoop/master/Other%20Code/Lab4-1/Screen%20Shot%202017-04-23%20at%209.05.44%20PM.png "wordcloud of tweet mentions")

The code and instructions to run the code are present in Code/Lab4-1 

### Word co-occurence for the tweets collected

This activity involved performing word co-occurence [pairs and stripes method] on the tweets obtained before. 
The output looked like this 

1. Pair Method
```
#ChampionsTotal,|pinchos.	3
#Championstwitt|#UCL	3
#Champions|#UCL	2
#Champions|:	4
#Champions|Barcelona	2
#Champions|Champions	1
#Champions|Champions,	16
#Champions|Champions.	4
```

2. Stripe Method
```
"Hemos	{"el": 1, "https://t.co/GYeLCZO": 1, "partidos": 1, "para": 1, "de": 1, "ma\u00f1ana\"": 1, "mucho": 1, "vivir": 1, "como": 1, "\ufffd\ufffd\u26aa\ufe0f": 1, "#UCL\u2026": 1, "https://t.co/txMUlawGN": 1, "trabajado": 1}
"Hoy	{"el": 2, "@Nissan_ESP": 2, "para": 2, "casa\"": 2, "lo": 2, "mi": 2, "#UCL": 2, "Un": 2, "que": 2, "mejor": 2, "ser\u00e1": 2, "visitado": 2, "entrenador\u2026": 2, "nueva": 2}
```

The code and instructions to run the code are present in Code/Lab4-2 


### Word Count on Classical Latin Text

This activity involved performing multiple pass on the input to obtain a specialized wordount. 

Pass 1: Lemmetization using the lemmas.csv file

Pass 2: Identify the words in the texts by <word <docid, [chapter#, line#]> for two documents. 

Pass 3: Repeat this for multiple documents.


The rough MR algorithm can be descirbed as 

```
for each word in the text

normalize the word spelling by replacing j with i and v with u throughout check lemmatizer

for the normalized spelling of the word

if the word appears in the lemmatizer
	obtain the list of lemmas for this word
	for each lemma, create a key/value pair from the lemma and the location 
    where the word was found
    
else	
	create a key/value pair from the normalized spelling and the location 
    where the word was found
```

The output looked like this

```
iuppiter	<luc. 1.198>
iuppiter	<luc. 1.661>
iuppiter	<luc. 1.633>
iura	<luc. 1.177>
iura	<luc. 1.225>
ius	<luc. 1.225>
iuro	<luc. 1.225>
iura	<verg. aen. 1.293>
```

The code and instructions to run the code are present in Code/Lab4-3

### Word co-occurrence among multiple documents

This activity required to 'scale-up' the existing wordcount to run for multiple documents as well increase the word co-occurence from n = 2 grams to n = 3 grams.

The output looked like this

1. Bigram output
```
{a2, taceo}	<verg. aen. 2.255>
{a2, tenedos}	<verg. aen. 2.203>, <verg. aen. 2.255>
{a2, urbs}	<verg. aen. 3.149>, <verg. aen. 2.611>, <luc. 1.483>, <luc. 1.592>
{a2, vertex}	<verg. aen. 10.270>, <verg. aen. 11.577>, <verg. aen. 5.444>, <verg. aen. 1.114>
{ab, aetherius}	<verg. aen. 7.281>, <verg. aen. 8.319>
```

2. Trigram output
```
{accipio, ago, quis2}	<verg. aen. 10.675>
{accipio, anima, ego}	<verg. aen. 4.652>
{accipio, anima, laeto}	<verg. aen. 5.304>
{accipio, animus, laetus}	<verg. aen. 5.304>
{accipio, animus, meum}	<verg. aen. 3.250>, <verg. aen. 10.104>
{accipio, atque, dico2}	<verg. aen. 3.250>, <verg. aen. 9.233>, <verg. aen. 10.104>
```

The code and instructions to run the code are present in Code/Lab4-3

### Comparison of runtime for different n-grams

![alt-text](https://raw.githubusercontent.com/monisjaved/Data-Processing-With-Hadoop/master/Other%20Code/Lab4-4/figure_1.png "comparison image")