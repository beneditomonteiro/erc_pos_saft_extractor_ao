{
    'name': 'SAF-T AO POS Extractor',
    'version': '1.0',
    'author': 'ERC Implementors',
    'summary': 'Módulo para extrair dados do SAF-T AO POS',
    'website': 'https://www.erc-implementos.com',
    'category': 'Accounting',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/saf_t_xml_extractor_views.xml',
        'wizard/saf_t_xml_export_wizard.xml'
    ],
    'installable': True,
    'application': True,
}