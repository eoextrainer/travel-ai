const regionButtons = document.querySelectorAll('.pill');
const optionsSection = document.getElementById('options');
const regionTitle = document.getElementById('regionTitle');
const transportList = document.getElementById('transport');
const accommodationList = document.getElementById('accommodation');
const foodList = document.getElementById('food');
const sitesList = document.getElementById('sites');
const onsiteList = document.getElementById('onsite');
const saveBtn = document.getElementById('save');
const statusDiv = document.getElementById('status');
const recentList = document.getElementById('recent');

let selections = {
  region: null,
  transport: null,
  accommodation: [],
  food: [],
  sites: [],
  onsite_transport: null
};

function renderList(parent, items, single = false) {
  parent.innerHTML = '';
  items.forEach((text) => {
    const li = document.createElement('li');
    li.textContent = text;
    li.addEventListener('click', () => {
      if (single) {
        [...parent.children].forEach(el => el.classList.remove('selected'));
        li.classList.add('selected');
      } else {
        li.classList.toggle('selected');
      }
    });
    parent.appendChild(li);
  });
}

async function loadRecent() {
  const res = await fetch('/api/selections');
  const data = await res.json();
  recentList.innerHTML = '';
  data.forEach(row => {
    const li = document.createElement('li');
    li.textContent = `${row.region} • ${row.transport} • ${row.onsite_transport}`;
    recentList.appendChild(li);
  });
}

regionButtons.forEach(btn => {
  btn.addEventListener('click', async () => {
    const region = btn.dataset.region;
    selections.region = region;
    regionTitle.textContent = `Region: ${region}`;
    optionsSection.classList.remove('hidden');

    const res = await fetch(`/api/curated/${region}`);
    const data = await res.json();

    const transport = [...data.transport_from_home.bus, ...data.transport_from_home.train, ...data.transport_from_home.airplane];
    renderList(transportList, transport, true);
    renderList(accommodationList, data.accommodation);
    renderList(foodList, data.food);
    renderList(sitesList, data.sites);
    renderList(onsiteList, data.on_site_transport, true);
  });
});

saveBtn.addEventListener('click', async () => {
  const getSelectedTexts = (ul) => [...ul.querySelectorAll('li.selected')].map(el => el.textContent);
  selections.transport = transportList.querySelector('li.selected')?.textContent || null;
  selections.accommodation = getSelectedTexts(accommodationList);
  selections.food = getSelectedTexts(foodList);
  selections.sites = getSelectedTexts(sitesList);
  selections.onsite_transport = onsiteList.querySelector('li.selected')?.textContent || null;

  const res = await fetch('/api/selections', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(selections)
  });
  const data = await res.json();
  statusDiv.textContent = data.status === 'saved' ? 'Saved successfully!' : 'Save failed.';
  await loadRecent();
});

loadRecent();
