---
layout: home
title: DISCOVER CHARACTERS' FEATURES BASED ON FIRST NAME
cover-img: /assets/img/IMG_title.jpg
---

## INTRODUCTION

When Tarantino makes his films, you might imagine that he starts with the most obvious choices: the genre of the film, the plot that will unfold, or the scenes that will surprise us. But among these big decisions, there's another, more subtle, but just as crucial: choosing the characters' first names. Bill, Rick, Django... how does he make his choice? Is it really a matter of chance, or does each name conceal a clue to the character's identity?  
Take the name “Jacky”’: do you imagine a rebellious teenager, an adorable Canadian grandmother, or a “badass” woman? It's interesting to note that some first names make us think of certain stereotypes or specific character traits. But what do these names reveal about the characters themselves? In the universe of cinema, each first name can have a considerable impact on the way we perceive a character.  
If you watch a series of romantic comedies, you may well start to notice a number of recurring first names. What is hiding behind these repetitions? Are these first names simply practical or do they allow us to deduce the personality of the characters they refer to?

So, beyond first impressions, the association of first names with character traits may in fact be much more relevant than we think. Through a number of qualitative and syntactic characteristics, we aim to show that there is no such thing as chance when choosing a first name for a film in the cinema! If I told you that Tarantino's next character had your first name, what would its attributes be? It's up to you to find out. 

### PETIT JEU

Well done if you've got the character right! If not, don't worry. We're now going to take you on a journey through our analyses to show you the different ways of predicting a character's characteristics using their first name.

Preview: Let's start with some interesting facts about the most common first names used in movies. First of all, let's take a look at the most common first names in our dataset:

PLOT TOP 1000 NAMES

Johns’ and “Sarahs” top the list. Can you think of an iconic film that features these two names? Here's a hint: ‘Hasta La Vista Baby’... 

### AFFICHE "TERMINATOR"

While John and Sarah are by far the most popular, in more general terms we can see that female first names are more evenly distributed than those given to the male characters. Among the latter, John clearly stands out, being given more than twice as many times as ‘George’, the second most common male first name.
Let's continue by analysing how the most common first names vary according to the country of origin of the films, in order to see whether these choices are influenced by different cultures.

PLOT TOP 10 NAMES COUNTRY

We can see here that in the English-speaking industries, the first name ‘John’ is most frequently attributed to male characters, while female first names show greater diversity. This confirms the observations made in the previous graphs: female first names tend to be more widely distributed than male first names, where ‘John’ stands out. As far as non-English-speaking countries are concerned, we can see that the most common first names used by the characters are often of local origin.

Now that we've set the scene, let's take a closer look at the links between the characters' first names and their attributes.

## I. GENDER ANALYSIS - autre titre

Naturally, in order to draw up a profile of a character from their name, it is essential to start by identifying their gender: male or female. At first sight, this may seem obvious. However, among the thousands of first names that exist, what is it that makes a first name perceived as masculine rather than feminine? With this in mind, we have undertaken an analysis of first names by looking at the notable differences in their composition between feminine and masculine first names. In the graph below, we compare the first and last letters of female first names with those of male first names.

PLOT FIRST LAST LETTER

Several significant differences emerge: Female names are much more likely to end with an ‘a’ or ‘e’ compared to male names. To further explore this observation, we conducted chi-square tests to compare the distributions of initial and final letters between male and female names. The results show that certain parameters, such as the presence of an ‘a’, ‘d’, ‘e’, or ‘s’ at the end of a name, help distinguish male names from female names with a confidence level greater than 95%. Additionally, by examining the common distribution, we find that nearly 15 times more female names start and end with an ‘a’ compared to male names, which further reinforces the distinct patterns observed. Perfect! We now have a first clue to avoid imagining John as Sarah or Sarah as John… it’s a great start !

## II. AGE ANALYSIS - autre titre

GIF d’un grand-père dans un film

Tastes and trends evolve over the years: the names of your grandparents are likely very different from those of your younger cousins. What was original in the past is now considered traditional, and this evolution also influences the way characters are named in cinema.

But then, can we associate certain names with specific age groups ? For example, do some names appear more frequently for an elderly person compared to a newborn ?

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/box_plot_features_age.html" width="100%" height="400" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

These graphs are not very expressive… this is probably not the right path to uncover the deepest secrets of Tarantino. However, we believe we have an explanation for this! The names of older people today are the names of younger people from the past. Taking this into account, it is normal not to find any significant difference between the names of characters from different age groups. Let’s try looking at the film genres instead.

