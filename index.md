---
layout: home
title: DISCOVER CHARACTERS' FEATURES BASED ON FIRST NAME
cover-img: /assets/img/IMG_title.jpg
---

## **WRITING THE SCENARIO...**

When *Tarantino* makes his films, you might imagine that he starts with the most obvious choices: the **genre** of the film, the **plot** that will unfold, or the **scenes** that will surprise us. But among these big decisions, there's another, more subtle, but just as crucial: choosing the **characters' first names**. 

![Django](assets/img/quentin-tarantino-peace.gif)

**Bill**, **Rick**, **Django**... how does he make his choice? Is it really a matter of chance, or does each name conceal a clue to the character's identity?  
Take the name *“Jacky”*: do you imagine a rebellious teenager, an adorable Canadian grandmother, or a *“badass”* woman? It's interesting to note that some first names make us think of certain **stereotypes** or specific **character traits**. But what do these names reveal about the characters themselves? In the universe of cinema, each first name can have a considerable impact on the way we perceive a character.  

If you watch a series of **romantic comedies**, you may well start to notice a number of recurring first names. What is hiding behind these repetitions? Are these first names simply **practical** or do they allow us to deduce the **personality** of the characters they refer to?

So, beyond first impressions, the association of first names with character traits may in fact be much more relevant than we think. Through a number of **qualitative** and **syntactic characteristics**, we aim to show that there is no such thing as chance when choosing a first name for a film in the cinema!  

If I told you that *Tarantino's* next character had **your first name**, what would its **attributes** be? It's up to you to find out.

### PETIT JEU

**Well done** if you've got the character right! If not, don't worry. We're now going to take you on a *journey* through our analyses to show you the different ways of predicting a character's **characteristics** using their *first name*.

---

**Preview**: 

Let's start with some **interesting facts** about the most common first names used in movies. First of all, let's take a look at the most common first names in our dataset:

<div class="tabs">
  <button class="tab-button active" data-target="plot-men">Femmes</button>
  <button class="tab-button" data-target="plot-women">Hommes</button>
</div>

<div class="tab-content">
  <div id="plot-men" class="plot-container active">
    <iframe src="{{ site.baseurl }}/assets/plots/1000_most_popular_female_names.html" class="iframe-plot"></iframe>
  </div>
  <div id="plot-women" class="plot-container">
    <iframe src="{{ site.baseurl }}/assets/plots/1000_most_popular_male_names.html" class="iframe-plot"></iframe>
  </div>
</div>

**Johns** and **“Sarahs”** top the list. Can you think of an iconic film that features these two names? Here's a hint: **‘Hasta La Vista Baby’**... 

### AFFICHE "TERMINATOR"

While **John** and **Sarah** are by far the most popular, in more general terms we can see that *female first names* are more evenly distributed than those given to the *male characters*. Among the latter, **John** clearly stands out, being given more than twice as many times as **‘George’**, the second most common male first name.

---

Let's continue by analysing how the most common first names vary according to the **country of origin** of the films, in order to see whether these choices are influenced by different *cultures*.

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/worldmap.html" width="100%" height="400" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

We can see here that in the **English-speaking industries**, the first name **‘John’** is most frequently attributed to male characters, while *female first names* show greater diversity. This confirms the observations made in the previous graphs: *female first names* tend to be more widely distributed than *male first names*, where **‘John’** stands out.

As far as **non-English-speaking countries** are concerned, we can see that the most common first names used by the characters are often of *local origin*.

Now that we've set the scene, let's take a closer look at the **links** between the characters' first names and their **attributes**.

## I. GENDER ANALYSIS - autre titre

Naturally, in order to draw up a **profile** of a character from their name, it is essential to start by identifying their **gender**: *male* or *female*. At first sight, this may seem obvious. However, among the thousands of first names that exist, what is it that makes a first name perceived as *masculine* rather than *feminine*? 

With this in mind, we have undertaken an analysis of first names by looking at the notable differences in their composition between **feminine** and **masculine** first names. 

In the graph below, we compare the **first** and **last letters** of *female* first names with those of *male* first names.

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/first_and_last_letter_by_gender.html" width="100%" height="800" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

Several significant **differences** emerge: *Female* names are much more likely to end with an **‘a’** or **‘e’** compared to *male* names. To further explore this observation, we conducted **chi-square tests** to compare the distributions of initial and final letters between *male* and *female* names. 

