/** @odoo-module **/

import publicWidget from "web.public.widget";

publicWidget.registry.NewArrivals = publicWidget.Widget.extend({
    selector: ".section_new_arrivals",
    start() {
        let newArrivalsRow = this.el.querySelector("#new-arrivals-row");
        let productCarousel = this.el.querySelector("#product-carousel");

        if (newArrivalsRow) {
            this._rpc({
                route: "/new_arrivals_list/",
                params: {},
            }).then((data) => {
                let carouselItems = ``;

                data.forEach((prod) => {
                    carouselItems +=
                        `<div class="item">` +
                            `<div class="card h-100 text-center rounded-0 s_card_style_1 tp_product_card">` +
                                `<div>
                                    <div class="img-container mr-3 rounded">
                                        <img class="new_product_image rounded" src="data:image/png;base64,${prod.product_image}"/>
                                    </div>
                                    <h5 class="mb-0">${prod.product_name}</h5>
                                    <div>${prod.product_price}</div>
                                </div>` +
                            `</div>` +
                        `</div>`
                })


                newArrivalsRow.innerHTML =
                    `<div class="owl-carousel" id="product-carousel">` +
                        carouselItems +
                    `</div>`

                productCarousel.owlCarousel({
                    loop: true, // Enable looping
                    margin: 20, // Margin between items
                    responsiveClass: true,
                    responsive: {
                        0: {
                            items: 1, // Number of items to display on small screens
                        },
                        600: {
                            items: 3, // Number of items to display on medium screens
                        },
                        1000: {
                            items: 4, // Number of items to display on large screens
                        },
                    },
                });
            });
        }
    },
});
