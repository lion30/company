#项目架构
1. 销售部sales_department
2. 售前部pre_sales_department
3. 研发部develop_department
4. 设计部design_department
5. 生产部product_department
6. 采购部purchase_department
7. 厂内测试部test_department
8. 质检部quality_department
9. 发货部Delivery_department
10. 工程部engineering_department
11. 技术支持部tech_support_department
12. 人力资源部human_res_department
13. 市场部marketing_department
14. 综合管理部integrated_department

#1. 销售部sales_department
##1.1 线索项目表 Contract_clue
1. 项目编号 clue_number
2. 项目名称 clue_name
3. 线索来源 clue_source
4. 所处行业 belong_industry
5. 项目所在区域clue_area
6. 项目所处阶段 at_stage
7. 下一步工作 next_plan
8. 项目预估合同额 estimate_contract
9. 项目情况简述 intro_situation
10. 线索建立时间 estabish_time
11. 线索最后更新时间 last_update_time
12. 线索建立人 establish_person(fk_User)
13. 项目状态 project_status

##1.2 合同表
1. 合同编号 project_number
2. 合同名称 project_name
3. 合同金额 contract_amount
4. 合同付款方式 contract_payment
5. 订货单位 customer_name
6. 所属行业 belong_industry 
7. 合同所在区域中project_area
8. 签订人员salesperson
9.  

## 1.2 
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
13. 项目状态 project_status

#3.研发部develop_department
##3.1 研发项目表Develop_project
1. 项目编号project_number(fk_Contract_clue)
2. 项目名称project_name(fk_Contract_clue)
3. 项目需求简述project_requirement
4. 涉及产品project_product(fk_Develop_product)
5. 涉及产品负责人project_product_owner(fk_Develop_product)
6. 项目计划完成时间project_finish_plan_time
7. 项目经理project_manager
8. 项目小组成员project_member
9. 项目等级project_level
10. 项目状态project_status

##3.2 研发产品表Develop_product
1. 产品物料编号product_number(fk_Supplier)
2. 产品物料名称product_name(fk_Supplier)
3. 产品单位product_unit(fk_Supplier)
3. 产品构成物料编号product_consist_number_(fk_Supplier)
4. 产品构成物料名称product_consist_name(fk_Supplier)
5. 产品构成物料单位product_consist_unit(fk_Supplier)
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


#4. 设计部design_department
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
2. 装置物料名称product_name(fk_Develop)
3. 材料物料编号material_number(fk_Supplier)
4. 材料物料名称material_name(fk_Supplier)
5. 订单下发时间order_purchase_time
6. 订单状态order_status
7. 订单完成时间order_finish_time

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

#7 厂内测试部test_department
1. 项目编号project_number(fk_Contract_clue)
2. 项目名称project_name(fk_Contract_clue)
3. 测试人员(fk_User)
4. 测试报告test_report
5. 测试开始时间test_starttime
6. 测试结束时间test_endtime
7. 测试结论test_conclusion
8. 项目状态project_status

#8 质检部quality_department
1. 项目编号project_number(fk_Contract_clue)
2. 项目名称project_name(fk_Contract_clue)
3. 质检人员quality_owner(fk_User)
4. 质检开始时间quality_starttime
5. 质检结束时间quality_endtime
6. 产品合格证product_certification
7. 项目状态project_status

#9 发货部Delivery_department
1. 项目编号project_number(fk_Contract_clue)
2. 项目名称project_name(fk_Contract_clue)
3. 物料编号material_number(fk_Supplier)
4. 物料名称material_name(fk_Supplier)
5. 物料数量material_count(fk_Design_department)

#9. 工程部engineering_department
1. 项目编号project_number(fk_Contract_clue)
2. 项目名称project_name(fk_Contract_clue)
3. 项目所属区域project_area(fk_Contract_clue)
4. 项目类型project_type(fk_Contract_clue)
5. 项目实施时间project_implement_time
6. 项目实施内容project_implement_content
7. 项目实施负责人project_implement_employee
8. 项目状态project_status

#10 技术支持部support_department
1. 项目编号project_number(fk_Contract_clue)
2. 项目名称project_name(fk_Contract_clue)
3. 装置名称(fk_Supplier)
4. 技术支持时间support_starttime
5. 技术支持内容support_content
6. 技术支持负责人support_person
7. 完成支持时间support_finishtime
8. 被支持人be_supported_person

#11. 人力资源部human_res_department
## 11.1 员工表 Employee
1. 工号 employee_id
2. 姓名 employee_name
3. 年龄 employee_age
3. 出生日期 birthday
4. 入职时间 enter_company_time
5. 所属部门 employee_department
6. 工龄 staff_seniority
7. 职位 staff_position

## 11.2 部门表 Department
1. 部门名称 department_name
2. 部门备注 department_remark

## 11.3 职位表 Position
1. 职位名称 position_name
2. 职位说明 position_remark

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
