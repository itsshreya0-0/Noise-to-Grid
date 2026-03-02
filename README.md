# Noise-to-Grid
Domain: Smart Cities and Urban Innovation
Urban noise pollution is wasted energy. This project uses piezoelectric sensor networks at high-decibel urban zones (airports, highways, construction sites) managed by an AI that predicts noise peaks and optimizes energy harvesting windows — feeding micro-generated power into local EV charging stations. Turns a pollution problem into a power asset.

## Problem
Indian urban centers are experiencing rapidly increasing noise pollution due to traffic congestion, airport activity, metro construction, and expanding infrastructure. Many high-density zones regularly exceed safe decibel limits, negatively impacting public health, productivity, and overall urban sustainability.

Current systems focus only on monitoring and regulating noise levels. However, NO mechanism exists to intelligently utilize this predictable, high-intensity acoustic energy present in urban hotspots.

At the same time, smart-city infrastructure such as EV charging stations, traffic sensors, and public safety systems requires distributed, low-scale, sustainable energy support.

The core problem is:

How can cities transform high-decibel urban noise zones from passive environmental liabilities into active, intelligently managed micro-energy assets that support smart infrastructure?

## Solution
AI-based predictive harvesting system that converts high-noise zones into micro-power for EV station auxiliary loads.

## Architecture
ESP32 → FastAPI → ML Model → Streamlit Dashboard

## How to Run
1. Train model
2. Start API
3. Run dashboard
