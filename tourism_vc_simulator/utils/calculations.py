# # utils/calculations.py
# import math

# def calc_scenario_A(n, sick_pct, pct_vc, vc_fee, vc_cost, referral_rate=0.25):
#     """
#     Scenario A (Paid VC)
#     revenue = vc_fee * #vc_calls
#     cost_vc = vc_cost * #vc_calls
#     net_profit = revenue - cost_vc
#     """
#     sick_total = n * sick_pct

#     vc_calls = sick_total * pct_vc

#     revenue = vc_calls * vc_fee

#     cost_vc = vc_calls * vc_cost

#     net_profit = revenue - cost_vc

#     # referrals = vc_calls * referral_rate
#     total_op_visits = sick_total - vc_calls 
#     return {
#         "sick_total": sick_total,
#         "vc_calls": vc_calls,
#         "revenue": revenue,
#         "cost_vc": cost_vc,
#         "net_profit": net_profit,
#         # "referrals": referrals,
#         "Sick %" : sick_pct*100, 
#         "% VC Uptake": pct_vc*100, 
#         "VC Fee": vc_fee,
#         "total_op_visits": total_op_visits
#     }

# def calc_scenario_B(n, premium, emergency_premium, sick_pct, pct_vc, vc_cost, referral_rate=0.25):
#     """
#     Scenario B (Free VC)
#     revenue = premium * n
#     cost_vc = vc_cost * #vc_calls
#     cost_emergency = emergency_premium * n
#     net_profit = revenue - cost_emergency - cost_vc
#     """
#     revenue = n * premium
#     vc_calls = n * sick_pct * pct_vc

#     cost_vc = vc_calls * vc_cost
 
#     cost_emergency = n * emergency_premium

#     net_profit = revenue - cost_emergency - cost_vc
#     # referrals = vc_calls * referral_rate

#     total_op_visits = n * sick_pct - vc_calls 
#     return {
#         "sick_total": n * sick_pct,
#         "vc_calls": vc_calls,
#         "revenue": revenue,
#         "cost_vc": cost_vc,
#         "cost_emergency": cost_emergency,
#         "net_profit": net_profit,
#         "total_op_visits": total_op_visits, 

#         "Sick %" : sick_pct*100, 
#         "% VC Uptake": pct_vc*100, 
#         "EI Fee": emergency_premium,
#         "total_op_visits": total_op_visits



#     }

# # KPI calculators
# def compute_kpis_A(resA, n):
#     revenue = resA['revenue']
#     cost_vc = resA['cost_vc']
#     profit = resA['net_profit']
#     profit_margin = profit / revenue if revenue != 0 else None
#     per_tourist_rev = revenue / n
#     per_tourist_cost = cost_vc / n
#     breakeven_vc_fee = None
#     # breakeven fee given current calls = cost per call
#     if resA['vc_calls'] > 0:
#         breakeven_vc_fee = cost_vc / resA['vc_calls']
#     return {
#         "VC Calls": int(round(resA['vc_calls'])),
#         "Revenue (SAR)": revenue,
#         "VC Cost (SAR)": cost_vc,
#         "Net Profit (SAR)": profit,
#         "Profit Margin": (profit_margin * 100.0) if profit_margin is not None else 'n/a',
#         "Revenue per tourist (SAR)": per_tourist_rev,
#         "Cost per tourist (SAR)": per_tourist_cost,
#         "Break-even VC fee (SAR)": breakeven_vc_fee
#     }

# def compute_kpis_B(resB, n, premium):
#     revenue = resB['revenue']
#     cost_vc = resB['cost_vc']
#     cost_emerg = resB['cost_emergency']
#     profit = resB['net_profit']
#     profit_margin = profit / revenue if revenue != 0 else None
#     per_tourist_rev = revenue / n
#     per_tourist_cost = (cost_vc + cost_emerg) / n
#     pool_per_tourist = premium - (cost_emerg / n)
#     return {
#         "VC Calls": int(round(resB['vc_calls'])),
#         "Revenue (SAR)": revenue,
#         "VC Cost (SAR)": cost_vc,
#         "Emergency Cost (SAR)": cost_emerg,
#         "Net Profit (SAR)": profit,
#         "Profit Margin": (profit_margin * 100.0) if profit_margin is not None else 'n/a',
#         "Revenue per tourist (SAR)": per_tourist_rev,
#         "Cost per tourist (SAR)": per_tourist_cost,
#         "Pool per tourist (SAR)": pool_per_tourist
#     }

