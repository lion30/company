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
1. 线索编号 clue_number
2. 线索名称 clue_name
3. 线索来源 clue_source
4. 所处行业 belong_industry
5. 线索所在区域clue_area
6. 线索所处阶段 at_stage
7. 下一步工作 next_plan
8. 项目预估合同额 estimate_contract
9. 项目情况简述 intro_situation
10. 线索建立时间 estabish_time
11. 线索最后更新时间 last_update_time
12. 线索建立人 establish_person(fk_Employee)
13. 线索状态 clue_status
14. 用户联系人 contact_customer

##1.2 合同表 Contract
1. 合同编号 project_number
2. 合同名称 project_name
3. 合同金额 contract_amount
4. 合同付款方式 contract_payment
5. 订货单位 customer_name
6. 用户等级 customer_level
7. 所属行业 belong_industry
8. 合同所在区域中project_area
9. 签订人员 sales_person (fk_Employee)
10. 批准人员 approval_person(fk_Employee)
11. 项目状态 project_status
12. 合同签订时间 sign_time
13. 合同文件 contract_file
14. 供货时间 supply_time
15. 项目线索 contract_clue(fk_Contract_clue)
16. 技术协议签订时间 technical_agreement_signtime(fk_Technical_agreement)
17. 技术负责人 technical_owner(fk_Employee)
18. 用户商务负责人  
19. 用户技术负责人

## 1.3 技术协议表 Technical_agreement
1. 合同编号 project_number(fk_Contract)
2. 合同名称 project_name(fk_Contract)
3. 合同签订人员 sales_person(fk_Contract)
4. 售前负责人 presale_person(fk_Presale)
5. 用户技术负责人 customer_owner
6. 用户技术负责人联系方式 coutomer_contact
6. 接收任务时间 receive_request_time
7. 技术协议签订时间 technical_agreement_signtime
8. 技术协议 technical_agreement_doc

#2. 售前部presales_department
##3.1 售前项目表 Presale
1. 线索编号 clue_number(fk_Contract_clue)
2. 线索名称 clue_name(fk_Contract_clue)
3. 销售负责人sales_person(fk_Contract_clue)
4. 物料编号 material_number(fk_Supplier)
5. 物料名称 material_name(fk_Supplier)
6. 物料单位 material_unit(fk_Supplier)
7. 供货厂家 supplier(fk_Supplier)
8. 标准价格 standard_outprice(fk_Supplier)
9. 物料类型 product_type(fk_Supplier)
10. 供货数量 material_count
11. 投标价格 bid_price
12. 售前负责人 employee_presale(fk_Employee)
13. 开标时间 bid_open_time
14. 项目状态 project_status

#3.研发部develop_department
##3.1 研发项目表Develop_project
1. 项目编号project_number(fk_Contract)
2. 项目名称project_name(fk_Contract)
3. 项目需求简述project_requirement
4. 涉及产品project_product(fk_Develop_product)
5. 涉及产品负责人project_product_owner(fk_Develop_product)
6. 项目计划完成时间 finish_plan_time
7. 项目经理project_manager(fk_Employee)
8. 项目小组成员project_member
9. 项目等级project_level
10. 项目状态project_status

##3.2 研发成品表 Develop_product
1. 成品物料编号 finished_product_number
2. 成品物料名称 finished_product_name
3. 成品物料单位 finished_product_unit
4. 成品物料数量 finished_product_count
5. 半成品物料编号 semi_finished_product_number(fk_Develop_Semi_product)
6. 半成品物料名称 semi_finished_product_name(fk_Develop_Semi_product)
7. 半成品物料单位 semi_finished_product_unit(fk_Develop_Semi_product)
8. 半成品物料数量 semi_finished_product_count(fk_Develop_Semi_product)
9. 原材料物料编号 semi_finished_product_number_(fk_Raw_material)
10. 原材料物料名称 semi_finished_product_name(fk_Raw_material)
11. 原材料物料单位 semi_finished_product_unit(fk_Raw_material)
12. 原材料构成数量 semi_finished_product_count(fk_Raw_material)
13. 产品一级图 first_class_diagram
14. 产品二级图 second_class_diagram
15. 产品说明书 product_manual
16. 产品产线测试手册 line_test_manual
17. 产品检验报告 Inspection_report
18. 产品源代码 product_code
19. 产品其他资料other_material
20. 产品硬件负责人product_hardware_owner
21. 产品软件负责人product_software_owner
22. 产品上市时间product_list_time(fk_Product_market)
23. 产品退市时间prodduct_delist_time(fk_Product_market)
24. 是否上市 is_list


