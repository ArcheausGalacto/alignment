import numpy as np
import pandas as pd

# Function to calculate extremism with specified relationships
def calculate_extremism(df, weights):
    extremism = (
        weights['ingenuity_utility'] * (df['Ingenuity'] - df['Utility']) +
        weights['ingenuity_impact'] * (df['Ingenuity'] + df['Impact']) +
        weights['ingenuity_ethical'] * (df['Ingenuity'] + df['Ethical Risk']) +
        weights['ingenuity_feasibility'] * (df['Ingenuity'] + df['Technical Feasibility']) +
        weights['ingenuity_security'] * (df['Ingenuity'] + df['Security Risk']) +
        weights['ingenuity_environment'] * (df['Ingenuity'] + df['Environmental Impact']) +
        weights['ingenuity_perception'] * (df['Ingenuity'] - df['Public Perception']) +
        weights['impact_utility'] * (df['Impact'] - df['Utility']) +
        weights['ethical_utility'] * (df['Ethical Risk'] - df['Utility']) +
        weights['feasibility_utility'] * (df['Technical Feasibility'] - df['Utility']) +
        weights['security_utility'] * (df['Security Risk'] - df['Utility']) +
        weights['environment_utility'] * (df['Environmental Impact'] - df['Utility']) +
        weights['perception_utility'] * (-df['Public Perception'] - df['Utility']) +
        weights['ethical_impact'] * (df['Ethical Risk'] + df['Impact']) +
        weights['feasibility_impact'] * (df['Technical Feasibility'] + df['Impact']) +
        weights['security_impact'] * (df['Security Risk'] + df['Impact']) +
        weights['environment_impact'] * (df['Environmental Impact'] + df['Impact']) +
        weights['perception_impact'] * (-df['Public Perception'] + df['Impact']) +
        weights['feasibility_ethical'] * (df['Technical Feasibility'] + df['Ethical Risk']) +
        weights['security_ethical'] * (df['Security Risk'] + df['Ethical Risk']) +
        weights['environment_ethical'] * (df['Environmental Impact'] + df['Ethical Risk']) +
        weights['perception_ethical'] * (-df['Public Perception'] + df['Ethical Risk']) +
        weights['security_feasibility'] * (df['Security Risk'] + df['Technical Feasibility']) +
        weights['environment_feasibility'] * (df['Environmental Impact'] + df['Technical Feasibility']) +
        weights['perception_feasibility'] * (-df['Public Perception'] + df['Technical Feasibility']) +
        weights['environment_security'] * (df['Environmental Impact'] + df['Security Risk']) +
        weights['perception_security'] * (-df['Public Perception'] + df['Security Risk']) +
        weights['perception_environment'] * (-df['Public Perception'] + df['Environmental Impact'])
    )
    return extremism

# Define weights for extremism calculation
weights = {
    'ingenuity_utility': 500,
    'ingenuity_impact': 500,
    'ingenuity_ethical': 500,
    'ingenuity_feasibility': 500,
    'ingenuity_security': 500,
    'ingenuity_environment': 500,
    'ingenuity_perception': 500,
    'impact_utility': 500,
    'ethical_utility': 500,
    'feasibility_utility': 500,
    'security_utility': 500,
    'environment_utility': 500,
    'perception_utility': 500,
    'ethical_impact': 500,
    'feasibility_impact': 500,
    'security_impact': 500,
    'environment_impact': 500,
    'perception_impact': 500,
    'feasibility_ethical': 500,
    'security_ethical': 500,
    'environment_ethical': 500,
    'perception_ethical': 500,
    'security_feasibility': 500,
    'environment_feasibility': 500,
    'perception_feasibility': 500,
    'environment_security': 500,
    'perception_security': 500,
    'perception_environment': 500
}

# Define the conditions for maximal extremism
maximal_conditions = {
    'Ingenuity': 1.0,
    'Utility': 0.0,
    'Impact': 1.0,
    'Ethical Risk': 1.0,
    'Technical Feasibility': 1.0,
    'Security Risk': 1.0,
    'Environmental Impact': 1.0,
    'Public Perception': 0.0
}

# Create a DataFrame with the maximal conditions
df_maximal = pd.DataFrame([maximal_conditions])

# Calculate the maximal extremism score
maximal_extremism_score = calculate_extremism(df_maximal, weights).iloc[0]

print(f"Maximal Extremism Score: {maximal_extremism_score}")