# utils/calculations.py
import math
import streamlit as st

@st.cache_data(show_spinner=False)
def calc_scenario_A(n, sick_pct, pct_vc, vc_fee, vc_cost, referral_rate=0.25):
    """
    Scenario A (Paid VC)
    revenue = vc_fee * #vc_calls
    cost_vc = vc_cost * #vc_calls
    net_profit = revenue - cost_vc
    """
    sick_total = n * sick_pct
    vc_calls = sick_total * pct_vc
    revenue = vc_calls * vc_fee
    cost_vc = vc_calls * vc_cost
    net_profit = revenue - cost_vc
    total_op_visits = sick_total - vc_calls 
    
    return {
        "sick_total": sick_total,
        "vc_calls": vc_calls,
        "revenue": revenue,
        "cost_vc": cost_vc,
        "net_profit": net_profit,
        "Sick %": sick_pct * 100, 
        "% VC Uptake": pct_vc * 100, 
        "VC Fee": vc_fee,
        "total_op_visits": total_op_visits
    }

@st.cache_data(show_spinner=False)
def calc_scenario_B(n, premium, emergency_premium, sick_pct, pct_vc, vc_cost, referral_rate=0.25):
    """
    Scenario B (Free VC)
    revenue = premium * n
    cost_vc = vc_cost * #vc_calls
    cost_emergency = emergency_premium * n
    net_profit = revenue - cost_emergency - cost_vc
    """
    revenue = n * premium
    vc_calls = n * sick_pct * pct_vc
    cost_vc = vc_calls * vc_cost
    cost_emergency = n * emergency_premium
    net_profit = revenue - cost_emergency - cost_vc
    total_op_visits = n * sick_pct - vc_calls 
    
    return {
        "sick_total": n * sick_pct,
        "vc_calls": vc_calls,
        "revenue": revenue,
        "cost_vc": cost_vc,
        "cost_emergency": cost_emergency,
        "net_profit": net_profit,
        "total_op_visits": total_op_visits, 
        "Sick %": sick_pct * 100, 
        "% VC Uptake": pct_vc * 100, 
        "EI Fee": emergency_premium,
        "total_op_visits": total_op_visits
    }

@st.cache_data(show_spinner=False)
def compute_kpis_A(resA, n):
    revenue = resA['revenue']
    cost_vc = resA['cost_vc']
    profit = resA['net_profit']
    profit_margin = (profit / revenue * 100.0) if revenue != 0 else 0
    per_tourist_rev = revenue / n
    per_tourist_cost = cost_vc / n
    
    breakeven_vc_fee = None
    if resA['vc_calls'] > 0:
        breakeven_vc_fee = cost_vc / resA['vc_calls']
    
    return {
        "VC Calls": int(round(resA['vc_calls'])),
        "Revenue (SAR)": revenue,
        "VC Cost (SAR)": cost_vc,
        "Net Profit (SAR)": profit,
        "Profit Margin": profit_margin,
        "Revenue per tourist (SAR)": per_tourist_rev,
        "Cost per tourist (SAR)": per_tourist_cost,
        "Break-even VC fee (SAR)": breakeven_vc_fee if breakeven_vc_fee else 'n/a'
    }

@st.cache_data(show_spinner=False)
def compute_kpis_B(resB, n, premium):
    revenue = resB['revenue']
    cost_vc = resB['cost_vc']
    cost_emerg = resB['cost_emergency']
    profit = resB['net_profit']
    profit_margin = (profit / revenue * 100.0) if revenue != 0 else 0
    per_tourist_rev = revenue / n
    per_tourist_cost = (cost_vc + cost_emerg) / n
    pool_per_tourist = premium - (cost_emerg / n)
    
    return {
        "VC Calls": int(round(resB['vc_calls'])),
        "Revenue (SAR)": revenue,
        "VC Cost (SAR)": cost_vc,
        "Emergency Cost (SAR)": cost_emerg,
        "Net Profit (SAR)": profit,
        "Profit Margin": profit_margin,
        "Revenue per tourist (SAR)": per_tourist_rev,
        "Cost per tourist (SAR)": per_tourist_cost,
        "Pool per tourist (SAR)": pool_per_tourist
    }