The results show that certain parameters, such as the presence of an **‘a’**, **‘d’**, **‘e’**, or **‘s’** at the end of a name, help distinguish **male** names from **female** names with a confidence level greater than **95%**. 

Additionally, by examining the common distribution, we find that nearly **15 times more female names** start and end with an **‘a’** compared to male names, which further reinforces the distinct patterns observed. 

*Perfect!* We now have a first clue to avoid imagining **John** as **Sarah** or **Sarah** as **John**… it’s a great start!


## II. AGE ANALYSIS - autre titre

**Tastes** and **trends** evolve over the years: the names of your grandparents are likely very different from those of your younger cousins. What was original in the past is now considered **traditional**, and this evolution also influences the way characters are named in *cinema*.

But then, can we associate certain names with specific **age groups**? For example, do some names appear more frequently for an *elderly* person compared to a *newborn*?

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/box_plot_age.html" width="100%" height="750" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

These graphs are not very **expressive**… this is probably not the right path to uncover the deepest **secrets** of *Tarantino*. However, we believe we have an **explanation** for this! 

The names of **older people** today are the names of **younger people** from the past. Taking this into account, it is normal not to find any significant difference between the names of characters from different **age groups**. 

## III. MOVIE GENRES ANALYSIS - autre titre

IMAGE DE ROMEO ET JULIETTE (ROMEO) ET PERCIVAL

You've probably already noticed that certain **first names** seem to be associated with **stereotypes** and often appear in the same categories of films. For example, it's hard to imagine a character named **‘Romeo’** being anything other than romantic, passionate, and desperate for love. Similarly, it’s almost impossible to picture a **‘Percival’** as rude, mediocre, and unathletic. 

And it's no **coincidence**! These names are often used to embody specific **archetypes** in films. In fact, they frequently appear in the **‘Romance’** and **‘Action & Adventure’** genres, respectively. 

So, to better understand these connections, let’s explore the **correlations** between **first names** and **film categories**, starting by looking at the most common **first names** in each genre:

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/top_10_names_by_movie_genre.html" width="100%" height="550" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

**Sarah** and **‘John’** continue to be omnipresent in all categories, but we can see that popular first names change according to **film genre**. 

---

Let’s analyze the **syntactic characteristics** of first names according to **film type**:

<div style="display: flex; justify-content: space-around;">
  <img src="/assets/plots/V_C_diff.jpeg" alt="Image 1" width="45%" />
  <img src="/assets/plots/V_C_length.jpeg" alt="Image 2" width="45%" />
</div>

**Great results!** **Conclusive results!** 

This **heatmap** tells us a lot about the remarkable differences between the **syntaxes** of first names present in different **film genres**. Boxes marked with an asterisk show pairs of film types with statistically different **'length'** or **'VOWEL/CONSONANT ratio** distributions (with **95% confidence**) according to the **Tukey test**.

We can now find our way between **‘Terminator’** characters and **‘La La Land’** characters, *phewf*... We're beginning to know a lot about character names... but let’s not stop there — the most interesting is yet to come!

## IV. ORIGIN ANALYSIS - autre titre

Notre jeu de données ne montre pas les **origines ethniques** des prénoms des personnages. C’est là que l'expertise de l’équipe **AdadaSurMonBidet** intervient. Nous avons trouvé un jeu de données supplémentaire (« **Name Ethnicity Dataset** » dans l'onglet 'Resources') qui comprend près de **14 000 prénoms** avec leur origine ethnique. Nous avons développé un modèle **prédictif** basé sur ce jeu de données supplémentaire, afin de pouvoir le généraliser à l'ensemble de notre jeu de données. 

**Impressionnant**, non ? Avec une précision de **72%**, nous avons pu établir les origines ethniques des prénoms de nos personnages pour des recherches ultérieures. Nos catégories d'origines sont :  
- **Slaves**  
- **Romance**  
- **Asie de l'Est**  
- **Anglophones**  
- **Hispaniques**

Les films utilisent des prénoms **culturellement spécifiques** pour renforcer l'**authenticité** de leur contexte. Les clichés sur certaines populations sont utilisés dans le choix des prénoms des personnages pour accentuer certains traits de caractère. Il est donc intéressant de voir s'il est possible de faire des liens entre les prénoms et **l'origine géographique** du prénom, afin de mieux imaginer notre célèbre **personnage mystérieux** dont nous ne connaissons que le prénom.  

