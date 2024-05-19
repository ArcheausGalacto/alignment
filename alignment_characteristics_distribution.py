import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# Generate a synthetic dataset
def generate_synthetic_data(num_samples=400, random_seed=42):
    np.random.seed(random_seed)

    data = {
        'Ingenuity': np.random.uniform(0, 1, num_samples),
        'Utility': np.random.uniform(0, 1, num_samples),
        'Impact': np.random.uniform(0, 1, num_samples),
        'Ethical Risk': np.random.uniform(0, 1, num_samples),
        'Technical Feasibility': np.random.uniform(0, 1, num_samples),
        'Security Risk': np.random.uniform(0, 1, num_samples),
        'Environmental Impact': np.random.uniform(0, 1, num_samples),
        'Public Perception': np.random.uniform(0, 1, num_samples)
    }

    return pd.DataFrame(data)

# Generate data
df = generate_synthetic_data()

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

# Calculate extremism
df['Extremism'] = calculate_extremism(df, weights)

# Normalize extremism to have values between 0 and 1
df['Extremism'] = (df['Extremism'] - df['Extremism'].min()) / (df['Extremism'].max() - df['Extremism'].min())

# Function to plot relationships between two variables with extremism
def plot_relationships(df, var1, var2, extremism_col='Extremism'):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[var1], df[var2], c=df[extremism_col], cmap='viridis', alpha=0.8)
    plt.colorbar(label='Extremism')
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.title(f'{var1} vs. {var2} with Extremism')
    plt.show()

# List of variable pairs to plot
variable_pairs = [
    ('Ingenuity', 'Utility'),
    ('Ingenuity', 'Impact'),
    ('Ingenuity', 'Ethical Risk'),
    ('Ingenuity', 'Technical Feasibility'),
    ('Ingenuity', 'Security Risk'),
    ('Ingenuity', 'Environmental Impact'),
    ('Ingenuity', 'Public Perception'),
    ('Utility', 'Impact'),
    ('Utility', 'Ethical Risk'),
    ('Utility', 'Technical Feasibility'),
    ('Utility', 'Security Risk'),
    ('Utility', 'Environmental Impact'),
    ('Utility', 'Public Perception'),
    ('Impact', 'Ethical Risk'),
    ('Impact', 'Technical Feasibility'),
    ('Impact', 'Security Risk'),
    ('Impact', 'Environmental Impact'),
    ('Impact', 'Public Perception'),
    ('Ethical Risk', 'Technical Feasibility'),
    ('Ethical Risk', 'Security Risk'),
    ('Ethical Risk', 'Environmental Impact'),
    ('Ethical Risk', 'Public Perception'),
    ('Technical Feasibility', 'Security Risk'),
    ('Technical Feasibility', 'Environmental Impact'),
    ('Technical Feasibility', 'Public Perception'),
    ('Security Risk', 'Environmental Impact'),
    ('Security Risk', 'Public Perception'),
    ('Environmental Impact', 'Public Perception')
]

# Generate plots for each pair of variables
for var1, var2 in variable_pairs:
    plot_relationships(df, var1, var2)