##3.3 研发半成品表 Develop_semi_product
1. 半成品物料编号semi_product_number
2. 半成品物料名称semi_product_name
3. 半成品物料单位semi_product_unit
4. 原材料物料编号raw_product_number_(fk_Raw_material)
5. 原材料物料名称raw_product_name(fk_Raw_material)
6. 原材料物料单位raw_product_unit(fk_Raw_material)
7. 原材料构成数量raw_product_count(fk_Raw_material)
8. 产品一级图first_class_diagram
9. 产品二级图second_class_diagram
10. 产品说明书product_manual
11. 产品产线测试手册line_test_manual
22. 产品检验报告Inspection_report
13. 产品源代码product_code
14. 产品其他资料other_material
15. 产品硬件负责人product_hardware_owner
16. 产品软件负责人product_software_owner
17. 产品上市时间product_list_time(fk_Product_market)
18. 产品退市时间prodduct_delist_time(fk_Product_market)
19. 半成品更新记录update_log
20. 是否上市 is_list

##3.4 研发软件表 Develop_software
1. 软件物料编号software_number
2. 软件物料名称software_name
3. 软件物料单位software_unit
5. 软件说明书software_instruction
6. 软件安装手册software_manual
7. 软件检验报告Inspection_report
8. 软件前端负责人front_owner(fk_Employee)
9. 软件前端源代码库front_code
10. 软件后端负责人backend_owner(fk_Employee)
11. 软件后端代码库backend_code
12. 软件数据库负责人database_owner(fk_Employee)
12. 数据库代码库database_code
13. 软件通讯负责人commucation_owner(fk_Employee)
14. 通讯代码库communication_code
15. 产品其他资料other_material
16. 软件上市时间product_list_time(fk_Product_market)
17. 软件退市时间prodduct_delist_time(fk_Product_market)
18. 软件更新记录software_update_log
19. 是否上市 is_list

#4. 设计部design_department
##4.1 正式项目表 Project_design
1. 项目编号project_number (fk_Contract)
2. 项目名称project_name (fk_Contract)
3. 签订时间sign_time(fk_Contract)
4. 销售contact_person(fk_Contract)
6. 物料编号 material_number(fk_Supplier)
7. 物料名称 material_name(fk_Supplier)
8. 物料厂家 supplier(fk_Supplier)
9. 物料数量 material_count
10. 图纸drawing
11. 设计负责人design_owner(fk_Employee)
12. 项目状态 project_status

# 5. 生产部production_department
## 5.1 半成品生产Semi_production
1. 需求半成品材料编号 semi_product_number(fk_Develop_Semi_product)
2. 需求半成品材料名称 semi_product_name(fk_Develop_Semi_product)
3. 原材料物料编号 raw_material_number(fk_Develop_Semi_product)
4. 原材料物料名称 raw_material_name(fk_Develop_Semi_product)
5. 原材料数量 raw_material_quantity(fk_Develop_Semi_product)
6. 原材料需求数量 demand_raw_material_quantity
7. 生产订单号 order_number
8. 生产订单名称 order_name
9. 订单下发时间 order_purchase_time
10. 订单状态 order_status
11. 需求数量 demand_quantity
12. 已完成数量 completed_quantity
13. 计划完成时间 plan_completion_time
14. 实际完成时间 order_finish_time
15. 生产负责人 order_owner(fk_Employee)
16. 测试开始时间 test_starttime
17. 测试结束时间 test_endtime
18. 订单备注 order_remark

## 5.1 成品生产Finished_production
1. 需求成品装置编号finished_product_number(fk_Develop_product)
2. 需求成品装置名称finished_product_name(fk_Develop_product)
3. 半成品物料编号semi_finished_product_number(fk_Develop_product)
4. 半成品物料名称semi_finished_product_name(fk_Develop_product)
5. 半成品物料数量semi_finished_product_count(fk_Develop_product)
6. 半成品需求数量demand_semi_finished_quantity
7. 原材料物料编号raw_material_number(fk_Develop_product)
8. 原材料物料名称raw_material_name(fk_Develop_product)
9. 原材料数量raw_material_quantity(fk_Develop_product)
10. 原材料需求数量demand_raw_material_quantity
11. 生产订单号 order_number
12. 生产订单名称 order_name
13. 订单下发时间 order_purchase_time
14. 订单状态order_status
15. 需求数量demand_quantity
16. 已完成数量completed_quantity
17. 计划完成时间 plan_completion_time
18. 实际完成时间order_finish_time
19. 生产负责人 production_owner(fk_Employee)
20. 测试开始时间test_starttime
21. 测试结束时间test_endtime
22. 订单备注order_remark


