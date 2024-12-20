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

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/plot_top1000_names.html" width="100%" height="500" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

Johns’ and “Sarahs” top the list. Can you think of an iconic film that features these two names? Here's a hint: ‘Hasta La Vista Baby’... 

### AFFICHE "TERMINATOR"

While John and Sarah are by far the most popular, in more general terms we can see that female first names are more evenly distributed than those given to the male characters. Among the latter, John clearly stands out, being given more than twice as many times as ‘George’, the second most common male first name.
Let's continue by analysing how the most common first names vary according to the country of origin of the films, in order to see whether these choices are influenced by different cultures.

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/top10_names_country.html" width="100%" height="800" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

We can see here that in the English-speaking industries, the first name ‘John’ is most frequently attributed to male characters, while female first names show greater diversity. This confirms the observations made in the previous graphs: female first names tend to be more widely distributed than male first names, where ‘John’ stands out. As far as non-English-speaking countries are concerned, we can see that the most common first names used by the characters are often of local origin.

Now that we've set the scene, let's take a closer look at the links between the characters' first names and their attributes.

## I. GENDER ANALYSIS - autre titre

Naturally, in order to draw up a profile of a character from their name, it is essential to start by identifying their gender: male or female. At first sight, this may seem obvious. However, among the thousands of first names that exist, what is it that makes a first name perceived as masculine rather than feminine? With this in mind, we have undertaken an analysis of first names by looking at the notable differences in their composition between feminine and masculine first names. In the graph below, we compare the first and last letters of female first names with those of male first names.

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/top10_names_country.html" width="100%" height="500" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

Several striking differences emerge: female first names end much more frequently with an ‘a’ or an ‘e’ than male first names. To investigate this observation further, we carried out Chi-square tests to compare the distributions of initial and final letters between male and female first names. The results show that certain parameters, such as the presence of an ‘a’, a ‘d’, an ‘e’ or an ‘s’ at the end of a first name, make it possible to distinguish between male and female first names with a confidence level of over 95%. Moreover, an examination of the joint distribution shows that almost 15 times as many female first names begin and end with an ‘a’ as male first names, further reinforcing the distinctive patterns observed.

## II. AGE ANALYSIS - autre titre

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/box_plot_features_age.html" width="100%" height="800" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

## III. MOVIE GENRES ANALYSIS - autre titre

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/top10_names_genres.html" width="100%" height="800" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/box_plot_features_genre.html" width="100%" height="800" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/movie_genre_first_letter.html" width="100%" height="800" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/movie_genre_last_letter.html" width="100%" height="800" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

## IV. ORIGIN ANALYSIS - autre titre

## V. SENTIMENTAL ANALYSIS ANALYSIS - autre titre

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/polarity_distribution.html" width="100%" height="800" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/sentiment_analysis_overview.html" width="100%" height="800" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

## VI. MODEL - autre titre

### Data Insights
In order to see all the attributes we have analysed and their distribution, take a look at the ‘Our Dataset’ tab, where you will find a detailed overview of our data.