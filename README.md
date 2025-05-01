# AI-Based Network Intrusion Detection System (NIDS)

## Overview
This project implements an AI-based NIDS using a Random Forest classifier trained on the UNSW-NB15 dataset, achieving 95.23% training accuracy and 98.71% testing accuracy. It features a FastAPI backend and React frontend, deployed locally.

## Features
- Random Forest model trained in Google Colab.
- FastAPI backend with `/predict` endpoint.
- React dashboard for sample predictions.
- Local deployment on macOS.


## Download Large Files
- `nids_model.pkl`: [Google Drive Link]
- `encoders.pkl`: [Google Drive Link]
- `UNSW_NB15_testing-set.csv`: [Google Drive Link]
- `UNSW_NB15_training-set.csv`: [Google Drive Link]
- Place `nids_model.pkl`, `encoders.pkl`, and `UNSW_NB15_*` in `NIDS/`.
- Place `UNSW_NB15_testing-set.csv` in `nids-dashboard/public/`.

## Setup
1. **Clone**:
   ```bash
   git clone https://github.com/bhusareprem/AI-based-NIDS.git
   cd AI-based-NIDS

   python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

cd nids-dashboard
npm install
npm start

Running
Backend: http://127.0.0.1:8000
Frontend: http://localhost:3000
Use the dashboard to predict samples.
License
MIT License.
