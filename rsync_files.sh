#!/usr/bin/env bash
# copia los repositorios de la instalacion local que se construyen con oe
# elimina el .git porque sino los toma como submodules

#rsync -r /odoo_ar/odoo-12.0e/botella/sources/account-financial-tools ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/account-invoicing ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/account-payment ./ --exclude=.git --exclude=setup/

rsync -r /odoo_ar/odoo-12.0e/botella/sources/aeroo_reports/report_aeroo ./aeroo_reports --exclude=.git --exclude=setup/

#rsync -r /odoo_ar/odoo-12.0e/botella/sources/argentina-reporting ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/argentina-sale ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/management-system ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/manufacture ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/miscellaneous ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/odoo-argentina ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/odoo-support ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/partner-contact ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/product ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/reporting-engine ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/sale ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/sale-workflow ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/server-brand ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/server-tools ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/server-ux ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/social ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/stock ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/stock-logistics-warehouse ./ --exclude=.git --exclude=setup/
#rsync -r /odoo_ar/odoo-12.0e/botella/sources/web ./ --exclude=.git --exclude=setup/
