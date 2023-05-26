from odoo import models, fields, api, _

class registrasi_material(models.Model):
    _name = 'registrasi.material'

    code = fields.Char(string='Material Code', required=True)
    nama_material = fields.Char(string='Material Name', required=True)
    tipe_material = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Material Type', required=True)
    harga_beli = fields.Float(string='Material Buy Price', required=True)
    nama_supplier = fields.Selection([
        ('joko', 'Joko'),
        ('elios', 'elios')
    ])

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for material in self:
            if material.harga_beli < 100:
                    raise models.ValidationError("Harga beli material harus lebih dari 100.")

