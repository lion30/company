from django.db import models

manufacturer_level_choice = (
    (0, '推荐'),
    (1, '备选等级1'),
    (2, '备选等级2'),
    (3, '慎选'),
    (4, '禁选'),
)

material_group_choice = (
    (0, '计算机类'),
    (1, '计算机附件'),
    (2, '屏柜'),
    (3, '电缆'),
    (4, '成套设备'),
    (5, '技术服务'),
    (6, '端子'),
    (7, '电源'),
    (8, '芯片'),
    (9, '公司成品装置'),
    (10, '公司半成品装置'),
    (11, '公司插件'),
    (12, '结构件'),
    (13, '办公用品'),
)

payment_method_choice = (
    (0, '款到发货'),
    (1, '货到付款'),
    (2, '按比例付款'),
    (3, '有账期，详见备注'),
)

material_unit_choice = (
    (0, 'pc'),
    (1, 'm'),
    (2, 'm2'),
    (3, 'm3'),
)
class supplier_table(models.Model):
    manufacturer = models.CharField('供应商',max_length=200)
    manufacturer_level = models.SmallIntegerField('供应商等级', manufacturer_level_choice)
    material_number = models.PositiveIntegerField('物料编号')
    material_name = models.CharField('物料名称')
    material_group = models.SmallIntegerField('物料组',choices=material_group_choice)
    payment_method =models.CharField('付款方式', choices=payment_method_choice)
    material_remarks = models.CharField('物料备注', max_length=100)
    discount_info = models.CharField('优惠信息', max_length=200)
    material_unit = models.SmallIntegerField('物料单位', choices=material_unit_choice)
    supply_cycle = models.CharField('供货周期', max_length=100)
    purchase_price = models.IntegerField('采购价格')

class desi_prod_table(models.Model):
    material_number = models.ForeignKey(
        supplier_table,
        on_delete=models.CASCADE,
        to_field=supplier_table.material_number,
        verbose_name='物料编号'
    )
    material_name = models.ForeignKey(
        supplier_table,
        on_delete=models.CASCADE,
        to_field=supplier_table.material_name,
        verbose_name='物料名称'
    )
    material_unit = models.ForeignKey(
        supplier_table,
        on_delete=models.CASCADE,
        to_field=supplier_table.material_unit,
        verbose_name='物料单位'
    )
    material_group = models.ForeignKey(
        supplier_table,
        on_delete=models.CASCADE,
        to_field=supplier_table.material_group,
        verbose_name='物料组'
    )
    manufacturer = models.ForeignKey(
        supplier_table,
        on_delete=models.CASCADE,
        to_field=supplier_table.manufacturer,
        verbose_name='供应商名称'
    )
    material_remarks = models.CharField('物料备注',max_length=100)
    inventory_quantity = models.PositiveIntegerField('库存数量')
    store_location = models.CharField('物料所在位置', max_length=100)

