from odoo import models, fields, api
import xml.etree.ElementTree as ET
import logging

_logger = logging.getLogger(__name__)

class SafTXMLExtractor(models.Model):
    _name = 'saf_t.xml.extractor'
    _description = 'SAF-T XML Extractor'

    name = fields.Char(string="Nome")
    file = fields.Binary(string="Arquivo SAF-T")
