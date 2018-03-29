from django.db import models


class Supplier(models.Model):
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
    manufacturer = models.CharField('供应商', max_length=200)
    manufacturer_level = models.PositiveSmallIntegerField('供应商等级', choices=manufacturer_level_choice)
    material_number = models.PositiveIntegerField('物料编号', unique=True)
    material_name = models.CharField('物料名称', max_length=40, unique=True)
    material_group = models.PositiveSmallIntegerField('物料组', choices=material_group_choice,)
    payment_method = models.PositiveSmallIntegerField('付款方式', choices=payment_method_choice)
    material_remarks_supplier = models.CharField('物料备注', max_length=100)
    discount_info = models.CharField('优惠信息', max_length=200)
    material_unit = models.PositiveSmallIntegerField('物料单位', choices=material_unit_choice)
    supply_cycle = models.CharField('供货周期', max_length=100)
    purchase_price = models.IntegerField('采购价格')

    def __str__(self):
        return self.manufacturer

    class Meta:
        verbose_name = "供应商表"
        verbose_name_plural = "供应商表"


class Store(models.Model):
    material_unit_choice = (
        (0, 'pc'),
        (1, 'm'),
        (2, 'm2'),
        (3, 'm3'),
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
    material_number = models.PositiveIntegerField('物料编号', unique=True)
    material_name = models.CharField('物料名称', max_length=40, unique=True)
    material_unit = models.PositiveSmallIntegerField('物料单位', choices=material_unit_choice)
    material_group = models.PositiveSmallIntegerField('物料组', choices=material_group_choice,)
    material_type = models.SmallIntegerField('物料类型', choices=(('o','自产'),('p','外购')))
    manufacturer = models.CharField('供应商', max_length=200)
    material_remarks_store = models.CharField('物料备注', max_length=100)
    inventory_quantity = models.PositiveIntegerField('库存数量')
    store_id = models.PositiveSmallIntegerField('库房序号')
    store_locker = models.PositiveSmallIntegerField('库房柜号')
    locker_x = models.PositiveSmallIntegerField('柜横坐标')
    locker_y = models.PositiveSmallIntegerField('柜纵坐标')
    locker_z = models.PositiveSmallIntegerField('柜深坐标')

    def __str__(self):
        return self.store_location

    class Meta:
        verbose_name = '库存表'
        verbose_name_plural = '库存表'
