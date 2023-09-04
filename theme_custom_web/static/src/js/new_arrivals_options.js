/** @odoo-module **/

import options from 'web_editor.snippets.options';

options.registry.NewArrivalsOptions = options.Class.extend({
    start() {
        let newArrivalsRow = this.$target.find('#new-arrivals-row')

        if (newArrivalsRow){
            this._rpc({
                route: '/new_arrivals_list/',
                params:{}
            }).then(data=>{
                let html = ``
                data.forEach(prod=>{
                    html += `<div class="col-lg-3 mb-5">
                        <div class="d-flex align-items-center">
                            <div class="img-container mr-3 rounded">
                                <img class="new_product_image rounded" src="data:image/png;base64,${prod.product_image}"/>
                            </div>
                            <div>
                                <h5 class="mb-0">${prod.product_name}</h5>
                                <div>${prod.product_price}</div>
                            </div>
                        </div>
                    </div>`
                })
                newArrivalsRow.html(html)
            })
        }
    },
})

export default {
    NewArrivalsOptions: options.registry.NewArrivalsOptions,
};