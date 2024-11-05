special = open("special.txt", "r")
special2 = open("special2.txt", "w")

c ={"普工":6990300, "Software Engineer": 2021300, "Manager":1, "企业董事":1050101, "其他社会服务和居民生活服务人员":4079900,"EHSS":2023100,
"Application Engineer": 2020700,
"企业经理":1050102,
"企业职能部门经理或主管":1050103,	
"生产经营经理":1050104,	
"财务经理":1050105,	
"行政、人事经理":1050106,	
"人事经理":1050107,	
"销售和营销经理":1050108,	
"广告和公关经理":1050109,	
"采购经理":1050110,	
"计算机服务经理":1050111,	
"研究和开发经理":1050112,	
"餐厅、客房经理":1050113,	
"客房经理":1050114,	
"其他企业负责人":1050199,	
"其他企业管理人员":1059900,
"teacher": 2010500,
"文员": 3990000,
"专员": 1,
"服务员": 4030500,
"厨师":4030100,
"医生": 2011700,
"美容美发":4070400,
"护士":	4060100,
"药剂":6140300,
"HR": 2023400}

count = 0
for i in special.readlines():
    l = i[1:]
    if "理发师" in l:
        special2.writelines(l.strip()+"," + str(c["美容美发"]) +"\n")
    elif "小工" in l or "普 工" in l or "临时工" in l or  "寒假工" in l or "短期工" in l or "杂工"in l or "普工" in l or "勤杂工" in l or "手机壳打包300元/天" in l or "报价跟单发单员" in l or "传单派发" in l or "打包工" in l :
        special2.writelines(l.strip()+"," + str(c["普工"]) +"\n")
    elif "家政服务" in l:
        if d["家政服务"] == 0:
            special2.writelines(l.strip()+"," + str(c["其他社会服务和居民生活服务人员"]) +"\n")
        else :
            continue
    elif  "Application Engineer" in l :
        if d["Application Engineer"] == 0:
            d["Application Engineer"] = 1
            special2.writelines(l.strip()+"," + str(c["Application Engineer"]) +"\n")
        else :
            continue
    elif "Network Engineer" in l or "Software Engineer" in l or "Software engineer" in l or "software engineer" in l or "Software Developer" in l :
        if d["Software Engineer"] == 0:
            d["Software Engineer"] = 1
            special2.writelines(l.strip()+"," + str(c["Software Engineer"]) +"\n")
        else :
            continue
    elif "EHSS" in l :
        if d["EHSS"] == 0:
            d["EHSS"] = 1
            special2.writelines(l.strip()+"," + str(c["EHSS"]) +"\n")
        else :
           continue
    elif "manager" in l or "Manager" in l:
        mCode = ""
        if "Actuarial" in l or "Financial" in l or  "Tax" in l or "Account" in l or "account" in l or "Finance" in l or "finance" in l:
            mCode = str(c["财务经理"])
        elif "Lean" in l or "Retail" in l or "KA" in l or "Sales" in l or "sale" in l or "Purchasing" in l or "purchasing" in l or "Market" in l or "market" in l or "price" in l or "pricing" in l or "Pric" in l:
            mCode = str(c["销售和营销经理"])
        elif "EHS" in l or "GA" in l or "Merchandising" in l or "Ops" in l or "RA" in l or "Relationship" in l or "relationship" in l or "Compliance" in l or "Communication" in l:
            mCode = str(c['广告和公关经理'])
        elif "Employee Relations" in l or "Human Resource" in l or "Employment Relation" in l or  "ELR" in l or "TA" in l or "Talent" in l or "People Development" in l or "HR" in l or "hr" in l or "Human Resources" in l:
            mCode = str(c['人事经理'])
        elif "IBM" in l or  "Visual Cloud" in l or  "IT" in l or "it" in l or "Hardware Project" in l:
            mCode = str(c['计算机服务经理'])
        elif "Purchase" in l or "Warehouse" in l or "Soft Good" in l or "Procurement" in l:
            mCode = str(c["采购经理"])
        elif "Client Engagement" in l or "Customer Insights" in l or "customer service" in l or "Client Development" in l or "PPA" in l or "Real Estate" in l or "eCommerce" in l or "Client Implementation" in l or "Clinical Applications" in l or "Agent Development" in l or "Portfolio" in l or "Investment" in l or "General" in l or "Business" in l or "Merchandiser" in l or "Process" in l or "Order" in l or  "Navigation" in l or "Risk" in l or "Partnership" in l or "Innovation" in l or "Banking" in l or "OUTLET" in l or "SHE" in l or "R2R" in l or "CSSC FL" in l or "PV" in l or "Reefer" in l or "Launch" in l or  "Activation" in l or "Solutions Development" in l or "Continuous Improvement" in l or "payment" in l or "Delivery Provisioning" in l or "Function Consumer Protection" in l or "Senior Control Manager" in l or "SDGs" in l or "Affiliate" in l or "SEA" in l or "Air Freight" in l or "Contract" in l or "Partner Success" in l or "Social Media" in l or "Corporate Development" in l or "CR planning" in l or "AP" in l or "Planning" in l or "Experience" in l or  "Internal Control" in l or "Lease" in l or "Proposal" in l or "Business Solution" in l or "Factory" in l or "product" in l or "Admin" in l or "Maintenance" in l or "Strategy" in l or "Agreement" in l or  "Program" in l or "Channel" in l or "Excellence" in l or "Portfolio Manager" in l or "Country Medical" in l or "Business Control" in l or "Training" in l or "HSE" in l or "Manager - Corporate Tax - Tax - Changsha" in l or "production" in l or "Planning Staff" in l or "Asset" in l or "Commercial" in l or "Regional" in l or "Application Manager" in l or "E-Commerce" in l or "APACTraining Workforce Manager" in l or "Strategy Development" in l or "Associate Corporate Banking Manager" in l or "EC/O2O Manager" in l or "Demand Manager Asia" in l or "Services" in l or "Costing" in l or "Plant" in l or "PM" in l or "Service Manager" in l or "BD Manager" in l or "Air Hub Manager" in l or "Revenue Planning" in l or "Delivery Manager" in l or "Clinical Support Manager" in l  or"Manager Charging Strategy" in l or "BD Manager (Civil)" in l or "Growth" in l or "Project" in l or "project" in l or "CRM" in l or "Business Development" in l or "Dealer" in l or "VM" in l or "produec" in l or "Product" in l or "Special Channel" in l:
            mCode = str(c["生产经营经理"])
        elif "Polymer" in l or "Supplier" in l or "Category" in l or "Resourcing" in l or  "Materials" in l or "supply" in l or "Supply" in l or "Store" in l or "Sourcing" in l or "Logistics" in l or "Logistic" in l :
            mCode = str(c["采购经理"])
        elif "Certification Manager" in l or "Area" in l or "Governance" in l:
            mCode = str(c["企业职能部门经理或主管"])
        elif "Assistant" in l or "assistant" in l:
            mCode = str(c["其他企业管理人员"])
        elif "SQE" in l or "QA" in l or "Forensic Investigations Manager" in l or "QMS" in l  :
            mCode = str(c["其他企业管理人员"])
        elif "Agency network" in l or "Metrology" in l or "application&amp;developer" in l or "Data Analysis" in l or "Automation" in l or "IE" in l or "Clinical Development" in l or "Apollo-Manufacturing" in l or "Data/EC" in l or "Network Management" in l or "Material Development" in l or "Affairs" in l or "Medical" in l or "Data Analytics" in l or "Hardware" in l or "Diagnosis &amp;CoE Manager" in l or "Trial" in l or "Lab" in l or "Workcell" in l or "Infrastructure" in l or "Machine Performance" in l or "Construction" in l or "CRO" in l or"Patient Solution" in l or "Mechanical" in l or "Test" in l or "Robotics" in l or "Technology" in l or "Technical" in l or "Engineering" in l or "Testing" in l or "Design" in l :
            mCode = str(c["研究和开发经理"])
        elif "Event" in l or "Meeting" in l or "Organzational Culture" in l or "Operation" in l :
            mCode = str(c["其他企业管理人员"])
        elif "Segment Manager" in l or "Vigilance" in l or "Legal" in l or "OD" in l :
            mCode = str(c["企业职能部门经理或主管"])
        elif "TEX" in l or "GIR" in l or "Royalty" in l or "Regulatory"in l or "Brand" in l or "Content" in l:
            mCode = str(c["广告和公关经理"])
        elif "Branch Manager" in l or "Associate" in l or "Country" in l :
            mCode = str(c["企业职能部门经理或主管"])
        if mCode == "":
            print(l.strip()+"," + mCode )
            count+=1
        special2.writelines(l.strip()+"," + mCode +"\n")
    elif "Sales" in l :
        special2.writelines(l.strip()+"," + str(c["Software Engineer"]) +"\n")
    elif "老师" in l or "教师" in l or "幼教" in l or "教练" in l or "助教" in l :
        special2.writelines(l.strip()+"," + str(c["teacher"]) +"\n")
    elif "文员" in l :
        special2.writelines(l.strip()+"," + str(c["文员"]) +"\n")
    elif "专员" in l :
        special2.writelines(l.strip()+"," + str(c["专员"]) +"\n")
    elif "服务员" in l :
        special2.writelines(l.strip()+"," + str(c["服务员"]) +"\n")
    elif "厨师" in l or "厨" in l or "包子制作师傅" in l  :
        special2.writelines(l.strip()+"," + str(c["厨师"]) +"\n")
    elif "医师" in l or "医生" in l :
        special2.writelines(l.strip()+"," + str(c["医生"]) +"\n")
    elif "护士" in l :
        special2.writelines(l.strip()+"," + str(c["护士"]) +"\n")
    elif "药剂" in l :
        special2.writelines(l.strip()+"," + str(c["药剂"]) +"\n")
    elif "HR" in l or "HRBP" in l  :
        special2.writelines(l.strip()+"," + str(c["HR"]) +"\n")
    else:
        count+=1
        special2.writelines(l)

special2.close()
print(count)