## III. MOVIE GENRES ANALYSIS - autre titre

Let's take a look at the differences between first names in different film genres. Certain first names are associated with specific types of character, and are often found in the same categories of film. For example, it's hard to imagine a character whose first name is “Romeo” being anything but romantic, passionate and desperate for love. Or it's hard to imagine a rude, mediocre and unathletic “Percival”. As a result, these two characters are often associated with the “Romance” and “Action & Adventure” genres respectively. With this in mind, let's take a look at the correlations between first names and film categories.

To get a good idea of these differences, let's take a look at the most common first names for each film category:

PLOT TOP 10 NAMES GENRE

Sarah” and ‘John’ continue to be omnipresent in all categories, but we can see that popular first names change according to film genre. Let's analyze the syntactic characteristics of first names according to film type:

BOX PLOT FATURES GENRE

MOVIE GENRE FIRST LETTER

MOVUE GENRE LAST LETTER

Great results! Conclusive results! This heatmap tells us a lot about the remarkable differences between the syntaxes of first names present in different film genres. Boxes marked with an asterisk show pairs of film types with statistically different 'length' or 'vowel/consonant ratio' distributions (with 95% confidence) according to the Tukey test. 
We can now find our way between 'Terminator' characters and 'La La Land' characters. We're beginning to know a lot about character names... but let's not stop there - the most interesting is yet to come!

Films use culturally specific first names to reinforce the authenticity of their context. Clichés about certain populations are used in the choice of characters' first names to reinforce certain character traits. So it's interesting to see if it's possible to make links between first names and the geographical origin of the first name, in order to better imagine our famous mystery character whose first name we only know.
We have focused our analysis on the lexical study of first names according to their origin, as we feel this is the most relevant and interesting choice. 

We began our study by looking at the distributions of the first and last letters of first names. We performed a statistical study using the CHI-2 test to determine the most significant elements. Here are the graphs we obtained, showing the distributions of origins for the most significant elements (i.e. the elements for which the distributions differ the most):

SIGNIFICANT LETTER FOR ORIGIN

This graph clearly shows that the first and last letters of first names are very good indicators of the origin of a given name. Could we have guessed it? Who is the Spanish character between “Pedro” and “Ivan”? It's intuitive, of course, but it's always good to trust good statistics!
Letters with accents are called diacritical letters. This is a very interesting and effective way of determining the origin of a given name. We've selected the 4 most significant ones to illustrate this:

PDIACRITICS LETTER FOR ORIGIN

This bar plot is very telling and shows that it is possible to isolate an origin thanks to the presence of certain diacritical letters.

Finally, it is also possible to use the articulatory phonetics of first names to determine their origin. We have chosen to focus on the most telling phonetics: affricate, fricative, liquid, nasal and occlusive. We therefore studied the percentage of first names, for each origin, that contain each of these phonetic categories.

PLOT PHONETIC ORIGIN

This analysis is useful, but we expected it to be more telling. We observe that names of Hispanic and Romance origin contain more liquid consonants (such as [l] and [r]), while Slavic and English names show a greater presence of plosives (such as [p] and [t]). Nasals (such as [m] and [n]) are particularly frequent in Slavic and Hispanic names, but less so in Asian names. On the whole, the phonetic structures of names reflect the specific features of each origin.

We now know how to recognize a character's origin from his or her first name. Now we want to know if it's a nice character we're going to get attached to, or a disgusting one who's going to disgust us.

## IV. ORIGIN ANALYSIS - autre titre

Our dataset doesn't show the ethnic origins of the characters' first names. This is where the expertise of the AdadaSurMonBidet team comes in. 
We found an additional dataset (“Name Ethnicity Dataset” in the 'Resources' tab) that includes almost 14,000 first names with their ethnic origin. We developed a predictive model based on this additional dataset, so that we could generalize to our entire dataset. Impressive, isn't it? With an accuracy of 72%, we were able to establish the ethnic origins of our characters' first names for further research. Our categories for origins are: “Slavic”, “Romance”, “East Asian”, “English-Speaking” and “Hispanic”. 


## V. SENTIMENTAL ANALYSIS ANALYSIS - autre titre

Which of these two names, “Toby” and “Lucifer”, would you give to a great villain? Which would you give to a sympathetic and generous character? I think we agree...
We've all been conditioned to think of some names as synonymous with kindness and trust, while others symbolize wickedness and terror. Let's continue our study to find out if there's a significant difference between the names of nice characters and the names of nasty characters.

