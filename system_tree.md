#项目架构
1. 销售部sales_department
2. 售前部pre_sales_department
3. 研发部develop_department
4. 设计部design_department
5. 生产部product_department
6. 采购部purchase_department
7. 厂内测试部test_department
8. 质检部quality_department
9. 工程部engineering_department
10. 技术支持部tech_support_department
11. 人力资源部human_res_department
12. 市场部marketing_department
13. 综合管理部integrated_department

#1. 销售部sales_department
##1.1 线索项目表 Contract_clue
1. 项目编号 project_number
2. 项目名称 project_name
3. 线索来源 clue_source
4. 所处行业 belong_industry
5. 项目所在区域project_area
6. 项目所处阶段 at_stage
7. 下一步工作 next_plan
8. 项目预估合同额 estimate_contract
9. 项目情况简述 intro_situation
10. 线索建立时间 estabish_time
11. 线索最后更新时间 last_update_time
12. 线索建立人 establish_person(fk_User)

#2. 售前部pre_sales_department
##3.1 售前项目表 Presale
1. 项目编号 project_number(fk_Contract_clue)
2. 项目名称 project_name(fk_Contract_clue)
3. 销售负责人establish_person(fk_Contract_clue)
4. 物料编号 material_number(fk_Supplier)
5. 物料名称 material_name(fk_Supplier)
6. 供货厂家 supplier(fk_Supplier)
7. 外购标准价格 standard_outprice(fk_Supplier)
8. 自产标准价格 standard_proprice(fk_)
9. 供货数量 material_count
10. 投标价格 bid_price
11. 售前负责人 employee_presale(fk_User)
12. 开标时间 bid_open_time

#3.研发部
##3.1 研发项目表
1. 项目编号project_number(fk)
2. 项目名称project_name(fk)
3. 项目需求简述project_requirement
4. 涉及产品project_product(fk)
5. 涉及产品负责人project_product_owner(fk)
6. 项目计划完成时间project_finish_plan_time
7. 项目经理project_manager
8. 项目小组成员project_member
9. 项目等级project_level
##3.2 研发产品表
1. 产品物料编号product_number(fk)
2. 产品物料名称product_name(fk)
3. 产品构成物料编号product_consist_number_(fk)
4. 产品构成物料名称product_consist_name(fk)
5. 产品构成物料单位product_consist_unit(fk)
6. 产品构成数量product_count
7. 产品一级图first_class_diagram
8. 产品二级图second_class_diagram
9. 产品说明书product_manual
10. 产品产线测试手册line_test_manual
11. 产品出厂测试手册factory_test_manual
12. 产品检验报告Inspection_report
13. 产品源代码product_code
14. 产品其他资料other_material
15. 产品负责人product_owner


#4. 设计部
##4.1 正式项目表 contract_table
1. 项目编号project_number (fk)
2. 项目名称project_name (fk)
3. 签订时间sign_time
4. 销售contact_person(fk)
5. 供货时间delivery_time
6. 物料编号 material_number(fk)
7. 物料名称 material_name(fk)
8. 物料厂家 supplier (fk)
9. 物料数量 material_count

#5. 生产部product_department
1. 装置物料编号product_number(fk_Develop)
2. 装置物料名称
3. 材料物料编号
4. 材料物料名称
5. 订单下发时间
6. 订单状态
7. 订单完成时间

#6.采购部 purchase_department
##6.1供应商物料表 Supplier
1. 供应商manufacturer
2. 供应商等级 manufacturer_level
3. 物料编号material_number
4. 物料名称material_name
5. 物料组material_group
6. 付款方式payment_method
7. 物料备注material_remarks_supplier
8. 优惠信息 discount_info
9. 物料单位material_unit
10. 供货周期supply_cycle
11. 采购价格purchase_price

##6.2 设计生产物料表 Store
1. 物料编号material_number
2. 物料名称material_name
3. 物料单位materail_unit
4. 物料组material_group
5. 物料类型material_type
5. 生产厂家manufacturer
6. 物料备注 material_remarks_store
7. 库存数量 inventory_quantity
8. 库房序号 store_id
9. 库房柜号 store_locker
10. 柜横坐标 locker_x
11. 柜纵坐标 locker_y
12. 柜深坐标 locker_z

#7 厂内测试部
1. 项目编号
2. 项目名称
3. 测试人员(fk_User)
4. 测试报告
5. 测试开始时间
6. 测试结束时间

#8 质检部
1. 项目编号
2. 项目名称
3. 质检人员
4. 质检开始时间
5. 质检结束时间
6. 产品合格证

#9. 工程部
1. 项目编号project_number(fk)
2. 项目名称project_name(fk)
3. 项目所属区域project_area
4. 项目类型project_type
5. 项目实施时间project_implement_time
6. 项目实施内容project_implement_content
7. 项目实施负责人project_implement_employee
8. 项目状态project_status

#10 技术支持部
1. 项目编号
2. 项目名称
3. 装置类型
4. 技术支持时间
5. 技术支持内容
6. 技术支持负责人
7. 完成支持时间

#11. 人力资源部
###11.1 业务部门表 business_department
1. 销售部sales_department
2. 售前部pre_sales_department
3. 研发部develop_department
4. 设计部design_department
5. 生产部product_department
6. 采购部purchase_department
7. 厂内测试部test_department
8. 质检部quality_department
9. 工程部engineering_department
10. 技术支持部tech_support_department
11. 人力资源部human_res_department
12. 市场宣传部marketing_department

###11.2 人员表 staff_table
1. 工号 job_number
2. 姓名 employee_name
3. 出生年月 birthday
4. 进入公司时间enter_company_time
5. 工龄 staff_seniority
6. 所属部门 department(fk)
7. 职位 staff_position(fk)

###11.3 职位表 position_table
1. 售前工程师 presale_engineer
2. 设计工程师 design_engineer
3. 销售经理 sales_engineer
4. 市场专员 market_engineer
5. 库房管理员 storeroom_keeper
6. 部门经理 department_manager
7. 部门副经理 deputy_department_manager
8. 大区经理 region_sales_manager
9. 省区经理 provincial_manager
10. 生产副总经理 deputy_production_gmanager
11. 销售副总经理 deputy_sales_gmanager
12. 市场副总经理 deputy_marketing_gmanager
13. 生产总经理 production_gmanager
14. 销售总经理 sales_gmanager
15. 市场总经理 market_gmanager
16. 综合管理部副经理 deputy_integrated_manager
17. 综合管理部经理 integrated_manager
16. 总经理 general_manager
17. 总经理助理 general_namager_assistant

#12. 市场部marketing_department
##12.1 自产信息表
1. 物料编号material_number
2. 物料名称material_name
3. 物料单位materail_unit
4. 物料组material_group
5. 生产厂家manufacturer
3. 物料类型material_type
4. 标准价格standart_price
5. 产品负责人product_owner

#13. 综合管理部 integrated_department
##13.1 公司发文 company_issuing_table
1. 文章名称 article_name
2. 文章作者 article_author
3. 所属部门 buziness_department
4. 点击量 clicks_count
5. 文章内容 article_content
6. 创建时间 article_establish_time
7. 文章状态 article_status

##13.2 会议室 meeting_room_table
1. 会议室申请人 conference_applicant(fk)
2. 会议开始时间 conference_start_time
3. 会议结束时间 conference_end_time
4. 会议内容 conference_theme
5. 会议参与人 conference_participant
6. 会议室申请状态 room_applicant_status
7. 会议室状态 room_status
