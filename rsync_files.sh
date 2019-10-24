#!/usr/bin/env bash
rsync -r /odoo_ar/odoo-12.0e/botella/sources/odoo-argentina/ ./odoo-argentina --exclude=.git
