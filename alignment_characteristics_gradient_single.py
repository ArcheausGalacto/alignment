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

# Generate a synthetic dataset for a grid
def generate_grid_data(num_points=100):
    values = np.linspace(0, 1, num_points)
    grid_x, grid_y = np.meshgrid(values, values)
    return grid_x, grid_y

# Plot gradient for each relationship
def plot_relationship(grid_x, grid_y, extremism_grid, x_label, y_label, ax):
    c = ax.contourf(grid_x, grid_y, extremism_grid, cmap='viridis')
    ax.set_xlabel(x_label, fontsize=6)  # Adjust fontsize as needed for x-axis label
    ax.set_ylabel(y_label, fontsize=6)  # Adjust fontsize as needed for y-axis label
    ax.set_title(f'{x_label} vs. {y_label} with Extremism', fontsize=6)  # Adjust fontsize as needed for title
    return c

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

# Relationships to plot
relationships = [
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

# Plotting all relationships on a single page
fig, axes = plt.subplots(nrows=7, ncols=4, figsize=(12 * 0.6, 18 * 0.6))
axes = axes.flatten()

# Ensure all columns are present in the DataFrame
required_columns = [
    'Ingenuity', 'Utility', 'Impact', 'Ethical Risk', 'Technical Feasibility',
    'Security Risk', 'Environmental Impact', 'Public Perception'
]

for idx, (x_var, y_var) in enumerate(relationships):
    x_grid, y_grid = generate_grid_data()
    df_grid = pd.DataFrame({
        x_var: x_grid.flatten(),
        y_var: y_grid.flatten()
    })
    # Add missing columns with zeros
    for col in required_columns:
        if col not in df_grid:
            df_grid[col] = 0.0

    # Calculate extremism for the grid points
    df_grid['Extremism'] = calculate_extremism(df_grid, weights)

    # Normalize extremism to have values between 0 and 1
    df_grid['Extremism'] = (df_grid['Extremism'] - df_grid['Extremism'].min()) / (df_grid['Extremism'].max() - df_grid['Extremism'].min())

    # Reshape the extremism values back into a grid for plotting
    extremism_grid = df_grid['Extremism'].values.reshape(x_grid.shape)

    # Plot the relationship
    c = plot_relationship(x_grid, y_grid, extremism_grid, x_var, y_var, axes[idx])

fig.tight_layout()
fig.subplots_adjust(right=0.9)
cbar_ax = fig.add_axes([0.95, 0.15, 0.02, 0.7])
cbar = fig.colorbar(c, cax=cbar_ax)
cbar.ax.yaxis.set_label_position('left')
cbar.set_label('Extremism', labelpad=15, rotation=270)
plt.show()