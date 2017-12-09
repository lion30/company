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
12. 市场宣传部marketing_department
13. 综合管理部integrated_department

#1. 销售部
##1.1 线索项目表 contract_clue_table
1. 项目编号 project_number
2. 项目名称 project_name
3. 线索来源 clue_source
4. 所处行业 belong_industry
5. 项目所处阶段 at_stage
6. 下一步计划 next_plan
7. 项目预估合同额 estimate_contract
8. 项目情况简述 intro_situation
9. 线索建立时间 estabish_time
10. 线索最后更新时间 last_update_time
11. 线索建立人 clue_est_person

#2. 售前部
##3.1 售前项目表 presale_tabel
1. 项目编号 project_number(fk)
2. 项目名称 project_name(fk)
3. 物料编号 material_number(fk)
4. 物料名称 material_name(fk)
5. 供货数量 material_count
6. 供货厂家 supplier
7. 标准价格 standard_price
8. 投标价格 bid_price
9. 销售 employee_name
10. 工号 employee_id

#3.研发部

#4. 设计部
##4.1 正式项目表 contract_table
1. 项目编号project_number (fk)
2. 项目名称project_name (fk)
3. 签订时间sign_time
4. 合同额contract_price
5. 销售contact_person(fk)
6. 供货时间delivery_time
7. 物料编号 material_number(fk)
8. 物料名称 material_name(fk)
9. 物料厂家 supplier (fk)
10. 物料数量 material_count

#11.人力资源部
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

###6.职位表 position_table
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




#13. 综合管理部 integrated_department
##13.1 公司发文 company_issuing_table
1. 文章名称 article_name
2. 文章作者 article_author
3. 所属部门 buziness_department
4. 点击量 clicks_count
5. 文章内容 article_content
6. 创建时间 article_estabish_time
7. 文章状态 article_status

##6.2 会议室 meeting_room_table
1. 会议室申请人 employee_name(fk)
2. 会议开始时间 meeting_start_time
3. 会议结束时间 meeting_end_time
4. 会议内容 meeting_content
5. 会议参与人 meeting_partipants
6. 会议室申请状态 meeting_application_status

#6.采购部
正式物料表
1. 物料编号material_number
2. 物料名称material_name
3. 物料单位materail_unit
3. 物料组material_group
4. 生产厂家manufacturer
5. 付款方式payment_method
6. 物料备注 material_remarks
7. 库存数量 inventory_quantity
8. 所在仓库及位置 store_location
9. 供应商manufacturer
10. 供应商等级 manufacturer_level 

