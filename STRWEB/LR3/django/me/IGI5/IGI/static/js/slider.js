class Slider {
    constructor(container, options = {}) {
        this.container = document.querySelector(container);
        this.slides = this.container.querySelectorAll('.slide');
        this.currentSlide = 0;
        this.options = {
            loop: options.loop || false,
            auto: options.auto || false,
            delay: options.delay || 5000,
            stopMouseHover: options.stopMouseHover || false,
        };
        this.init();
    }

    init() {
        this.createPagination();
        this.bindEvents();
        if (this.options.auto) this.startAutoSlide();
    }

    bindEvents() {
        const prevButton = document.querySelector('#prev');
        const nextButton = document.querySelector('#next');

        prevButton.addEventListener('click', () => this.showSlide(this.currentSlide - 1));
        nextButton.addEventListener('click', () => this.showSlide(this.currentSlide + 1));

        if (this.options.stopMouseHover) {
            this.container.addEventListener('mouseover', () => this.stopAutoSlide());
            this.container.addEventListener('mouseout', () => this.startAutoSlide());
        }
    }

    createPagination() {
        const pagination = this.container.querySelector('.pagination');
        pagination.innerHTML = '';
        this.slides.forEach((_, index) => {
            const dot = document.createElement('button');
            dot.addEventListener('click', () => this.showSlide(index));
            pagination.appendChild(dot);
        });
        this.updatePagination();
    }

    updatePagination() {
        const dots = this.container.querySelectorAll('.pagination button');
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === this.currentSlide);
        });
    }

    showSlide(index) {
        if (this.options.loop) index = (index + this.slides.length) % this.slides.length;
        else index = Math.max(0, Math.min(index, this.slides.length - 1));
        this.slides[this.currentSlide].classList.remove('active');
        this.currentSlide = index;
        this.slides[this.currentSlide].classList.add('active');
        this.updatePagination();
    }

    startAutoSlide() {
        this.autoSlideInterval = setInterval(() => this.showSlide(this.currentSlide + 1), this.options.delay);
    }

    stopAutoSlide() {
        clearInterval(this.autoSlideInterval);
    }
}
