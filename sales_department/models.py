from django.db import models
from human_res_department.models import Employee
from django.contrib.auth.models import User


class Contractclue(models.Model):
    clue_number = models.CharField('项目编号', max_length=40, unique=True, db_index=True)
    clue_name= models.CharField('项目名称', max_length=200, unique=True)
    clue_source = models.CharField('项目来源', max_length=200)
    belong_industry = models.SmallIntegerField('所属行业', choices=(
        (0, '发电厂'),
        (1, '电网'),
        (2, '工业'),
        (3, '轨道交通'),
        (4, '石油化工'),
        (5, '城市楼宇'),
        (6, '其他')))
    clue_area = models.SmallIntegerField(verbose_name='项目区域',
                                            choices=(
                                                (0, '东北区'),
                                                (1, '西北区'),
                                                (2, '华北区'),
                                                (3, '华南区'),
                                                (4, '华中区'),
                                                (5, '华东区'),
                                                (6, '新疆大区'),
                                                (7, '国际'))
                                            )
    at_stage = models.SmallIntegerField('所处阶段', choices=(
        (0, '寻求机会'),
        (1, '确定用户意向'),
        (2, '招投标')))
    next_plan = models.CharField('下一步工作', max_length=400)
    estimate_contract = models.IntegerField('项目预估合同额')
    intro_situation = models.CharField('项目情况简述', max_length=400)
    establish_time = models.DateField('线索建立时间', auto_now_add=True)
    last_update_time = models.DateField('线索更新时间', auto_now=True)
    establish_person = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='establish_person',
        verbose_name='线索建立人')
    clue_status = models.SmallIntegerField(verbose_name='线索状态',
                                           choices=(
                                               (0, '进行中'),
                                               (1, '暂停'),
                                               (2, '丢失'),
                                           ))
    customer_company = models.CharField(verbose_name='用户单位', max_length=400)
    main_customer_name = models.CharField(verbose_name='主联系人姓名', max_length=40)
    main_customer_contact = models.CharField(verbose_name='主联系人联系方式', max_length=40)
    main_customer_post = models.CharField(verbose_name='用户职位', max_length=40)
    customer_name = models.CharField(verbose_name='用户姓名', max_length=40)
    customer_contact = models.CharField(verbose_name='用户联系方式', max_length=40)
    customer_post = models.CharField(verbose_name='用户职务', max_length=40)
    clue_remark = models.CharField(verbose_name='线索备注', max_length=200)
    competitor_1 = models.CharField(verbose_name='竞争对手1', max_length=60)
    competitor_2 = models.CharField(verbose_name='竞争对手2', max_length=60)
    competitor_3 = models.CharField(verbose_name='竞争对手3', max_length=60)
    success_rate = models.SmallIntegerField(verbose_name='成功率', choices=(
        (0, '无把握'),
        (1, '优于竞争对手'),
        (2, '弱于竞争对手'),
        (3, '基本确定')
    ))

    def __str__(self):
        return '销售线索表'

    class Meta:
        verbose_name = "销售线索表"
        verbose_name_plural = "销售线索表"


class Contract(models.Model):
    project_number = models.CharField(verbose_name='合同编号', max_length=40)
    project_name = models.CharField(verbose_name='合同名称', max_length=200)
    contract_amount = models.IntegerField(verbose_name='合同额')
    contract_payment = models.CharField(verbose_name='合同付款方式', max_length=40)
    customer_company = models.CharField(verbose_name='订货单位', max_length=200)
    customer_level = models.SmallIntegerField(verbose_name='用户等级', choices=(
        (0, '重要用户'),
        (1, '潜力用户'),
        (2, '一般用户'),
        (4, '新用户'),
    ))
    belong_industry = models.CharField(verbose_name='所属行业', max_length=20)
    project_area = models.CharField(verbose_name='项目所在地', max_length=40)
    sales_person = models.ForeignKey(User, on_delete=models.PROTECT,related_name='sign_person')
    approval_person = models.ForeignKey(User, on_delete=models.PROTECT, related_name='approval_person')
    project_stage = models.SmallIntegerField(verbose_name='项目所处阶段', choices=(
        (0, '设计阶段'),
        (1, '生产采购阶段'),
        (2, '厂内测试阶段'),
        (3, '现场调试阶段'),
        (4, '售后服务阶段'),
        (5, '项目暂停'),
    ))
    project_status = models.SmallIntegerField(verbose_name='项目状态', choices=(
        (0, '正常'),
        (1, '设计阶段延误'),
        (2, '生产采购阶段延误'),
        (3, '厂内测试阶段延误'),
        (4, '出厂验收阶段延误'),
        (5, '已发货'),
        (6, '已闭环'),
    ))
    sign_time = models.DateField(verbose_name='合同签订时间')
    contract_file = models.FileField(verbose_name='合同文件')
    supply_time = models.DateField(verbose_name='供货时间')
    is_contract_clue = models.SmallIntegerField(verbose_name='是否关联销售线索', choices=(
        (0, '有关联销售线索'),
        (1, '无关联销售线索'),
    ))
    contract_clue = models.ForeignKey('Contractclue', verbose_name='线索编号', on_delete=models.CASCADE, related_name='contract_clue_number')
    business_leader = models.CharField('商务负责人', max_length=20)
    business_post = models.CharField('商务负责人职务', max_length=40)
    business_leader_contact = models.CharField('商务负责人联系方式', max_length=40)
    technical_leader = models.CharField('用户技术负责人', max_length=20)
    technical_leader_post = models.CharField('用户技术负责人职务',max_length=40)
    technical_leader_contact = models.CharField('用户技术负责人联系方式', max_length=40)
    contract_receipt = models.SmallIntegerField('回款状态', choices=(
        (0, '未回款'),
        (1, '部分回款'),
        (2, '已回款'),
        (3, '延期未回款'),
    ))
    contract_remark = models.CharField('合同备注', max_length=200)

    def __str__(self):
        return '合同表'

    class Meta:
        verbose_name = "销售合同表"
        verbose_name_plural = "销售合同表"


class TechnicalAgreement(models.Model):
    project_info = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='contract_number')
    presale_info = models.ForeignKey(User, on_delete=models.CASCADE, related_name='presale_owner')
    customer_owner = models.CharField('用户技术负责人', max_length=20)
    customer_contact = models.CharField('用户技术负责人联系方式', max_length=20)
    receive_request_time = models.DateTimeField(verbose_name='接收任务时间', auto_now=False, auto_now_add=False)
    technical_agreement_signtime = models.DateField(verbose_name='技术协议签订时间', auto_now=False, auto_now_add=False)
    technical_agreement_doc = models.FileField(verbose_name='技术协议文档')
    project_process = models.SmallIntegerField(verbose_name='项目进度', choices=(
        (0, '正常'),
        (1, '延误'),
        (2, '暂停'),
    ))
    project_status = models.SmallIntegerField(verbose_name='项目状态', choices=(
        (0, '已签订'),
        (1, '已确定技术细节，未正式签订'),
        (2, '未签订'),
        ))
    delivery_receiver = models.CharField(verbose_name='收货人', max_length=20)
    receivering_address= models.CharField(verbose_name='收货地址', max_length=100)
    receiver_contact = models.CharField(verbose_name='收货人联系方式', max_length=20)

    def __str__(self):
        return '技术协议表'

    class Meta:
        verbose_name = '技术协议表'
        verbose_name_plural = '技术协议表'
