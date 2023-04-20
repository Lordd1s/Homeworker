const baseUrll = 'http://universities.hipolabs.com/search?country=Finland';

window.onload = () => {
    const url = `${baseUrll}&name=`;
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const resultsContainer = document.getElementById('results');
            resultsContainer.innerHTML = '';
            data.forEach(university => {
                const div = document.createElement('div');
                div.className = 'result'
                const name = document.createElement('h3');
                const link = document.createElement('a');
                const logo = document.createElement('img');

                name.textContent = university.name;
                link.href = university.web_pages[0];
                link.textContent = university.web_pages[0];
                logo.alt = university.name;

                const domain = university.web_pages[0].replace(/^https?:\/\//,'');
                const logoUrl = `https://logo.clearbit.com/${domain}`;
                logo.src = logoUrl;

                div.appendChild(name);
                div.appendChild(link);
                div.appendChild(logo);
                resultsContainer.appendChild(div);
            });
        })
        .catch(error => console.error('Error fetching universities:', error));
};


const baseUrl = 'http://universities.hipolabs.com/search?country=Finland';

		const searchInput = document.getElementById('searchInput');
		const searchButton = document.getElementById('searchButton');

        searchButton.addEventListener('click', () => {
            const searchTerm = searchInput.value;
            const url = searchTerm ? `${baseUrl}&name=${searchTerm}` : baseUrl;
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    const resultsContainer = document.getElementById('results');
                    resultsContainer.innerHTML = '';
                    data.forEach(university => {
                        const div = document.createElement('div');
                        div.className = 'result'
                        const name = document.createElement('h3');
                        const link = document.createElement('a');
                        const logo = document.createElement('img');

                        name.textContent = university.name;
                        link.href = university.web_pages[0];
                        link.textContent = university.web_pages[0];
                        logo.alt = university.name;

                        const domain = university.web_pages[0].replace(/^https?:\/\//,'');
                        const logoUrl = `https://logo.clearbit.com/${domain}`;
                        logo.src = logoUrl;

                        div.appendChild(name);
                        div.appendChild(link);
                        div.appendChild(logo);
                        resultsContainer.appendChild(div);
                    });
                })
                .catch(error => console.error('Error fetching universities:', error));
        });

        

