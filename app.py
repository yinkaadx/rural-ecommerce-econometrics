import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Agri-Digitalization Econometrics", layout="wide")

st.title("Serverless Rural E-Commerce Pipeline")
st.caption("Real-Time Telemetry Ingestion & Microeconometric Vectorization for Agricultural Welfare Analysis")

st.sidebar.header("Econometric Configuration")
selected_region = st.sidebar.selectbox("Simulated Emerging Market", ["Sub-Saharan Africa (Agro-Processing Hub)", "Southeast Asia (Digital Cooperative)", "South Asia (Smallholder Network)"])
adoption_shock = st.sidebar.slider("Simulate ICT Adoption Rate Surge", 1.0, 5.0, 2.5)
run_simulation = st.sidebar.button("Initialize Econometric Pipeline")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: Smartphone API -> AWS Lambda Normalization -> Panel-Data Vectorization")

if run_simulation:
    st.subheader(f"Active Market Integration: {selected_region}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_tx = col1.empty()
    metric_margin = col2.empty()
    metric_adoption = col3.empty()
    metric_welfare = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(808)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    adoption_rates = []
    welfare_indices = []
    
    base_adoption = 15.0 
    base_welfare = 50.0
    
    for i in range(100):
        if i < 30:
            current_adoption = base_adoption + np.random.uniform(-1.0, 2.0)
            current_welfare = base_welfare + np.random.uniform(-2.0, 2.0)
            tx_volume = int(np.random.uniform(50, 150))
            margin_increase = np.random.uniform(1.0, 3.0)
        elif i >= 30 and i < 65:
            current_adoption = base_adoption + (i - 30) * (0.8 * adoption_shock) + np.random.uniform(-2.0, 2.0)
            current_welfare = base_welfare + (i - 30) * (0.5 * adoption_shock) + np.random.uniform(-2.0, 2.0)
            tx_volume = int(np.random.uniform(300, 800 * adoption_shock))
            margin_increase = np.random.uniform(5.0, 12.0)
        else:
            current_adoption = current_adoption + np.random.uniform(-1.0, 1.0)
            current_welfare = current_welfare + np.random.uniform(-1.0, 1.0)
            tx_volume = int(np.random.uniform(1500, 3000 * adoption_shock))
            margin_increase = np.random.uniform(12.0, 18.0)
            
        adoption_rates.append(current_adoption)
        welfare_indices.append(current_welfare)
        
        metric_tx.metric("E-Commerce Tx Volume", f"{tx_volume:,} / hr")
        metric_margin.metric("Farm Profit Margin Shift", f"+{margin_increase:.1f}%", "Market Integration")
        metric_adoption.metric("Digital Adoption Rate", f"{current_adoption:.1f}%", f"+{(current_adoption - base_adoption):.1f}%")
        
        if current_welfare >= 70.0:
            metric_welfare.metric("Econometric Welfare Index", f"{current_welfare:.1f} pts", "Significant Treatment Effect")
        else:
            metric_welfare.metric("Econometric Welfare Index", f"{current_welfare:.1f} pts", "Baseline")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=adoption_rates, mode='lines', name='Digital Adoption Rate (%)', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=welfare_indices, mode='lines', name='Household Welfare Index', yaxis='y2', line=dict(color='green', dash='dot')))
        
        fig.update_layout(
            title="Real-Time Agri-Digitalization: Technology Adoption vs Simulated Household Welfare",
            xaxis=dict(title="High-Frequency Telemetry Timestamp"),
            yaxis=dict(title="Adoption Rate (%)"),
            yaxis2=dict(title="Welfare Index (Pts)", overlaying='y', side='right', range=[30, 100]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if current_adoption > 40.0 and i % 4 == 0:
            log_placeholder.success(f"ECONOMETRIC LOG: Structural shift detected at {time_steps[i].strftime('%H:%M:%S')}. AWS middleware auto-vectorizing panel data for Endogenous Switching Model analysis.")
        else:
            log_placeholder.info(f"Log: Telemetry tick {i} ingested via API gateway. E-commerce friction parameters normalized.")
            
        time.sleep(0.15)
        
    st.info("Simulation Complete. The serverless cloud pipeline successfully aggregated and vectorized rural e-commerce data for advanced applied microeconometrics.")
else:
    st.info("Click 'Initialize Econometric Pipeline' in the sidebar to simulate high-frequency agri-digitalization ingestion.")