#6.采购部 purchase_department
##6.1供应商物料表 Supplier
1. 采购负责人purchase_owner(fk_Employee)
2. 供应商manufacturer
3. 供应商等级 manufacturer_level
4. 物料编号material_number
5. 物料名称material_name
6. 物料组material_group
7. 物料类型 material_type
8. 付款方式payment_method
9. 物料备注material_remark
10. 优惠信息 discount_info
11. 物料单位material_unit
12. 供货周期supply_cycle
13. 采购价格purchase_price


##6.2 成品物料表 Finished_material
1. 物料编号material_number(fk_Develop_product)
2. 物料名称material_name(fk_Develop_product)
3. 物料单位materail_unit(fk_Develop_product)
4. 物料组material_group
5. 物料类型material_type
5. 生产厂家manufacturer
6. 物料备注 material_remark
7. 库存数量 inventory_quantity
8. 库房序号 store_id
9. 库房柜号 store_locker
10. 柜横坐标 locker_x
11. 柜纵坐标 locker_y
12. 柜深坐标 locker_z

##6.3 半成品材料表 Semi_finished_material
1. 物料编号material_number(fk_Develop_Semi_product)
2. 物料名称material_name(fk_Develop_Semi_product)
3. 物料单位materail_unit(fk_Develop_Semi_product)
4. 物料组material_group
5. 物料类型material_type
5. 生产厂家manufacturer
6. 物料备注 material_remark
7. 库存数量 inventory_quantity
8. 库房序号 store_id
9. 库房柜号 store_locker
10. 柜横坐标 locker_x
11. 柜纵坐标 locker_y
12. 柜深坐标 locker_z


##6.4 原材料表 Raw_material
1. 物料编号material_number(fk_Supplier)
2. 物料名称material_name(fk_Supplier)
3. 物料单位materail_unit(fk_Supplier)
4. 物料组material_group(fk_Supplier)
5. 物料类型material_type(fk_Supplier)
5. 生产厂家manufacturer(fk_Supplier)
6. 物料备注 material_remark
7. 库存数量 inventory_quantity
8. 库房序号 store_id
9. 库房柜号 store_locker
10. 柜横坐标 locker_x
11. 柜纵坐标 locker_y
12. 柜深坐标 locker_z



#7 厂内测试部test_department
## 7.1 测试表Test_factory
1. 项目编号project_number(fk_Contract)
2. 项目名称project_name(fk_Contract)
3. 测试人员(fk_Employee)
4. 测试报告test_report
5. 图纸drawing
6. 测试开始时间test_starttime
7. 测试结束时间test_endtime
8. 测试结论test_conclusion
9. 项目状态project_status

#8 质检部quality_department
## 8.1 厂内质检表 Quality_factory
1. 项目编号project_number(fk_Contract)
2. 项目名称project_name(fk_Contract)
3. 质检人员quality_owner(fk_Employee)
4. 质检开始时间quality_starttime
5. 质检结束时间quality_endtime
6. 检验结论quality_conclusion
7. 产品合格证product_certification
8. 项目状态project_status

#9 发货部delivery_department
## 9.1 项目发货表 Project_delivery
1. 项目编号project_number(fk_Contract)
2. 项目名称project_name(fk_Contract)
3. 物料编号material_number
4. 物料名称material_name
5. 物料数量material_count
6. 物料单位 material_unit
6. 发货状态 delivery_status
7. 发货文档类 delivery_document
8. 发货负责人 delivery_owner(fk_Employee)
9. 收货人 delivery_receiver
10. 收获地址 receivering_address
11. 收货人联系方式 receiver_contact_information
12. 承运公司 carieer_company
13. 发货单号 invoice_number
14. 发货日期 delivery_time



# 10. 工程部engineering_department
## 10.1 工程表Engineer_project
1. 项目编号project_number(fk_Contract)
2. 项目名称project_name(fk_Contract)
3. 项目所属区域project_area(fk_Contract)
4. 项目类型project_type(fk_Contract)
5. 项目发货状态(fk_Project_delivery)
6. 项目计划时间 plan_implement_time
7. 项目实施时间 implement_time
8. 入场时间 enter_time
9. 离场时间 leave_time
10. 项目实施内容implement_content
11. 遗留问题 remaining_problem
12. 归档资料 archival_information
13. 用户联系人 customer_name
14. 用户联系方式  customer_contact
15. 项目实施负责人implement_owner(fk_Employee)
16. 项目状态project_status

