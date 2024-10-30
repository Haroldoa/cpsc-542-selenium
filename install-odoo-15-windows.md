Need to install odoo 15 and fleet and hospital apps. Specifically 15 because the selenium code given as example will not work in different versions of the interface. Also hospital is a third party app for version 15 of odoo.

1. install https://nightly.odoo.com/15.0/nightly/exe/odoo_15.0.latest.exe . See https://nightly.odoo.com/15.0/nightly/ for linux versions. More info at https://nightly.odoo.com/
   1. Default postgres username: openpg password: openpgpwd
   2. Make sure to write down passwords
2. install https://apps.odoo.com/apps/modules/15.0/om_hospital/
3. Copy om_hospital under odoo/server/odoo/addons/ (C:\Program Files\Odoo 15.0.20241030\server\odoo\addons)
   1. https://stackoverflow.com/questions/61523261/odoo-13-how-install-custom-module https://www.odoo.com/forum/help-1/how-does-odoo-16-community-edition-install-3rd-party-apps-246700
   2. Restart odoo-server-15.0 in services.msc
   3. Click the tiles on localhost:8069 > go to apps > update apps list > search hospital > install om_hospital
   4. Stay on the page while it loads
   5. Now you can see hospital from top left tiles as an installed app and create patients
4. Install fleet app from app list