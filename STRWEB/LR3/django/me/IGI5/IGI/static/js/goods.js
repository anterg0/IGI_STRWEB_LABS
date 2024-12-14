document.addEventListener('DOMContentLoaded', () => {
    const productsPerPage = 3;
    const products = document.querySelectorAll('.card-wrapper');
    const paginationControls = document.getElementById('paginationControls');
    let currentPage = 1;

    // Функция для обновления отображения товаров
    function updateProductDisplay() {
        const startIndex = (currentPage - 1) * productsPerPage;
        const endIndex = startIndex + productsPerPage;

        // Скрываем все товары
        products.forEach((product, index) => {
            if (index >= startIndex && index < endIndex) {
                product.style.display = 'block';
            } else {
                product.style.display = 'none';
            }
        });
    }

    // Функция для отображения кнопок пагинации
    function renderPaginationControls() {
        const totalPages = Math.ceil(products.length / productsPerPage);
        paginationControls.innerHTML = '';  // Очищаем предыдущие элементы пагинации

        // Кнопка "Предыдущая"
        if (currentPage > 1) {
            const prevButton = document.createElement('button');
            prevButton.innerText = '«';
            prevButton.addEventListener('click', () => {
                currentPage--;
                updateProductDisplay();
                renderPaginationControls();
            });
            paginationControls.appendChild(prevButton);
        }

        // Кнопки с номерами страниц
        for (let i = 1; i <= totalPages; i++) {
            const pageButton = document.createElement('button');
            pageButton.innerText = i;
            if (i === currentPage) pageButton.disabled = true;
            pageButton.addEventListener('click', () => {
                currentPage = i;
                updateProductDisplay();
                renderPaginationControls();
            });
            paginationControls.appendChild(pageButton);
        }

        // Кнопка "Следующая"
        if (currentPage < totalPages) {
            const nextButton = document.createElement('button');
            nextButton.innerText = '»';
            nextButton.addEventListener('click', () => {
                currentPage++;
                updateProductDisplay();
                renderPaginationControls();
            });
            paginationControls.appendChild(nextButton);
        }
    }
    const cards = document.querySelectorAll('.card-wrapper');

    cards.forEach(cardWrapper => {
        const card = cardWrapper.querySelector('.card');

        cardWrapper.addEventListener('mousemove', (event) => {
            const { width, height, left, top } = cardWrapper.getBoundingClientRect();
            const mouseX = event.clientX - left;
            const mouseY = event.clientY - top;

            const centerX = width / 2;
            const centerY = height / 2;

            const offsetX = (mouseX - centerX) / centerX;
            const offsetY = (mouseY - centerY) / centerY;

            const rotateX = -offsetY * 20;
            const rotateY = offsetX * 20;

            card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });

        cardWrapper.addEventListener('mouseleave', () => {
            card.style.transform = 'rotateX(0) rotateY(0)';
        });
    });
    // Инициализация
    updateProductDisplay();
    renderPaginationControls();
});
