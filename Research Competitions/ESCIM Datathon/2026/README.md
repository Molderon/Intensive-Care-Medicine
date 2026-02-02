> #  PReVENT2BI Study: Protective Ventilation to Prevent Secondary Brain Injury

## **Project Overview**
This repository contains the **ESICM Datathon 2026** submission from **Team Code2heal**, investigating the relationship between mechanical ventilation parameters and cerebral perfusion in traumatic brain injury (TBI) patients.

###  **Study Objective**
To assess the impact of airway pressure changes during mechanical ventilation on cerebral perfusion pressure (CPP) in TBI patients, with the goal of preventing secondary brain injury through optimized ventilation strategies.

### **🏥 Dataset**
- **Source**: AmsterdamUMC ICU Database
- **Patients**: 7,189 mechanically ventilated patients
- **Groups**: 
  - No TBI: 5,716 patients
  - TBI: 1,473 patients (with ICP measurements)
  - Detailed cohort: 279 patients with continuous CVP/ICP measurements (33,138 instances)

### **Methodology**
- **Retrospective analysis** of ICU patients with TBI
- **Machine Learning Approach**: Ensemble model using XGBoost, LightGBM, CatBoost, and Random Forest
- **Target Variables**: Prediction of Central Venous Pressure (CVP) and Intracranial Pressure (ICP)
- **Key Features**: PEEP, ΔPEEP, plateau pressure, I:E ratio, FiO₂, pCO₂, mechanical power parameters

### 📊 Model Results
The XGBoost-based ensemble model demonstrated excellent predictive performance:

#### Training Performance:
- **R² Score**: 0.9930
- **Mean Absolute Error (MAE)**: 0.0309
- **Root Mean Squared Error (RMSE)**: 0.2545

#### Test Performance:
- **R² Score**: 0.9954
- **MAE**: 0.0297
- **RMSE**: 0.2068

### **Key Findings**
1. **Feature Importance**: ΔPEEP and previous CVP measurements were the most influential predictors
2. **Clinical Insight**: Even small PEEP adjustments (1-3 cmH₂O) significantly affect CVP levels
3. **Brain-Lung Interaction**: Airway pressure changes directly influence cerebral venous drainage
4. **Personalized Ventilation**: The model enables prediction of individual patient responses to ventilation adjustments

### 🏆 ESICM Datathon 2026 Context
This project was developed for the **European Society of Intensive Care Medicine (ESICM) Datathon 2026**, which focuses on leveraging AI and machine learning to solve critical challenges in intensive care medicine, particularly in the domain of neurocritical care and ventilator management.

### 👥 Team Code2heal
An interdisciplinary team from:
- Medical University of Plovdiv, Bulgaria
- Technical University of Sofia, Plovdiv Branch, Bulgaria
- Center for Competence PERIMED-2, Plovdiv, Bulgaria
- Ege University, Izmir, Türkiye
- Kirikkale University, Türkiye
- Ufuk University, Ankara, Türkiye

### **Citation**
This work is based on the study: *"Protective ventilation to prevent secondary brain injury - PReVENT2BI study"* presented at ESICM Datathon 2026.

---
*For more details, refer to the complete abstract in `Team Code2heal - Abstract.pdf`*
