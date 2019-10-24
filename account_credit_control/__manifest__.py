# Copyright 2012-2017 Camptocamp SA
# Copyright 2017 Okia SPRL (https://okia.be)
# Copyright 2018 Access Bookings Ltd (https://accessbookings.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{'name': 'Account Credit Control',
 'version': '12.0.1.4.0',
 'author': "Camptocamp,"
           "Odoo Community Association (OCA),"
           "Okia,"
           "Access Bookings,"
           "Tecnativa,"
           "ACSONE SA/NV",
 'maintainer': 'Camptocamp',
 'category': 'Finance',
 'depends': [
     'base',
     'account',
     'contacts',
     'mail',
 ],
 'website': 'https://github.com/OCA/account-financial-tools',
 'data': [
     # Security
     "security/res_groups.xml",
     "security/account_security.xml",
     "security/ir.model.access.csv",
     "security/acl_account_credit_control_analysis.xml",
     "security/acl_res_partner_payment_action_type.xml",

     # Views
     "views/account_invoice.xml",
     "views/credit_control_line.xml",
     "views/credit_control_policy.xml",
     "views/credit_control_run.xml",
     "views/res_company.xml",
     "views/res_partner.xml",
     "views/res_config_settings_view.xml",

     # Reports
     "report/report.xml",
     "report/report_credit_control_summary.xml",
     "report/account_credit_control_analysis.xml",

     # Data
     "data/data.xml",

     # Wizards
     "wizard/credit_control_emailer_view.xml",
     "wizard/credit_control_marker_view.xml",
     "wizard/credit_control_printer_view.xml",
     "wizard/credit_control_policy_changer_view.xml",
 ],
 'installable': True,
 'license': 'AGPL-3',
 'application': True,
 }
