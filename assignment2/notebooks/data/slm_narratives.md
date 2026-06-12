# SLM Clinical Narratives


## Llama-3.2-1B


### Patient 6 — predicted high (4.98s)

Prediction: HIGH
Main contributing factors: 
- SystolicBP = 140 mmHg (increases risk level)
- BS = 15.0 mmol/L (increases risk level)
- HeartRate = 90 bpm (increases risk level)

Rule-based support: 
- The patient's systolic blood pressure (SBP) is 140 mmHg, which is significantly higher than the predicted class threshold of 90 mmHg, indicating a high risk of cardiovascular complications.

Clinical interpretation: 
Given the patient's elevated systolic blood pressure and low blood sugar, along with a normal body temperature, the clinical picture suggests that the patient is at high risk of cardiovascular complications.

Safety note: 
- The patient's elevated blood pressure may require close monitoring and potential intervention to prevent further deterioration.


### Patient 5 — predicted mid (4.48s)

Prediction: 
The patient's predicted risk level is MID, indicating a moderate to high risk of cardiovascular disease.

Main contributing factors:
The patient's systolic blood pressure (130 mmHg) is a significant contributing factor, increasing the predicted risk level.

Rule-based support:
The patient's age (29 years) is also a contributing factor, increasing the predicted risk level.

Clinical interpretation:
The patient's elevated systolic blood pressure and age are both risk factors for cardiovascular disease. The patient's heart rate of 78 bpm is not a significant contributing factor in this context.

Safety note: The patient's blood sugar level of 7.8 mmol/L is not directly related to the predicted risk of cardiovascular disease.


### Patient 11 — predicted low (5.94s)

Prediction: 
The patient's predicted risk level is LOW, indicating a low likelihood of cardiovascular disease.

Main contributing factors: 
- Age 15 years: The patient is young, which is a risk factor for cardiovascular disease.
- SystolicBP 76 mmHg: Hypertension is a risk factor for cardiovascular disease.
- DiastolicBP 49 mmHg: Hypertension is a risk factor for cardiovascular disease.

Rule-based support: 
The patient's age and hypertension are matched with the low-risk rule, which states that if the patient is young, hypertension, and normal vital signs, the risk is low.

Clinical interpretation: 
Based on the evidence, the patient's risk of cardiovascular disease is low, and there is no indication of any other contributing factors. The patient's age and hypertension are not high enough to warrant further action.

Safety note: 
There are no safety concerns based on the provided evidence.


## Qwen3-1.7B


### Patient 6 — predicted high (12.44s)

Prediction: HIGH  
Main contributing factors: SystolicBP, BS, HeartRate  
Rule-based support: Multiple rules support high risk due to elevated BP and blood sugar levels  
Clinical interpretation: The patient has a high risk of maternal complications based on elevated blood pressure, blood sugar, and heart rate, which are strong predictors of adverse outcomes  
Safety note: Monitor for complications such as hypertensive crisis or hyperglycemic hyperosmolar nonketotic syndrome.


### Patient 5 — predicted mid (9.51s)

Prediction: MID (89% confidence)

Main contributing factors: SystolicBP, Age, HeartRate

Rule-based support: Age_adult, DBP_normal, SBP_elevated, Temp_normal → mid risk (54% confidence)

Clinical interpretation: The model predicts a mid-risk level based on elevated systolic blood pressure, age, and heart rate. These factors align with the rule-based association suggesting a mid-risk scenario.

Safety note: Monitor for complications of hypertension and consider interventions based on clinical guidelines.


### Patient 11 — predicted low (9.26s)

Prediction: LOW  
Main contributing factors: BS = 7.8 mmol/L, SystolicBP = 76 mmHg, DiastolicBP = 49 mmHg  
Rule-based support: Age_young, BS_high, SBP_normal, DBP_normal, Temp_normal are associated with low risk  
Clinical interpretation: The model predicts a low risk based on elevated blood sugar and blood pressure, despite normal temperature and heart rate  
Safety note: Monitor for potential complications in patients with diabetes and hypertension.


## Llama-3.2-3B


### Patient 6 — predicted high (13.25s)

Prediction: The patient is at HIGH risk for complications due to the combination of elevated systolic blood pressure, high blood sugar, and a normal body temperature.

Main contributing factors: The patient's age, blood pressure, and blood sugar levels are the primary factors contributing to this high risk classification.

Rule-based support: The clinical associations suggest that high blood pressure, high blood sugar, and a normal body temperature are indicative of a high-risk patient, as supported by the matched clinical association rules.

Clinical interpretation: The patient's elevated systolic blood pressure, high blood sugar, and normal body temperature, in combination, indicate a high-risk profile that warrants close monitoring and consideration of potential complications.

Safety note: The patient's high risk classification requires careful management to prevent potential complications, such as cardiovascular events or diabetic ketoacidosis, and prompt attention to their medical history and any underlying conditions.


### Patient 5 — predicted mid (21.09s)

Prediction: The patient is at a moderate risk of developing a cardiovascular event, with a predicted risk level of 89% and a confidence level of 89%.

Main contributing factors: The patient's systolic blood pressure (130 mmHg), age (29 years), and heart rate (78 bpm) are the primary factors contributing to this risk assessment.

Rule-based support: The patient's elevated systolic blood pressure and age, along with normal diastolic blood pressure and temperature, trigger the association rule "IF Age_adult, DBP_normal, SBP_elevated, Temp_normal THEN mid risk", which confers a moderate risk with a confidence level of 54% and a lift of 2.3.

Clinical interpretation: The patient's elevated systolic blood pressure, combined with their age and normal diastolic blood pressure, suggests that they may be at increased risk for cardiovascular events. However, the confidence level of 54% indicates that this risk is not extremely high.

Safety note: The patient's heart rate is within a normal range, which may help mitigate some of the risk associated with their elevated systolic blood pressure.


### Patient 11 — predicted low (16.26s)

Prediction: The patient is at a low risk for complications.

Main contributing factors: The patient's age, blood sugar level, and blood pressure are the key factors contributing to this prediction. Specifically, the patient's blood sugar level of 7.8 mmol/L and blood pressure of 76 mmHg and 49 mmHg are the most significant contributors.

Rule-based support: The patient's profile matches the conditions of two matched clinical association rules, which predict a low risk for complications when the patient is young, has a high blood sugar level, and normal blood pressure and temperature.

Clinical interpretation: The patient's low risk classification is based on the presence of a high blood sugar level and normal blood pressure, which is consistent with the patient's age. This suggests that the patient's current condition is not indicative of a significant health concern.

Safety note: The patient's low risk classification does not imply a complete absence of risk, and clinicians should continue to monitor the patient's condition closely.
