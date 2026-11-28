/* Load the browser PDF preview only on desktop-like devices.
 * Direct open/download links work everywhere, including without JavaScript.
 */
(function () {
  'use strict';
  var preview = document.getElementById('cv-preview');
  if (!preview || !preview.dataset.pdf || !window.matchMedia) return;
  var desktop = window.matchMedia('(min-width: 992px) and (hover: hover) and (pointer: fine)');
  function showPreview() {
    if (!desktop.matches || navigator.pdfViewerEnabled === false) {
      preview.hidden = true;
      return;
    }
    if (!preview.firstElementChild) {
      var frame = document.createElement('iframe');
      frame.title = 'Curriculum vitae PDF preview';
      frame.src = preview.dataset.pdf;
      preview.appendChild(frame);
    }
    preview.hidden = false;
  }
  showPreview();
  if (desktop.addEventListener) desktop.addEventListener('change', showPreview);
  else if (desktop.addListener) desktop.addListener(showPreview);
}());
