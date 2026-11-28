---
layout: page
permalink: /cv/
title: cv
seo_title: "Curriculum Vitae | Jakub Breier"
seo_description: "Academic and professional CV of Jakub Breier, including education, research publications, industry experience, teaching and academic service."
description: 
nav: true
nav_order: 6
cv_pdf: /assets/pdf/breier_cv_nov27.pdf
---

{% assign cv_url = page.cv_pdf | relative_url %}

<p>My curriculum vitae includes my research publications, education, professional experience, teaching and academic service.</p>

<div class="cv-actions">
  <a class="btn btn-primary" href="{{ cv_url }}" target="_blank" rel="noopener">Open CV (PDF)</a>
  <a class="btn btn-outline-primary" href="{{ cv_url }}" download>Download PDF</a>
</div>

<p class="cv-mobile-note text-muted">For the best experience on a phone or tablet, open the PDF using your device's document viewer.</p>

<div id="cv-preview" data-pdf="{{ cv_url | escape }}" hidden></div>

<style>
.cv-actions { display: flex; flex-wrap: wrap; gap: .5rem; margin: 1rem 0; }
.cv-actions .btn { margin: 0; white-space: normal; }
#cv-preview[hidden] { display: none !important; }
#cv-preview iframe { width: 100%; height: 80vh; min-height: 480px; border: 1px solid var(--global-divider-color, #ddd); border-radius: 4px; display: block; }
@media (min-width: 992px) and (hover: hover) and (pointer: fine) {
  .cv-mobile-note { display: none; }
}
@media (max-width: 575.98px) {
  .cv-actions .btn { flex: 1 1 100%; }
}
</style>
<script src="{{ '/assets/js/cv-viewer.js' | relative_url }}" defer></script>