Nous avons axé notre analyse sur l'**étude lexicale** des prénoms selon leur origine, car nous estimons que c’est le choix le plus **pertinent** et **intéressant**.

Nous avons commencé notre étude en examinant les distributions des **premières** et **dernières lettres** des prénoms. Nous avons effectué une étude statistique à l’aide du test du **CHI-2** pour déterminer les éléments les plus significatifs. Voici les graphiques que nous avons obtenus, montrant les distributions des origines pour les éléments les plus significatifs (c'est-à-dire les éléments pour lesquels les distributions diffèrent le plus) :

<div class="tabs">
  <button class="tab-button active" data-target="plot-men">First Letter</button>
  <button class="tab-button" data-target="plot-women">Last Letter</button>
</div>

<div class="tab-content">
  <div id="plot-men" class="plot-container active">
    <iframe src="{{ site.baseurl }}/assets/plots/first_letter_by_origin.html" class="iframe-plot"></iframe>
  </div>
  <div id="plot-women" class="plot-container">
    <iframe src="{{ site.baseurl }}/assets/plots/last_letter_by_origin.html" class="iframe-plot"></iframe>
  </div>
</div>

This graph clearly shows that the **first** and **last letters** of first names are very good indicators of the **origin** of a given name. Could we have guessed it? Who is the **Spanish character** between **“Pedro”** and **“Ivan”**? It’s intuitive, of course, but it’s always good to trust **good statistics**!

---

**Letters with accents** are called **diacritical letters**. This is a very interesting and effective way of determining the origin of a given name. We've selected the **4 most significant** ones to illustrate this:

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/diacritic_origin.html" width="100%" height="400" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

This **bar plot** is very telling and shows that it is possible to isolate an **origin** thanks to the presence of certain **diacritical letters**.

---

Finally, it is also possible to use the **articulatory phonetics** of first names to determine their origin. We have chosen to focus on the most telling phonetics: **affricate**, **fricative**, **liquid**, **nasal**, and **occlusive**. We therefore studied the **percentage** of first names, for each origin, that contain each of these **phonetic categories**.

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/phonetics_by_origin.html" width="100%" height="400" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

This analysis is useful, but we expected it to be more **telling**. We observe that names of **Hispanic** and **Romance** origin contain more **liquid consonants** (such as [l] and [r]), while **Slavic** and **English** names show a greater presence of **plosives** (such as [p] and [t]). **Nasals** (such as [m] and [n]) are particularly frequent in **Slavic** and **Hispanic** names, but less so in **Asian** names. On the whole, the phonetic structures of names reflect the specific features of each **origin**.

We now know how to recognize a character's **origin** from his or her **first name**. Now we want to know if it's a **nice character** we're going to get attached to, or a **disgusting one** who's going to disgust us.

## V. SENTIMENTAL ANALYSIS ANALYSIS - autre titre

Which of these two names, **“Toby”** and **“Lucifer”**, would you give to a great villain? Which would you give to a **sympathetic** and **generous** character? I think we agree...

We've all been conditioned to think of some names as synonymous with **kindness** and **trust**, while others symbolize **wickedness** and **terror**. Let's continue our study to find out if there's a **significant difference** between the names of **nice characters** and the names of **nasty characters**.

### **Sentimental Analysis**

Our main dataset does not include information on character **morality**. However, we do have access to all the **movie summaries** in our dataset. We therefore came up with the idea of establishing our characters' **values** ourselves, so that we could study the link between these and their **first names**. 

To achieve this, we carried out a **sentimental analysis** for each first name in our dataset, based on the movie summaries. We began by grouping all the sentences in the summaries according to the **first name** of the character they refer to. From there, we performed sentimental analysis on each first name, enabling us to assess the tendency of certain first names to designate **good guys** or **bad guys**. 

Our sentimental analysis enabled us to classify the first names into **5 different categories**:
**Extraordinary**, we can finally put labels on our first names: **“Very Good Guy”**, **“Good Guy”**, **“Neutral”**, **“Bad Guy”** or **“Very Bad Guy”**. 

So what are the names of the greatest **villains** and those of the most **lovable characters**? Let's take a look:

<div class="tabs">
  <button class="tab-button active" data-target="plot-men">Femmes</button>
  <button class="tab-button" data-target="plot-women">Hommes</button>
</div>

<div class="tab-content">
  <div id="plot-men" class="plot-container active">
    <iframe src="{{ site.baseurl }}/assets/plots/sunburst_good_bad_girls.html" class="iframe-plot"></iframe>
  </div>
  <div id="plot-women" class="plot-container">
    <iframe src="{{ site.baseurl }}/assets/plots/sundburst_good_bad_guy.html" class="iframe-plot"></iframe>
  </div>
</div>

Now that we've familiarized ourselves with **sentimental analysis**, let's see if we can find some interesting **motifs**. 

If you're a fan of **American espionage blockbusters**, you've probably noticed that the villains' names are, in most cases, not English-speaking... But can we say the same in the opposite direction? The idea immediately came to us to compare the presence of **Russian first names** for **American film villains** during the **Cold War**, and vice versa.

### USA/URSS

We might wonder if we can identify broader historical or political trends through morality, character origin, and the country of film production.

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/us-urss.html" width="100%" height="400" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

Well, the results aren't what we'd hoped for, but are they really that **bad**? 

We can see that the **villains** are mostly from the country in question. That makes sense! **Films** often tell an internal story in their **country of production**, so it's only natural that the **villains** (but also the **good guys**) should come from that country. 

However, the question remains: are there really more **villains of Slavic origin** in **Russian films** and of **English origin** in **American films**, or is this simply the effect of being the **majority group**? Let's dig deeper.

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/proportion_us.html" width="100%" height="400" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

**Ah-ha!** The high proportion of **English villains** in **American films** was only due to the large number of **English names**. 

This graph shows more clearly the proportion of **villains**, **neutrals**, and **good guys** for each **ethnic group**. All ethnic groups have more or less the same distribution, with more **good characters** than **bad**. 

**Phew**, we're saved, the **good guys** are in the majority!

Unfortunately, we don't have enough data for **Russian films** to be able to give us **usable results**.

So **Russians** aren't the **bad guys** in **American films**? According to our data, no, not especially. 

Out of curiosity, let's take a look at **American films** released during the **Cold War** to see if a trend emerges.

<div style="box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); margin-top: 20px;">
    <iframe src="{{ site.baseurl }}/assets/plots/cold_war.html" width="100%" height="400" frameborder="0" style="border-radius: 10px; margin-top: 20px; box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);"></iframe>
</div>

The results aren't very **exciting**... The same graph is found as for all films. Our hypothesis that **Russian names** are predominantly the names of **villains** in **American films** is not confirmed. 

One hypothesis to explain this lack of evidence is that the **dataset on movies** was compiled by **Americans**, which may introduce a **Western-centric bias**. This bias could mean that even the **Russian movies** included in the dataset are those that are more **Westernized**, potentially leading to an overrepresentation of **English-speaking ethnicities** as the dominant group, even in **Russian films**. 

Additionally, this bias is evident in the **underrepresentation** of **Russian movies**, among others, in the dataset, as reflected in the disproportionate number of films produced per country.

## Conclusion

**Congratulations**, you’ve reached the end of our **data-driven guide** to discovering **character features** based on names! We took you on a journey through the hidden power of **linguistics**, **phonetics**, and the broader world of **words**, and we hope you’ve learned something **fascinating** along the way.

While our exploration revealed some intriguing insights, it’s important to recognize the **limitations** of our approach. One potential weakness lies in our **predictive models** for **sentiment analysis** and **ethnicity**. These models, despite their potential, may not fully capture the richness or nuance of the datasets they were trained on, which can sometimes lead to **oversimplified** or **inaccurate interpretations**. Additionally, the **movie dataset** itself comes with its own **biases**. As with any human-generated content, it reflects the inherent biases of its creators and could influence the conclusions drawn about the movie industry.

Despite these challenges, the possibilities are **exciting**. Imagine knowing the **personality traits** and **attributes** of a movie character simply from their name before you’ve even seen the movie. It’s a tantalizing prospect, isn’t it?

Of course, it seems difficult to manually analyze **character features** — and you probably wouldn’t want to count **diacritics** or analyze **n-grams** every time you encounter a new character name.

That’s where we come in! We’ve built a **model** to handle the **heavy lifting** for you. Just think of a name, and our model will reveal the likely features of that character based on the patterns we’ve uncovered. **ADA magic** to bring characters to life in ways you’ve never imagined!

## Name Predictor

{% include predictive_model.html %}

### Data Insights
In order to see all the attributes we have analysed and their distribution, take a look at the ‘Our Dataset’ tab, where you will find a detailed overview of our data.
