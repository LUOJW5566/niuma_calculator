import streamlit as st

# 初始化页面标题
st.title("牛马含量计算器")

# 用户输入基本信息
with st.form("user_info"):
    # 个人信息
    age = st.number_input("请输入您的年龄", min_value=18, max_value=65, value=25)
    marital_status = st.radio("您的婚姻状况", ["未婚", "已婚"])
    education = st.selectbox("您的学历", ["高中及以下", "大专", "本科", "硕士", "博士"])
    city = st.selectbox("您居住的城市", ["一线城市", "二线城市", "三线及以下城市"])
    
    # 工作信息
    job_type = st.selectbox("工作性质", ["国企", "私企", "外企", "创业", "自由职业"])
    salary = st.number_input("税前月薪（元）", min_value=0, value=8000)
    work_hours = st.slider("每周工作时间（小时）", 40, 100, 40)
    commute_time = st.slider("单程通勤时间（分钟）", 0, 180, 30)
    has_overtime = st.checkbox("是否经常加班")
    has_overtime_pay = st.checkbox("是否有加班费")
    has_weekend_work = st.checkbox("是否经常周末工作")
    job_satisfaction = st.slider("工作满意度 (1-10分)", 1, 10, 5)
    
    # 人际关系
    leader_relationship = st.slider("与领导关系 (1-10分)", 1, 10, 5)
    colleague_relationship = st.slider("与同事关系 (1-10分)", 1, 10, 5)
    
    # 福利待遇
    subsidy = st.number_input("每月补助（元）", min_value=0, value=0)
    housing_fund = st.slider("公积金缴纳比例（%）", 0, 12, 5)
    
    # 生活状况
    housing = st.radio("住房情况", ["租房", "自有无贷", "自有有贷"])
    housing_cost = st.number_input("每月房租/房贷支出（元）", min_value=0, value=0)
    has_side_job = st.checkbox("是否有副业")
    has_health_check = st.checkbox("近一年内是否有体检")
    stress_level = st.slider("主观精神压力 (1-10分)", 1, 10, 5)
    
    submitted = st.form_submit_button("计算牛马含量")

# 计算逻辑
if submitted:
    # 初始化分数
    score = 0
    
    # 个人信息权重
    if age >= 35:
        score += 10
    if marital_status == "已婚":
        score += 5
        
    # 学历与薪资匹配度
    edu_weight = {"高中及以下": 0, "大专": 1, "本科": 2, "硕士": 3, "博士": 4}
    expected_salary = edu_weight[education] * 5000 + 8000
    if salary < expected_salary * 0.8:
        score += 20
    elif salary < expected_salary:
        score += 10
        
    # 工作强度
    if work_hours > 50:
        score += 10
    if has_overtime and not has_overtime_pay:
        score += 15
    if has_weekend_work:
        score += 10
        
    # 通勤
    if commute_time > 60:
        score += 15
    elif commute_time > 30:
        score += 10
        
    # 人际关系
    if leader_relationship < 5:
        score += 10
    if colleague_relationship < 5:
        score += 5
        
    # 福利待遇
    if housing_fund < 5:
        score += 10
    if subsidy < 1000:
        score += 5
        
    # 生活压力
    if housing == "租房":
        score += 10
    elif housing == "自有有贷":
        score += 5
    if housing_cost > salary * 0.3:
        score += 15
        
    # 健康状况
    if not has_health_check:
        score += 10
        
    # 精神压力
    if stress_level > 7:
        score += 15
    elif stress_level > 5:
        score += 10
        
    # 工作满意度
    if job_satisfaction < 5:
        score += 15
    elif job_satisfaction < 7:
        score += 10
        
    # 副业
    if not has_side_job:
        score += 5
        
    # 计算最终分数（0-100）
    final_score = min(100, score)
    
    # 显示结果
    st.subheader("您的牛马含量为：")
    st.progress(final_score / 100)
    st.write(f"{final_score}%")
    
    # 结果分析
    if final_score >= 80:
        st.error("您的生活工作状态非常'牛马'，建议及时调整！")
    elif final_score >= 60:
        st.warning("您的生活工作状态较为'牛马'，需要注意平衡。")
    else:
        st.success("您的生活工作状态相对健康，继续保持！")