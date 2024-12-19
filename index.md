<style>
.header-title {
  background: url("{{ site.baseurl }}/assets/img/IMG_title.jpg") no-repeat center center;
  background-size: cover;
  color: #FFFFFF !important;
  padding: 4rem 2rem;
  text-align: center;
  font-size: 3rem;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
  width: 100%;
  height: 100vh; /* Ajout de la hauteur */
  position: relative;
  overflow: hidden;
  border: 1px solid red; /* Vérification */
}

body {
  margin: 0;
}
</style>

<div class="header-title">
  <h1>{{ page.title }}</h1>
</div>

<iframe src="{{ site.baseurl }}/assets/plots/presentation_data_values.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/top1000_names.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/top10_names_genres.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/top10_names_country.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/first_last_letter.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/box_plot_features_genre.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/box_plot_features_genres.html" width="100%" height="800" frameborder="0"></iframe>
<iframe src="{{ site.baseurl }}/assets/plots/box_plot_features_age.html" width="100%" height="800" frameborder="0"></iframe>