#11 技术支持部support_department
# 11.1 技术支持表Project_support
1. 项目编号project_number(fk_Contract)
2. 项目名称project_name(fk_Contract)
3. 装置名称(fk_Finished_product)
4. 技术支持时间support_starttime
5. 技术支持内容support_content
6. 技术支持负责人support_person(fk_Employee)
7. 完成支持时间support_finishtime
8. 被支持人be_supported_person
9. 被支持人单位 be_supported_firm
10. 提供资料 support_document
11. 遗留问题 remaining_problem

#12. 人力资源部human_res_department
## 12.1 django用户表 auth_user
1. 密码 password
2. 最后登录 last_login
3. 是否超级用户 is_superuser
4. 用户名 username
5. 姓 first_name
6. 名 last_name
7. 邮箱 email
8. 是否员工 is_staff
9. 是否激活 is_active
10. 加入时间 date_joined

## 12.2 员工表 Employee
1. 工号 employee_id
2. 姓名 employee_name(fk_auth_user)
3. 年龄 employee_age
3. 出生日期 birthday
4. 入职时间 enter_company_time
5. 所属部门 employee_department(fk_Department)
6. 工龄 staff_seniority
7. 职位 staff_position(fk_Position)

## 12.3 部门表 Department
1. 部门名称 department_name
2. 部门备注 department_remark

## 12.4 职位表 Position
1. 职位名称 position_name
2. 职位说明 position_remark

# 13. 市场部marketing_department
## 13.1 软件产品市场表 Software_market
1. 软件编号software_number(fk_Develop_software)
2. 软件名称software_name(fk_Develop_software)
3. 软件物料单位software_unit(fk_Develop_software)
4. 物料组material_group(fk_Develop_software)
5. 生产厂家manufacturer(fk_Develop_software)
6. 物料类型material_type(fk_Develop_software)
7. 标准价格standart_price
8. 产品负责人product_owner(fk_Develop_software)
9. 产品市场负责人 market_owner(fk_Employee)
10. 装置上市时间 product_list_time
11. 装置退市时间 product_delist_time
11. 价格修订时间 price_modify_time
12. 价格修订原因 price_modify_reason

## 13.2 装置市场表 Product_market
1. 物料编号material_number(fk_Develop_product)
2. 物料名称material_name(fk_Develop_product)
3. 物料单位materail_unit(fk_Develop_product)
4. 物料组material_group
5. 生产厂家manufacturer
6. 物料类型material_type
7. 标准价格standart_price
8. 产品负责人product_owner(fk_Develop_product)
9. 产品市场负责人 market_owner(fk_Employee)
10. 装置上市时间 product_list_time
11. 装置退市时间 product_delist_time
11. 价格修订时间 price_modify_time
12. 价格修订原因 price_modify_reason

## 13.3 半成品市场表 Semi_product_market
1. 物料编号material_number(fk_Develop_semi_product)
2. 物料名称material_name(fk_Develop_semi_product)
3. 物料单位materail_unit(fk_Develop_semi_product)
4. 物料组material_group
5. 生产厂家manufacturer
6. 物料类型material_type
7. 标准价格standart_price
8. 产品负责人product_owner(fk_Develop_semi_product)
9. 产品市场负责人 market_owner(fk_Employee)
10. 装置上市时间 product_list_time
11. 装置退市时间 product_delist_time
11. 价格修订时间 price_modify_time
12. 价格修订原因 price_modify_reason

# 14. 综合管理部 integrated_department
## 14.1 公司发文 Company_issuing
1. 文章名称 article_name
2. 文章作者 article_author(fk_Employee)
3. 所属部门 buziness_department(fk_Employee)
4. 点击量 clicks_count
5. 文章内容 article_content
6. 创建时间 establish_time
7. 文章状态 article_status

## 14.2 会议室 Meeting_room
1. 会议室申请人 conference_applicant(fk_Employee)
2. 会议开始时间 conference_starttime
3. 会议结束时间 conference_endtime
4. 会议内容 conference_theme
5. 会议参与人 conference_participant
6. 会议室申请状态 room_applicant_status
7. 会议室状态 room_status