### Sentimental Analysis

Our main dataset does not include information on character morality. However, we do have access to all the movie summaries in our dataset. We therefore came up with the idea of establishing our characters' values ourselves, so that we could study the link between these and their first names. 
To achieve this, we carried out a sentimental analysis for each first name in our dataset, based on the movie summaries. We began by grouping all the sentences in the summaries according to the first name of the character they refer to. From there, we performed sentimental analysis on each first name, enabling us to assess the tendency of certain first names to designate good guys or bad guys. 

Our sentimental analysis enabled us to classify the first names into 5 different categories. These are presented in the graph below:

PLOT SENTIMENTAL ANALYSIS RESULT 
PLOT POLARITY

Extraordinary, we can finally put labels on our first names: “Very Good Guy”, “Good Guy”, “Neutral”, “Bad Guy” or “Very Bad Guy”. So what are the names of the greatest villains and those of the most lovable characters? Let's take a look:

PLOT SUNBURST POLARITY FILLE ET GARCON
PLOT POLARITY BOX

Now that we've familiarized ourselves with sentimental analysis, let's see if we can find some interesting motifs. We got the idea straight away of comparing the presence of Russian first names for American film villains during the Cold War, and vice versa. 

### USA/URSS

Can we identify broader historical or political trends through morality, character origin and the country of film production? We might ask whether villains in American films are statistically more often Russian and whether, conversely, villains in Russian films are more often of American origin.

PLOT RUSSIA VS USA

Well, the results aren't what we'd hoped for, but are they really that bad? We can see that the villains are mostly from the country in question. That makes sense! Films often tell an internal story in their country of production, so it's only natural that the villains (but also the good guys) should come from that country. However, the question remains: are there really more villains of Slavic origin in Russian films and of English origin in American films, or is this simply the effect of being the majority group? Let's dig deeper.

PLOT PROPORTION US

Ah-ha! The high proportion of English villains in American films was only due to the large number of English names. This graph shows more clearly the proportion of villains, neutrals and good guys for each ethnic group. All ethnic groups have more or less the same distribution, with more good characters than bad. Phew, we're saved, the good guys are in the majority!

Unfortunately, we don't have enough data for Russian films to be able to give us usable results.

So Russians aren't the bad guys in American films? According to our data, no, not especially. Out of curiosity, let's take a look at American films released during the Cold War to see if a trend emerges.

PLOT COLD WAR US

The results aren't very exciting... The same graph is found as for all films. Our hypothesis that Russian names are predominantly the names of villains in American films is not confirmed. One hypothesis to explain this lack of evidence is that the dataset on movies was compiled by Americans, which may introduce a Western-centric bias. This bias could mean that even the Russian movies included in the dataset are those that are more Westernized, potentially leading to an overrepresentation of English-speaking ethnicities as the dominant group, even in Russian films. Additionally, this bias is evident in the underrepresentation of Russian movies, among others, in the dataset, as reflected in the disproportionate number of films produced per country.


VI) CONCLUSION
Congratulations, you’ve reached the end of our data-driven guide to discovering character features based on names! We took you on a journey through the hidden power of linguistics, phonetics, and the broader world of words, and we hope you’ve learned something fascinating along the way. While our exploration revealed some intriguing insights, it’s important to recognize the limitations of our approach. One potential weakness lies in our predictive models for sentiment analysis and ethnicity. These models, despite their potential, may not fully capture the richness or nuance of the datasets they were trained on, which can sometimes lead to oversimplified or inaccurate interpretations. Additionally, the movie dataset itself comes with its own biases. As with any human-generated content, it reflects the inherent biases of its creators and could influence the conclusions drawn about the movie industry.
Despite these challenges, the possibilities are exciting. Imagine knowing the personality traits and attributes of a movie character simply from their name before you’ve even seen the movie. It’s a tantalizing prospect, isn’t it? Of course, it seems difficult to manually analyze character features —and you probably wouldn’t want to count diacritics or analyze n-grams every time you encounter a new character name.
That’s where we come in! We’ve built a model to handle the heavy lifting for you. Just think of a name, and our model will reveal the likely features of that character based on the patterns we’ve uncovered. ADA magic at your fingertips—ready to bring characters to life in ways you’ve never imagined!


## VI. MODEL - autre titre

4 TEST

{% include predictive_model.html %}

### Data Insights
In order to see all the attributes we have analysed and their distribution, take a look at the ‘Our Dataset’ tab, where you will find a detailed overview of our data.