---
layout: page
permalink: /publications/
title: publications
description: Research publications, preprints and books
nav: true
nav_order: 2
---

<p><a href="#refereed">Peer-reviewed publications</a> &middot; <a href="#preprints">Preprints</a> &middot; <a href="#books">Books and chapters</a> &middot; <a href="#workshops">Other workshop contributions</a></p>

<div id="publication-search-controls" class="mb-4" hidden>
  <label for="publication-search">Search publications</label>
  <input type="search" class="form-control" id="publication-search" placeholder="Title, author, venue, or year" autocomplete="off" />
  <small id="publication-search-status" class="form-text text-muted" aria-live="polite"></small>
</div>

<div id="publication-catalog" class="publications">
  <section id="refereed" class="publication-category">
    <h2>Peer-reviewed publications</h2>
    <p>Journal and conference papers, including accepted papers awaiting publication.</p>
    {% bibliography -f {{ site.scholar.bibliography }} --query @*[pubcategory=refereed]* %}
  </section>
  <section id="preprints" class="publication-category">
    <h2>Preprints and manuscripts under review</h2>
    {% bibliography -f {{ site.scholar.bibliography }} --query @*[pubcategory=preprint]* %}
  </section>
  <section id="books" class="publication-category">
    <h2>Books and book chapters</h2>
    {% bibliography -f {{ site.scholar.bibliography }} --query @*[pubcategory=book]* %}
  </section>
  <section id="workshops" class="publication-category">
    <h2>Other workshop contributions</h2>
    {% bibliography -f {{ site.scholar.bibliography }} --query @*[pubcategory=workshop]* %}
  </section>
</div>

<style>
#publication-catalog .publication-category { margin-bottom: 2.5rem; scroll-margin-top: 5rem; }
#publication-catalog [hidden] { display: none !important; }
#publication-catalog .row [id] { scroll-margin-top: 5rem; }
#publication-search-controls[hidden] { display: none !important; }
</style>
<script src="{{ '/assets/js/publication-search.js' | relative_url }}" defer></script>
