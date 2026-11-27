/* Client-side filtering; the complete bibliography remains available without JS. */
(function () {
  'use strict';
  const catalog = document.getElementById('publication-catalog');
  const controls = document.getElementById('publication-search-controls');
  const input = document.getElementById('publication-search');
  const status = document.getElementById('publication-search-status');
  if (!catalog || !controls || !input || !status) return;
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const groups = Array.from(catalog.querySelectorAll('.publication-category')).map(section => {
    const lists = Array.from(section.querySelectorAll('ol.bibliography, ul.bibliography'));
    return { section, lists: lists.map(list => ({
      list,
      heading: list.previousElementSibling && /^H[2-6]$/.test(list.previousElementSibling.tagName) && list.previousElementSibling.classList.contains('bibliography') ? list.previousElementSibling : null,
      entries: Array.from(list.children).filter(li => li.tagName === 'LI' && li.querySelector('.title')).map(li => ({
        li, text: normalize(Array.from(li.querySelectorAll('.title, .author, .periodical, abbr')).map(e => e.textContent).join(' '))
      }))
    })) };
  });
  const total = groups.reduce((n, group) => n + group.lists.reduce((m, list) => m + list.entries.length, 0), 0);
  if (!total) return;
  controls.hidden = false;
  const filter = () => {
    const terms = normalize(input.value.trim()).split(/\s+/).filter(Boolean);
    let count = 0;
    groups.forEach(group => {
      let sectionCount = 0;
      group.lists.forEach(list => {
        let listCount = 0;
        list.entries.forEach(entry => {
          const match = terms.every(term => entry.text.includes(term));
          entry.li.hidden = !match;
          if (match) listCount++;
        });
        list.list.hidden = !listCount;
        if (list.heading) list.heading.hidden = !listCount;
        sectionCount += listCount;
      });
      group.section.hidden = !sectionCount;
      count += sectionCount;
    });
    status.textContent = count + ' of ' + total + ' publications shown';
  };
  input.addEventListener('input', filter);
  filter();
}());
