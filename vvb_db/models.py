# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class B2B(models.Model):
    frec = models.BigIntegerField(primary_key=True)
    trec = models.BigIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    detail = models.TextField(blank=True)
    code = models.BigIntegerField()
    company = models.BigIntegerField()
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    date = models.DateField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'b2b'

class Bsheet(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    rcode = models.BigIntegerField()
    cd = models.BooleanField()
    edit = models.NullBooleanField()
    tborder = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'bsheet'

class Company(models.Model):
    name = models.CharField(max_length=40)
    addr = models.TextField()
    place = models.CharField(max_length=40)
    tngst = models.CharField(max_length=40)
    cst = models.CharField(max_length=40, blank=True)
    tin = models.CharField(max_length=40, blank=True)
    area = models.CharField(max_length=5)
    stoffice = models.CharField(max_length=40)
    cperson = models.CharField(max_length=40)
    code = models.IntegerField(primary_key=True)
    vname = models.CharField(max_length=5)
    header1 = models.TextField(blank=True)
    header2 = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    item1 = models.TextField(blank=True)
    item2 = models.TextField(blank=True)
    scode = models.IntegerField(blank=True, null=True)
    sale = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'company'

class Config(models.Model):
    fdate = models.CharField(max_length=5)
    tdate = models.CharField(max_length=5)
    printer = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ledger = models.NullBooleanField()
    product = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'config'

class Counter(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    upcode = models.IntegerField()
    defa = models.IntegerField(blank=True, null=True)
    ttype = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'counter'

class CwUsers(models.Model):
    userid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email_address = models.CharField(max_length=50)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=255)
    info = models.CharField(max_length=50)
    last_loggedin = models.CharField(max_length=100)
    user_level = models.DecimalField(max_digits=65535, decimal_places=65535)
    forgot = models.CharField(max_length=100, blank=True)
    status = models.DecimalField(max_digits=65535, decimal_places=65535)
    class Meta:
        managed = False
        db_table = 'cw_users'

class DbCor(models.Model):
    oid = models.TextField(blank=True) # This field type is a guess.
    party_name = models.CharField(max_length=50, blank=True)
    party_place = models.CharField(max_length=40, blank=True)
    party_suffix = models.CharField(max_length=10, blank=True)
    party_prefix = models.CharField(max_length=10, blank=True)
    led_code = models.IntegerField(blank=True, null=True)
    company = models.BigIntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    code = models.BigIntegerField(blank=True, null=True)
    detail = models.TextField(blank=True)
    bill = models.CharField(max_length=50, blank=True)
    cr = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    db = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    vtype = models.BigIntegerField(blank=True, null=True)
    contra_name = models.CharField(max_length=50, blank=True)
    contra_place = models.CharField(max_length=40, blank=True)
    contra_prefix = models.CharField(max_length=10, blank=True)
    contra_suffix = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'db_cor'

class Employee(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=40)
    address = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    active = models.BooleanField(primary_key=True)
    describe = models.TextField(blank=True)
    canlog = models.NullBooleanField()
    psw = models.CharField(max_length=40, blank=True)
    uname = models.CharField(max_length=6, blank=True)
    change_db = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'employee'

class Envalope(models.Model):
    e_type = models.IntegerField()
    contact_it = models.BigIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    workstation = models.CharField(max_length=100)
    documented = models.CharField(max_length=30, blank=True)
    jobid = models.BigIntegerField(blank=True, null=True)
    receipt = models.CharField(max_length=50, blank=True)
    podcopy = models.CharField(max_length=50, blank=True)
    modif = models.DateTimeField(blank=True, null=True)
    cname = models.CharField(max_length=100, blank=True)
    c_name = models.CharField(max_length=100, blank=True)
    c_addr1 = models.CharField(max_length=100, blank=True)
    c_addr2 = models.CharField(max_length=100, blank=True)
    c_place = models.CharField(max_length=100, blank=True)
    c_phone = models.CharField(max_length=50, blank=True)
    c_addr3 = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'envalope'

class Epabx(models.Model):
    slno = models.IntegerField()
    ext1 = models.CharField(max_length=4, blank=True)
    ext2 = models.CharField(max_length=4, blank=True)
    trunk = models.CharField(max_length=4, blank=True)
    number = models.CharField(max_length=20, blank=True)
    duration = models.CharField(max_length=5, blank=True)
    rate = models.CharField(max_length=5, blank=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    un = models.IntegerField(blank=True, null=True)
    units = models.CharField(max_length=4, blank=True)
    amount = models.TextField(blank=True) # This field type is a guess.
    ctype = models.CharField(max_length=1, blank=True)
    calltype = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True)
    ttime = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'epabx'

class EpxCode(models.Model):
    slno = models.IntegerField()
    number = models.CharField(max_length=10, blank=True)
    unit = models.CharField(max_length=4, blank=True)
    class Meta:
        managed = False
        db_table = 'epx_code'

class HInvoiceMainCN(models.Model):
    stype = models.IntegerField(primary_key=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField()
    dc = models.CharField(max_length=40, blank=True)
    refer = models.CharField(max_length=40, blank=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    esc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sale_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    tdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tdyn = models.NullBooleanField()
    cdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cdyn = models.NullBooleanField()
    vtyn = models.NullBooleanField()
    fwg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    roundoff = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    terms = models.TextField(blank=True)
    attender = models.CharField(max_length=100, blank=True)
    pcode = models.IntegerField()
    p_prefix = models.CharField(max_length=10, blank=True)
    p_suffix = models.CharField(max_length=10, blank=True)
    p_name = models.CharField(max_length=100, blank=True)
    p_addr = models.TextField(blank=True)
    p_tin = models.CharField(max_length=20, blank=True)
    p_cst = models.CharField(max_length=20, blank=True)
    tpt_code = models.IntegerField(blank=True, null=True)
    tpt_name = models.CharField(max_length=100, blank=True)
    tpt_addr = models.TextField(blank=True)
    tpt_contact = models.CharField(max_length=25, blank=True)
    painter = models.IntegerField(blank=True, null=True)
    b_comm = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    b_comm_paid = models.CharField(max_length=2, blank=True)
    b_cpn = models.IntegerField(blank=True, null=True)
    b_cpn_paid = models.CharField(max_length=2, blank=True)
    compcode = models.IntegerField()
    mid = models.CharField(max_length=100)
    uid = models.IntegerField()
    modified = models.DateTimeField()
    id = models.BigIntegerField()
    muid = models.IntegerField(blank=True, null=True)
    mmid = models.CharField(max_length=100, blank=True)
    tid = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'h_invoice_main_c_n'

class HInvoiceMainGoodsTransferFrom(models.Model):
    stype = models.IntegerField(primary_key=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField()
    dc = models.CharField(max_length=40, blank=True)
    refer = models.CharField(max_length=40, blank=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    esc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sale_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    tdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tdyn = models.NullBooleanField()
    cdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cdyn = models.NullBooleanField()
    vtyn = models.NullBooleanField()
    fwg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    roundoff = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    terms = models.TextField(blank=True)
    attender = models.CharField(max_length=100, blank=True)
    pcode = models.IntegerField()
    p_prefix = models.CharField(max_length=10, blank=True)
    p_suffix = models.CharField(max_length=10, blank=True)
    p_name = models.CharField(max_length=100, blank=True)
    p_addr = models.TextField(blank=True)
    p_tin = models.CharField(max_length=20, blank=True)
    p_cst = models.CharField(max_length=20, blank=True)
    tpt_code = models.IntegerField(blank=True, null=True)
    tpt_name = models.CharField(max_length=100, blank=True)
    tpt_addr = models.TextField(blank=True)
    tpt_contact = models.CharField(max_length=25, blank=True)
    painter = models.IntegerField(blank=True, null=True)
    b_comm = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    b_comm_paid = models.CharField(max_length=2, blank=True)
    b_cpn = models.IntegerField(blank=True, null=True)
    b_cpn_paid = models.CharField(max_length=2, blank=True)
    compcode = models.IntegerField()
    mid = models.CharField(max_length=100)
    uid = models.IntegerField()
    modified = models.DateTimeField()
    id = models.BigIntegerField()
    muid = models.IntegerField(blank=True, null=True)
    mmid = models.CharField(max_length=100, blank=True)
    tid = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'h_invoice_main_goods_transfer_from'

class HInvoiceMainGoodsTransferTo(models.Model):
    stype = models.IntegerField(primary_key=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField()
    dc = models.CharField(max_length=40, blank=True)
    refer = models.CharField(max_length=40, blank=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    esc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sale_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    tdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tdyn = models.NullBooleanField()
    cdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cdyn = models.NullBooleanField()
    vtyn = models.NullBooleanField()
    fwg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    roundoff = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    terms = models.TextField(blank=True)
    attender = models.CharField(max_length=100, blank=True)
    pcode = models.IntegerField()
    p_prefix = models.CharField(max_length=10, blank=True)
    p_suffix = models.CharField(max_length=10, blank=True)
    p_name = models.CharField(max_length=100, blank=True)
    p_addr = models.TextField(blank=True)
    p_tin = models.CharField(max_length=20, blank=True)
    p_cst = models.CharField(max_length=20, blank=True)
    tpt_code = models.IntegerField(blank=True, null=True)
    tpt_name = models.CharField(max_length=100, blank=True)
    tpt_addr = models.TextField(blank=True)
    tpt_contact = models.CharField(max_length=25, blank=True)
    painter = models.IntegerField(blank=True, null=True)
    b_comm = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    b_comm_paid = models.CharField(max_length=2, blank=True)
    b_cpn = models.IntegerField(blank=True, null=True)
    b_cpn_paid = models.CharField(max_length=2, blank=True)
    compcode = models.IntegerField()
    mid = models.CharField(max_length=100)
    uid = models.IntegerField()
    modified = models.DateTimeField()
    id = models.BigIntegerField()
    muid = models.IntegerField(blank=True, null=True)
    mmid = models.CharField(max_length=100, blank=True)
    tid = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'h_invoice_main_goods_transfer_to'

class HInvoiceMainQuotation(models.Model):
    stype = models.IntegerField(primary_key=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField()
    dc = models.CharField(max_length=40, blank=True)
    refer = models.CharField(max_length=40, blank=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    esc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sale_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    tdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tdyn = models.NullBooleanField()
    cdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cdyn = models.NullBooleanField()
    vtyn = models.NullBooleanField()
    fwg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    roundoff = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    terms = models.TextField(blank=True)
    attender = models.CharField(max_length=100, blank=True)
    pcode = models.IntegerField()
    p_prefix = models.CharField(max_length=10, blank=True)
    p_suffix = models.CharField(max_length=10, blank=True)
    p_name = models.CharField(max_length=100, blank=True)
    p_addr = models.TextField(blank=True)
    p_tin = models.CharField(max_length=20, blank=True)
    p_cst = models.CharField(max_length=20, blank=True)
    tpt_code = models.IntegerField(blank=True, null=True)
    tpt_name = models.CharField(max_length=100, blank=True)
    tpt_addr = models.TextField(blank=True)
    tpt_contact = models.CharField(max_length=25, blank=True)
    painter = models.IntegerField(blank=True, null=True)
    b_comm = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    b_comm_paid = models.CharField(max_length=2, blank=True)
    b_cpn = models.IntegerField(blank=True, null=True)
    b_cpn_paid = models.CharField(max_length=2, blank=True)
    compcode = models.IntegerField()
    mid = models.CharField(max_length=100)
    uid = models.IntegerField()
    modified = models.DateTimeField()
    id = models.BigIntegerField()
    muid = models.IntegerField(blank=True, null=True)
    mmid = models.CharField(max_length=100, blank=True)
    tid = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'h_invoice_main_quotation'

class HInvoiceMainSales(models.Model):
    stype = models.IntegerField(primary_key=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField()
    dc = models.CharField(max_length=40, blank=True)
    refer = models.CharField(max_length=40, blank=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    esc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sale_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    tdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tdyn = models.NullBooleanField()
    cdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cdyn = models.NullBooleanField()
    vtyn = models.NullBooleanField()
    fwg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    roundoff = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    terms = models.TextField(blank=True)
    attender = models.CharField(max_length=100, blank=True)
    pcode = models.IntegerField()
    p_prefix = models.CharField(max_length=10, blank=True)
    p_suffix = models.CharField(max_length=10, blank=True)
    p_name = models.CharField(max_length=100, blank=True)
    p_addr = models.TextField(blank=True)
    p_tin = models.CharField(max_length=20, blank=True)
    p_cst = models.CharField(max_length=20, blank=True)
    tpt_code = models.IntegerField(blank=True, null=True)
    tpt_name = models.CharField(max_length=100, blank=True)
    tpt_addr = models.TextField(blank=True)
    tpt_contact = models.CharField(max_length=25, blank=True)
    painter = models.IntegerField(blank=True, null=True)
    b_comm = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    b_comm_paid = models.CharField(max_length=2, blank=True)
    b_cpn = models.IntegerField(blank=True, null=True)
    b_cpn_paid = models.CharField(max_length=2, blank=True)
    compcode = models.IntegerField()
    mid = models.CharField(max_length=100)
    uid = models.IntegerField()
    modified = models.DateTimeField()
    id = models.BigIntegerField()
    muid = models.IntegerField(blank=True, null=True)
    mmid = models.CharField(max_length=100, blank=True)
    tid = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'h_invoice_main_sales'

class HInvoiceSubCN(models.Model):
    stype = models.IntegerField(blank=True, null=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    compcode = models.IntegerField(blank=True, null=True)
    item_code = models.IntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True)
    gcode = models.CharField(primary_key=True, max_length=200, blank=True)
    rmethod = models.IntegerField(blank=True, null=True)
    tdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rebamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pcomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    scomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item = models.TextField(blank=True)
    id = models.BigIntegerField()
    muid = models.IntegerField(blank=True, null=True)
    mmid = models.CharField(max_length=100, blank=True)
    tid = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'h_invoice_sub_c_n'

class HInvoiceSubGoodsTransferFrom(models.Model):
    stype = models.IntegerField(blank=True, null=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    compcode = models.IntegerField(blank=True, null=True)
    item_code = models.IntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True)
    gcode = models.CharField(primary_key=True, max_length=200, blank=True)
    rmethod = models.IntegerField(blank=True, null=True)
    tdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rebamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pcomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    scomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item = models.TextField(blank=True)
    id = models.BigIntegerField()
    muid = models.IntegerField(blank=True, null=True)
    mmid = models.CharField(max_length=100, blank=True)
    tid = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'h_invoice_sub_goods_transfer_from'

class HInvoiceSubGoodsTransferTo(models.Model):
    stype = models.IntegerField(blank=True, null=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    compcode = models.IntegerField(blank=True, null=True)
    item_code = models.IntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True)
    gcode = models.CharField(primary_key=True, max_length=200, blank=True)
    rmethod = models.IntegerField(blank=True, null=True)
    tdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rebamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pcomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    scomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item = models.TextField(blank=True)
    id = models.BigIntegerField()
    muid = models.IntegerField(blank=True, null=True)
    mmid = models.CharField(max_length=100, blank=True)
    tid = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'h_invoice_sub_goods_transfer_to'

class HInvoiceSubQuotation(models.Model):
    stype = models.IntegerField(blank=True, null=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    compcode = models.IntegerField(blank=True, null=True)
    item_code = models.IntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True)
    gcode = models.CharField(primary_key=True, max_length=200, blank=True)
    rmethod = models.IntegerField(blank=True, null=True)
    tdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rebamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pcomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    scomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item = models.TextField(blank=True)
    id = models.BigIntegerField()
    muid = models.IntegerField(blank=True, null=True)
    mmid = models.CharField(max_length=100, blank=True)
    tid = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'h_invoice_sub_quotation'

class HInvoiceSubSales(models.Model):
    stype = models.IntegerField(blank=True, null=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    compcode = models.IntegerField(blank=True, null=True)
    item_code = models.IntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True)
    gcode = models.CharField(primary_key=True, max_length=200, blank=True)
    rmethod = models.IntegerField(blank=True, null=True)
    tdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rebamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pcomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    scomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item = models.TextField(blank=True)
    id = models.BigIntegerField()
    muid = models.IntegerField(blank=True, null=True)
    mmid = models.CharField(max_length=100, blank=True)
    mtid = models.DateTimeField(blank=True, null=True)
    party_code = models.IntegerField(blank=True, null=True)
    comm_code = models.CharField(max_length=6, blank=True)
    tid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'h_invoice_sub_sales'

class HLedgerName(models.Model):
    code = models.IntegerField()
    ocode = models.BigIntegerField()
    gcode = models.BigIntegerField(blank=True, null=True)
    prefix = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=10, blank=True)
    place = models.CharField(max_length=40)
    address = models.TextField(blank=True)
    baddress = models.TextField(blank=True)
    daddress = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    tngst = models.CharField(max_length=40, blank=True)
    cst = models.CharField(max_length=20, blank=True)
    tin = models.CharField(max_length=20, blank=True)
    transport = models.BigIntegerField(blank=True, null=True)
    cldays = models.DecimalField(max_digits=3, decimal_places=0)
    clamount = models.BigIntegerField()
    b2b = models.NullBooleanField()
    fupcode = models.BigIntegerField(blank=True, null=True)
    ccode = models.BigIntegerField()
    mid = models.CharField(max_length=30)
    uid = models.BigIntegerField()
    oid = models.BigIntegerField()
    active = models.NullBooleanField()
    modified = models.DateTimeField()
    memo = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'h_ledger_name'

class InvoiceMainCN(models.Model):
    stype = models.IntegerField()
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField()
    dc = models.CharField(max_length=40, blank=True)
    refer = models.CharField(max_length=40, blank=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    esc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sale_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    tdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tdyn = models.NullBooleanField()
    cdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cdyn = models.NullBooleanField()
    vtyn = models.NullBooleanField()
    fwg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    roundoff = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    terms = models.TextField(blank=True)
    attender = models.CharField(max_length=100, blank=True)
    pcode = models.IntegerField()
    p_prefix = models.CharField(max_length=10, blank=True)
    p_suffix = models.CharField(max_length=10, blank=True)
    p_name = models.CharField(max_length=100, blank=True)
    p_addr = models.TextField(blank=True)
    p_tin = models.CharField(max_length=20, blank=True)
    p_cst = models.CharField(max_length=20, blank=True)
    tpt_code = models.IntegerField(blank=True, null=True)
    tpt_name = models.CharField(max_length=100, blank=True)
    tpt_addr = models.TextField(blank=True)
    tpt_contact = models.CharField(max_length=25, blank=True)
    painter = models.IntegerField(blank=True, null=True)
    b_comm = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    b_comm_paid = models.CharField(max_length=2, blank=True)
    b_cpn = models.IntegerField(blank=True, null=True)
    b_cpn_paid = models.CharField(max_length=2, blank=True)
    compcode = models.IntegerField()
    mid = models.CharField(max_length=100)
    uid = models.IntegerField()
    modified = models.DateTimeField()
    tid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'invoice_main_c_n'

class InvoiceMainGoodsTransferFrom(models.Model):
    stype = models.IntegerField()
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_date = models.DateField()
    dc = models.CharField(max_length=40, blank=True)
    refer = models.CharField(max_length=40, blank=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    esc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sale_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    tdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tdyn = models.NullBooleanField()
    cdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cdyn = models.NullBooleanField()
    vtyn = models.NullBooleanField()
    fwg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    roundoff = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    terms = models.TextField(blank=True)
    attender = models.CharField(max_length=100, blank=True)
    pcode = models.IntegerField()
    p_prefix = models.CharField(max_length=10, blank=True)
    p_suffix = models.CharField(max_length=10, blank=True)
    p_name = models.CharField(max_length=100, blank=True)
    p_addr = models.TextField(blank=True)
    p_tin = models.CharField(max_length=20, blank=True)
    p_cst = models.CharField(max_length=20, blank=True)
    tpt_code = models.IntegerField(blank=True, null=True)
    tpt_name = models.CharField(max_length=100, blank=True)
    tpt_addr = models.TextField(blank=True)
    tpt_contact = models.CharField(max_length=25, blank=True)
    painter = models.IntegerField(blank=True, null=True)
    b_comm = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    b_comm_paid = models.CharField(max_length=2, blank=True)
    b_cpn = models.IntegerField(blank=True, null=True)
    b_cpn_paid = models.CharField(max_length=2, blank=True)
    compcode = models.IntegerField()
    mid = models.CharField(max_length=100)
    uid = models.IntegerField()
    modified = models.DateTimeField()
    tid = models.IntegerField()
    inv_no = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'invoice_main_goods_transfer_from'

class InvoiceMainGoodsTransferTo(models.Model):
    stype = models.IntegerField()
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField()
    dc = models.CharField(max_length=40, blank=True)
    refer = models.CharField(max_length=40, blank=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    esc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sale_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    tdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tdyn = models.NullBooleanField()
    cdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cdyn = models.NullBooleanField()
    vtyn = models.NullBooleanField()
    fwg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    roundoff = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    terms = models.TextField(blank=True)
    attender = models.CharField(max_length=100, blank=True)
    pcode = models.IntegerField()
    p_prefix = models.CharField(max_length=10, blank=True)
    p_suffix = models.CharField(max_length=10, blank=True)
    p_name = models.CharField(max_length=100, blank=True)
    p_addr = models.TextField(blank=True)
    p_tin = models.CharField(max_length=20, blank=True)
    p_cst = models.CharField(max_length=20, blank=True)
    tpt_code = models.IntegerField(blank=True, null=True)
    tpt_name = models.CharField(max_length=100, blank=True)
    tpt_addr = models.TextField(blank=True)
    tpt_contact = models.CharField(max_length=25, blank=True)
    painter = models.IntegerField(blank=True, null=True)
    b_comm = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    b_comm_paid = models.CharField(max_length=2, blank=True)
    b_cpn = models.IntegerField(blank=True, null=True)
    b_cpn_paid = models.CharField(max_length=2, blank=True)
    compcode = models.IntegerField()
    mid = models.CharField(max_length=100)
    uid = models.IntegerField()
    modified = models.DateTimeField()
    tid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'invoice_main_goods_transfer_to'

class InvoiceMainQuotation(models.Model):
    stype = models.IntegerField()
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField()
    dc = models.CharField(max_length=40, blank=True)
    refer = models.CharField(max_length=40, blank=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    esc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sale_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    tdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tdyn = models.NullBooleanField()
    cdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cdyn = models.NullBooleanField()
    vtyn = models.NullBooleanField()
    fwg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    roundoff = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    terms = models.TextField(blank=True)
    attender = models.CharField(max_length=100, blank=True)
    pcode = models.IntegerField()
    p_prefix = models.CharField(max_length=10, blank=True)
    p_suffix = models.CharField(max_length=10, blank=True)
    p_name = models.CharField(max_length=100, blank=True)
    p_addr = models.TextField(blank=True)
    p_tin = models.CharField(max_length=20, blank=True)
    p_cst = models.CharField(max_length=20, blank=True)
    tpt_code = models.IntegerField(blank=True, null=True)
    tpt_name = models.CharField(max_length=100, blank=True)
    tpt_addr = models.TextField(blank=True)
    tpt_contact = models.CharField(max_length=25, blank=True)
    painter = models.IntegerField(blank=True, null=True)
    b_comm = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    b_comm_paid = models.CharField(max_length=2, blank=True)
    b_cpn = models.IntegerField(blank=True, null=True)
    b_cpn_paid = models.CharField(max_length=2, blank=True)
    compcode = models.IntegerField()
    mid = models.CharField(max_length=100)
    uid = models.IntegerField()
    modified = models.DateTimeField()
    tid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'invoice_main_quotation'

class InvoiceMainSales(models.Model):
    stype = models.IntegerField()
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField()
    dc = models.CharField(max_length=40, blank=True)
    refer = models.CharField(max_length=40, blank=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    esc_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sale_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    tdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tdyn = models.NullBooleanField()
    cdisc = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cdyn = models.NullBooleanField()
    vtyn = models.NullBooleanField()
    fwg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    roundoff = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    terms = models.TextField(blank=True)
    attender = models.CharField(max_length=100, blank=True)
    pcode = models.IntegerField()
    p_prefix = models.CharField(max_length=10, blank=True)
    p_suffix = models.CharField(max_length=10, blank=True)
    p_name = models.CharField(max_length=100, blank=True)
    p_addr = models.TextField(blank=True)
    p_tin = models.CharField(max_length=20, blank=True)
    p_cst = models.CharField(max_length=20, blank=True)
    tpt_code = models.IntegerField(blank=True, null=True)
    tpt_name = models.CharField(max_length=100, blank=True)
    tpt_addr = models.TextField(blank=True)
    tpt_contact = models.CharField(max_length=25, blank=True)
    painter = models.IntegerField(blank=True, null=True)
    b_comm = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    b_comm_paid = models.CharField(max_length=2, blank=True)
    b_cpn = models.IntegerField(blank=True, null=True)
    b_cpn_paid = models.CharField(max_length=2, blank=True)
    compcode = models.IntegerField()
    mid = models.CharField(max_length=100)
    uid = models.IntegerField()
    modified = models.DateTimeField()
    tid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'invoice_main_sales'

class InvoiceSubCN(models.Model):
    stype = models.IntegerField(blank=True, null=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    compcode = models.IntegerField(blank=True, null=True)
    item_code = models.IntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True)
    gcode = models.CharField(primary_key=True, max_length=200, blank=True)
    rmethod = models.IntegerField(blank=True, null=True)
    tdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rebamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pcomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    scomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item = models.TextField(blank=True)
    id = models.BigIntegerField()
    tid = models.IntegerField()
    party_code = models.IntegerField(blank=True, null=True)
    comm_code = models.CharField(max_length=6, blank=True)
    class Meta:
        managed = False
        db_table = 'invoice_sub_c_n'

class InvoiceSubGoodsTransferFrom(models.Model):
    stype = models.IntegerField(blank=True, null=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    compcode = models.IntegerField(blank=True, null=True)
    item_code = models.IntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True)
    gcode = models.CharField(primary_key=True, max_length=200, blank=True)
    rmethod = models.IntegerField(blank=True, null=True)
    tdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rebamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pcomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    scomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item = models.TextField(blank=True)
    id = models.BigIntegerField()
    tid = models.IntegerField()
    comm_code = models.CharField(max_length=6, blank=True)
    party_code = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'invoice_sub_goods_transfer_from'

class InvoiceSubGoodsTransferTo(models.Model):
    stype = models.IntegerField(blank=True, null=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    compcode = models.IntegerField(blank=True, null=True)
    item_code = models.IntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True)
    gcode = models.CharField(primary_key=True, max_length=200, blank=True)
    rmethod = models.IntegerField(blank=True, null=True)
    tdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rebamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pcomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    scomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item = models.TextField(blank=True)
    id = models.BigIntegerField()
    tid = models.IntegerField()
    party_code = models.IntegerField(blank=True, null=True)
    comm_code = models.CharField(max_length=6, blank=True)
    class Meta:
        managed = False
        db_table = 'invoice_sub_goods_transfer_to'

class InvoiceSubQuotation(models.Model):
    stype = models.IntegerField(blank=True, null=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    compcode = models.IntegerField(blank=True, null=True)
    item_code = models.IntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True)
    gcode = models.CharField(primary_key=True, max_length=200, blank=True)
    rmethod = models.IntegerField(blank=True, null=True)
    tdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rebamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pcomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    scomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item = models.TextField(blank=True)
    id = models.BigIntegerField()
    tid = models.IntegerField()
    party_code = models.IntegerField(blank=True, null=True)
    comm_code = models.CharField(max_length=6, blank=True)
    class Meta:
        managed = False
        db_table = 'invoice_sub_quotation'

class InvoiceSubSales(models.Model):
    stype = models.IntegerField(blank=True, null=True)
    inv_prefix = models.CharField(max_length=3, blank=True)
    inv_no = models.IntegerField(blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    btype = models.IntegerField(blank=True, null=True)
    tcode = models.IntegerField(blank=True, null=True)
    taxper = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    compcode = models.IntegerField(blank=True, null=True)
    item_code = models.IntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True)
    gcode = models.CharField(primary_key=True, max_length=200, blank=True)
    rmethod = models.IntegerField(blank=True, null=True)
    tdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cdamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rebamt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pcomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    scomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item = models.TextField(blank=True)
    id = models.BigIntegerField()
    tid = models.IntegerField()
    comm_code = models.CharField(max_length=6, blank=True)
    party_code = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'invoice_sub_sales'

class InvoiceType(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    prefix = models.CharField(max_length=3, blank=True)
    post = models.NullBooleanField()
    ttype = models.IntegerField()
    reverse = models.NullBooleanField()
    tname = models.CharField(max_length=40, blank=True)
    counter = models.TextField(blank=True)
    company = models.TextField(blank=True)
    line = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'invoice_type'

class ItemMaster(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    gcode = models.CharField(max_length=200, blank=True)
    p_name = models.CharField(max_length=40, blank=True)
    pcode = models.IntegerField(blank=True, null=True)
    dpl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    mrp = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    rec = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cdate = models.DateField(blank=True, null=True)
    cp = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pgp = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    rgp = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    rtcode = models.IntegerField(blank=True, null=True)
    com_code = models.CharField(max_length=6, blank=True)
    cat_code = models.CharField(max_length=6, blank=True)
    td = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cd = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rdlvl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    rdmin = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    rdmax = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    rebate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    pcomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    scomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    bcode = models.IntegerField(blank=True, null=True)
    bname = models.CharField(max_length=40, blank=True)
    stk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'item_master'

class LedgerName(models.Model):
    code = models.IntegerField(primary_key=True)
    ocode = models.BigIntegerField()
    gcode = models.BigIntegerField(blank=True, null=True)
    prefix = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=10, blank=True)
    place = models.CharField(max_length=40)
    address = models.TextField(blank=True)
    baddress = models.TextField(blank=True)
    daddress = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    tngst = models.CharField(max_length=40, blank=True)
    cst = models.CharField(max_length=20, blank=True)
    tin = models.CharField(max_length=20, blank=True)
    transport = models.BigIntegerField(blank=True, null=True)
    cldays = models.DecimalField(max_digits=3, decimal_places=0)
    clamount = models.BigIntegerField()
    b2b = models.NullBooleanField()
    dabadaba = models.BigIntegerField(blank=True, null=True)
    ccode = models.BigIntegerField()
    mid = models.CharField(max_length=100)
    uid = models.BigIntegerField()
    active = models.NullBooleanField()
    modified = models.DateTimeField()
    memo = models.TextField(blank=True)
    fupcode = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'ledger_name'

class Menu(models.Model):
    name = models.CharField(max_length=20)
    label = models.CharField(primary_key=True, max_length=40)
    accel = models.CharField(max_length=40, blank=True)
    tooltips = models.CharField(max_length=40, blank=True)
    actions = models.CharField(max_length=40, blank=True)
    act_data = models.CharField(max_length=40, blank=True)
    users = models.CharField(max_length=100, blank=True)
    ordered = models.BigIntegerField(blank=True, null=True)
    code = models.BigIntegerField(blank=True, null=True)
    mnu = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'menu'

class Mmenu(models.Model):
    mname = models.CharField(max_length=20)
    label = models.CharField(primary_key=True, max_length=40)
    accel = models.CharField(max_length=40, blank=True)
    tooltips = models.CharField(max_length=40, blank=True)
    actions = models.CharField(max_length=40, blank=True)
    act_data = models.CharField(max_length=40, blank=True)
    users = models.CharField(max_length=100, blank=True)
    ordered = models.BigIntegerField(blank=True, null=True)
    code = models.BigIntegerField(blank=True, null=True)
    mnu = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'mmenu'

class Myrec(models.Model):
    cr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    db = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'myrec'

class PackageMaster(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True)
    unit = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    package = models.CharField(max_length=10, blank=True)
    carton = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'package_master'

class PgaDiagrams(models.Model):
    diagramname = models.CharField(primary_key=True, max_length=64)
    diagramtables = models.TextField(blank=True)
    diagramlinks = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'pga_diagrams'

class PgaForms(models.Model):
    formname = models.CharField(primary_key=True, max_length=64)
    formsource = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'pga_forms'

class PgaGraphs(models.Model):
    graphname = models.CharField(primary_key=True, max_length=64)
    graphsource = models.TextField(blank=True)
    graphcode = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'pga_graphs'

class PgaImages(models.Model):
    imagename = models.CharField(primary_key=True, max_length=64)
    imagesource = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'pga_images'

class PgaLayout(models.Model):
    tablename = models.CharField(primary_key=True, max_length=64)
    nrcols = models.SmallIntegerField(blank=True, null=True)
    colnames = models.TextField(blank=True)
    colwidth = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'pga_layout'

class PgaQueries(models.Model):
    queryname = models.CharField(primary_key=True, max_length=64)
    querytype = models.CharField(max_length=1, blank=True)
    querycommand = models.TextField(blank=True)
    querytables = models.TextField(blank=True)
    querylinks = models.TextField(blank=True)
    queryresults = models.TextField(blank=True)
    querycomments = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'pga_queries'

class PgaReports(models.Model):
    reportname = models.CharField(primary_key=True, max_length=64)
    reportsource = models.TextField(blank=True)
    reportbody = models.TextField(blank=True)
    reportprocs = models.TextField(blank=True)
    reportoptions = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'pga_reports'

class PgaScripts(models.Model):
    scriptname = models.CharField(primary_key=True, max_length=64)
    scriptsource = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'pga_scripts'

class Place(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'place'

class Pop13(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'pop13'

class Popi(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'popi'

class Posi117832737984(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi117832737984'

class Posi18040427799(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi18040427799'

class Posi234501139476(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi234501139476'

class Posi289011135826(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi289011135826'

class Posi300701481039(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi300701481039'

class Posi354234140462(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi354234140462'

class Posi429175926721(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi429175926721'

class Posi448577934426(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi448577934426'

class Posi5341926858(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi5341926858'

class Posi540444279825(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi540444279825'

class Posi555094379813(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi555094379813'

class Posi630560251512(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi630560251512'

class Posi638284183033(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi638284183033'

class Posi641824983733(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi641824983733'

class Posi6622588757(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi6622588757'

class Posi667303035797(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi667303035797'

class Posi704341092102(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi704341092102'

class Posi777500752514(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi777500752514'

class Posi889916753261(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi889916753261'

class Posi918401462321(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi918401462321'

class Posi936725199552(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi936725199552'

class Posi9709628767(models.Model):
    date = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True)
    days = models.TextField(blank=True) # This field type is a guess.
    am1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    am2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    am3 = models.IntegerField(blank=True, null=True)
    bal = models.IntegerField(blank=True, null=True)
    cd = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    reco = models.BigIntegerField(blank=True, null=True)
    trec = models.IntegerField(blank=True, null=True)
    orec = models.BigIntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'posi9709628767'

class Printer(models.Model):
    code = models.IntegerField(primary_key=True)
    company = models.TextField(blank=True)
    defa = models.NullBooleanField()
    report_name = models.CharField(max_length=20, blank=True)
    printer_que = models.CharField(max_length=20, blank=True)
    printer_type = models.CharField(max_length=5, blank=True)
    class Meta:
        managed = False
        db_table = 'printer'

class ProductMaster(models.Model):
    code = models.IntegerField(primary_key=True)
    rcode = models.BigIntegerField()
    name = models.CharField(max_length=40)
    gcode = models.CharField(max_length=200)
    short_name = models.CharField(max_length=10)
    print_name = models.CharField(max_length=40)
    ptype = models.IntegerField(blank=True, null=True)
    lcode = models.BigIntegerField(blank=True, null=True)
    disp_name = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'product_master'

class Qpos(models.Model):
    code = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True)
    place = models.CharField(max_length=40, blank=True)
    cr = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    db = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'qpos'

class StockMaster(models.Model):
    code = models.IntegerField()
    opstk = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    rdlevel = models.IntegerField(blank=True, null=True)
    rmin = models.IntegerField(blank=True, null=True)
    rmax = models.IntegerField(blank=True, null=True)
    company = models.IntegerField()
    dt = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'stock_master'

class TaxMaster(models.Model):
    code = models.IntegerField(primary_key=True)
    ttype = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True)
    stper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stcode = models.IntegerField(blank=True, null=True)
    sccode = models.IntegerField(blank=True, null=True)
    edper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    scper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    edcode = models.IntegerField(blank=True, null=True)
    ecper = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    eccode = models.IntegerField(blank=True, null=True)
    taxcode = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    scode = models.IntegerField(blank=True, null=True)
    round = models.IntegerField()
    fwg = models.IntegerField()
    fwgcode = models.IntegerField()
    ocode = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'tax_master'

class Tb(models.Model):
    oname = models.CharField(max_length=40, blank=True)
    ocode = models.BigIntegerField(blank=True, null=True)
    gcode = models.BigIntegerField(blank=True, null=True)
    prefix = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=50, blank=True)
    suffix = models.CharField(max_length=10, blank=True)
    place = models.CharField(max_length=40, blank=True)
    address = models.TextField(blank=True)
    baddress = models.TextField(blank=True)
    daddress = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    tngst = models.CharField(max_length=40, blank=True)
    cst = models.CharField(max_length=20, blank=True)
    tin = models.CharField(max_length=20, blank=True)
    transport = models.BigIntegerField(blank=True, null=True)
    cldays = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    clamount = models.BigIntegerField(blank=True, null=True)
    b2b = models.NullBooleanField()
    fupcode = models.BigIntegerField(blank=True, null=True)
    ccode = models.BigIntegerField(blank=True, null=True)
    mid = models.CharField(max_length=100, blank=True)
    uid = models.BigIntegerField(blank=True, null=True)
    active = models.NullBooleanField()
    modified = models.DateTimeField(blank=True, null=True)
    memo = models.TextField(blank=True)
    code = models.BigIntegerField(blank=True, null=True)
    cr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    db = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tb'

class TitemMaster(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True)
    gcode = models.CharField(max_length=200, blank=True)
    p_name = models.CharField(max_length=40, blank=True)
    pcode = models.IntegerField(blank=True, null=True)
    dpl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    mrp = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    rec = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cdate = models.DateField(blank=True, null=True)
    cp = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pgp = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    rgp = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    rtcode = models.IntegerField(blank=True, null=True)
    com_code = models.CharField(max_length=6, blank=True)
    cat_code = models.CharField(max_length=6, blank=True)
    td = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cd = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rebate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    pcomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    scomm = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'titem_master'

class TproductMaster(models.Model):
    code = models.IntegerField(primary_key=True)
    rcode = models.BigIntegerField()
    name = models.CharField(max_length=40)
    gcode = models.CharField(max_length=200)
    short_name = models.CharField(max_length=10)
    print_name = models.CharField(max_length=40)
    ptype = models.IntegerField(blank=True, null=True)
    lcode = models.BigIntegerField(blank=True, null=True)
    disp_name = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'tproduct_master'

class Transport(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.TextField()
    place = models.CharField(max_length=50)
    contact = models.TextField()
    pcode = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'transport'

class Vtran(models.Model):
    company = models.BigIntegerField()
    date = models.DateField()
    contra = models.BigIntegerField()
    code = models.BigIntegerField()
    detail = models.TextField()
    bill = models.CharField(max_length=50, blank=True)
    cr = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    db = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    vtype = models.BigIntegerField(blank=True, null=True)
    image = models.BigIntegerField(blank=True, null=True)
    ccode = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vtran'

class Year(models.Model):
    code = models.IntegerField(primary_key=True)
    ccode = models.BigIntegerField()
    name = models.CharField(max_length=5)
    sales = models.NullBooleanField()
    active = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'year'

