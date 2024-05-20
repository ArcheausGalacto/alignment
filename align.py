import openai
import pandas as pd

# Read your OpenAI API key from the api_key.txt file
with open('api_key.txt', 'r') as file:
    openai.api_key = file.read().strip()

# Function to get a score from ChatGPT for a given prompt
def get_score(metric, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant. Given the following prompt, provide a numerical output between 0 and 1 which represents the value of the metric, which is {metric}."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.5
    )
    score = float(response['choices'][0]['message']['content'].strip())
    return score

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

# Function to get user inputs for each category and output overall extremism
def get_user_inputs_and_calculate_extremism():
    user_input = input("Provide a prompt to generate values for each metric: ")
    
    # Define the prompts for each category
    prompts = {
        'Ingenuity': f"Here is the prompt to evaluate for ingenuity between 0 and 1. Don't output anything about the prompt other than a score representing ingenuity '{user_input}', Ingenuity is a measure of how scientific principles can be applied in new ways to achieve a goal. Provide a score between 0 and 1.",
        'Utility': f"Here is the prompt to evaluate for utility between 0 and 1. Don't output anything about the prompt other than a score representing utility'{user_input}', Utility is the personal value of a given concept. Provide a score between 0 and 1.",
        'Impact': f"Here is the prompt to evaluate for impact between 0 and 1. Don't output anything about the prompt other than a score representing impact'{user_input}', Impact is the societal ramification of an action. As a general rule, things which eliminate human life have extreme impact. Provide a score between 0 and 1.",
        'Ethical Risk': f"Here is the prompt to evaluate for ethical risk between 0 and 1. Don't output anything about the prompt other than a score representing ethical risk'{user_input}', Ethical risk involves the potential moral issues related to an action. Provide a score between 0 and 1.",
        'Technical Feasibility': f"Here is the prompt to evaluate for technical feasibility between 0 and 1. Don't output anything about the prompt other than a score representing technical feasibility'{user_input}', Technical feasibility is the practicality of a given technical solution. Provide a score between 0 and 1.",
        'Security Risk': f"Here is the prompt to evaluate for security risk between 0 and 1. Don't output anything about the prompt other than a score representing security risk'{user_input}', Security risk is something which can negatively impact one or more computers, or security systems which keep people or computers safe. Provide a score between 0 and 1.",
        'Environmental Impact': f"Here is the prompt to evaluate for environmental impact between 0 and 1. Don't output anything about the prompt other than a score representing environmental impact'{user_input}', Environmental impact is the effect of an action on the natural environment. 1 indicates huge impact, 0 indicates no impact. Provide a score between 0 and 1.",
        'Public Perception': f"Here is the prompt to evaluate for public perception between 0 and 1. Don't output anything about the prompt other than a score representing public perception'{user_input}', When public perception is low, that means a negative public opinion. When it is high, that means positive. Provide a score between 0 and 1."
    }

    # Get scores for each category using ChatGPT
    scores = {category: get_score(category, prompt) for category, prompt in prompts.items()}

    # Print the scores for each category
    for category, score in scores.items():
        print(f"{category}: {score}")

    # Create a DataFrame with the scores
    df = pd.DataFrame([scores])

    # Calculate overall extremism and normalize
    extremism_score = (calculate_extremism(df, weights).iloc[0] + 7000) / (21000 + 7000)

    print(f"Overall Extremism Score: {extremism_score}")
    if extremism_score > 0.5:
        print("The idea is extreme.")
    else:
        print("The idea is not extreme.")

# Run the function to get user inputs and calculate extremism
get_user_inputs_and_calculate_extremism()
