---
layout: home
title: DISCOVER CHARACTERS' FEATURES BASED ON FIRST NAME
cover-img: /assets/img/IMG_title.jpg
---

INTRODUCTION

When Tarantino makes his films, you might imagine that he starts with the most obvious choices: the genre of the film, the plot that will unfold, or the scenes that will surprise us. But among these big decisions, there's another, more subtle, but just as crucial: choosing the characters' first names. Bill, Rick, Django... how does he make his choice? Is it really a matter of chance, or does each name conceal a clue to the character's identity?
Take the name “Jacki”’: do you imagine a rebellious teenager, an adorable Canadian grandmother, or a “badass” woman? It's interesting to note that some first names make us think of certain stereotypes or specific character traits. But what do these names reveal about the characters themselves? In the universe of cinema, each first name can have a considerable impact on the way we perceive a character. 
If you watch a series of romantic comedies, you may well start to notice a number of recurring first names. What is hiding behind these repetitions? Are these first names simply practical or do they allow us to deduce the personality of the characters they refer to?

So, beyond first impressions, the association of first names with character traits may in fact be much more relevant than we think. Through a number of qualitative and syntactic characteristics, we aim to show that there is no such thing as chance when choosing a first name for a film in the cinema! If I told you that Tarantino's next character had your first name, what would its attributes be? It's up to you to find out. 

PETIT JEU

Bravo à vous si vous avez bien visualisé le personnage! Si ce n’est pas le cas, ne vous en faites pas. Nous allons maintenant vous faire voyager à travers nos analyses afin de vous montrer les différentes manières de prédire les caractéristiques d’un personnage à l’aide de son prénom.
Preview: Pour commencer, prenons connaissance de quelques informations intéressantes concernant les prénoms les plus distribués dans les films. Tout d’abord, regardons quels sont les prénoms les plus présents dans notre dataset:

<iframe src="{{ site.baseurl }}/assets/plots/plot_top1000_names.html" width="100%" height="800" frameborder="0"></iframe>

Les “John” et les “Sarah” prennent la première place du podium. Pourriez vous penser à un film qui contient les prénoms de nos deux gagnants? Un petit indice: “Hasta La Vista Baby”..

AFFICHE "TERMINATOR"

Désormais, regardons comment les prénoms les plus donnés dans les films varient en fonction du pays d’origine du film.

<iframe src="{{ site.baseurl }}/assets/plots/top10_names_country.html" width="100%" height="800" frameborder="0"></iframe>

Maintenant que nous avons pu planter le décor, passons aux analyses plus poussées des liens entre prénoms des personnages et leurs attributs.

I. GENDER ANALYSIS - autre titre

Naturellement, dans le but de dépeindre un personnage à partir de son nom, il est naturel de commencer par déterminer son genre (homme ou femme). C’est dans cette démarche que nous avons voulu déterminer les différences notables entre les prénoms masculins et les prénoms féminins. Dans le graphique présenté ci-dessous, nous comparons les premières et dernières lettres des noms féminins par rapport à celles des prénoms masculins.

<iframe src="{{ site.baseurl }}/assets/plots/first_last_letter.html" width="100%" height="800" frameborder="0"></iframe>

Ce graphique présente les distributions des première et dernière lettres des prénoms, en fonction des genres, ainsi que leur répartition commune. Nous pouvons observer des différences notables. Par exemple, les prénoms féminins finissent bien plus souvent par un ‘a’ ou un ‘e’ que les prénoms masculins. Nous avons effectué des Chi test entre les distributions masculines et féminines pour chaque première et dernière lettre afin de déterminer quels sont les paramètres qui diffèrent le plus entre les prénoms féminins et masculins. Nous avons trouvé que les paramètres suivants permettent de différencier les prénoms masculins et féminins avec une confiance supérieure à 95%: le fait que le prénom se termine par un ‘a’, un ’d’, un ‘e’ ou encore un ‘s’.
De plus, si l’on regarde la distribution commune, nous remarquons aussi certains motifs qui différencient les prénoms féminins. Le plus marquant est qu’une proportion près de 15 fois plus grande des prénoms féminins commencent et finissent par un ‘a’ par rapport aux prénoms masculins.

II. AGE ANALYSIS - autre titre

<iframe src="{{ site.baseurl }}/assets/plots/box_plot_features_age.html" width="100%" height="800" frameborder="0"></iframe>

III. MOVIE GENRES ANALYSIS - autre titre

<iframe src="{{ site.baseurl }}/assets/plots/top10_names_genres.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/box_plot_features_genre.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/movie_genre_first_letter.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/movie_genre_last_letter.html" width="100%" height="800" frameborder="0"></iframe>

IV. ORIGIN ANALYSIS - autre titre
V. SENTIMENTAL ANALYSIS ANALYSIS - autre titre

<iframe src="{{ site.baseurl }}/assets/plots/polarity_distribution.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/polarit_g_movie_genre.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/polarity_b_movie_genre.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/polarity_box_plot.html" width="100%" height="800" frameborder="0"></iframe>

VI. MODEL - autre titre

