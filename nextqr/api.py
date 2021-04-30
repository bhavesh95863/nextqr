from __future__ import unicode_literals
import frappe
import os,io
from frappe.model.document import Document
from pyqrcode import create as qrcreate

@frappe.whitelist()
def attach_qrcode(doctype,docname,qrcode):
    filename = 'QRCode_{}.png'.format(docname).replace(os.path.sep, "__")
    qr_image = io.BytesIO()
    url = qrcreate(qrcode, error='L')
    url.png(qr_image, scale=2, quiet_zone=1)
    _file = frappe.get_doc({
        "doctype": "File",
        "file_name": filename,
        "attached_to_doctype": doctype,
        "attached_to_name": docname,
        "attached_to_field": "qrcode_image",
        "is_private": 1,
        "content": qr_image.getvalue()})
    _file.save()
    frappe.db.commit()
    frappe.db.set_value(doctype,docname,"qrcode_image",_file.file_url)