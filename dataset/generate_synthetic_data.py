import pandas as pd
import numpy as np

def generate_realistic_machine_data(num_records=1000, num_machines=100):
    data = []
    np.random.seed(42)  # For reproducibility

    for machine_id in range(1, num_machines + 1):
        base_temp = np.random.uniform(60, 75)  # Base temperature varies by machine
        temp_variance = np.random.uniform(5, 15)  # Temperature variation
        
        for _ in range(num_records // num_machines):
            # Generate temperature and runtime
            temperature = np.random.normal(base_temp, temp_variance)
            temperature = round(max(min(temperature, 100), 30), 2)  # Clamp between 30-100°C
            
            runtime = round(np.random.exponential(60), 2)
            runtime = min(runtime, 300)  # Cap at 300 hours
            
            # Calculate downtime probability
            temp_contribution = np.exp((temperature - 80) / 10) if temperature > 80 else 0
            runtime_contribution = np.exp((runtime - 200) / 50) if runtime > 200 else 0
            
            # Baseline probability + contributions + noise
            prob_downtime = (
                0.05 +  # Base probability
                0.5 * temp_contribution +  # Temperature contribution
                0.5 * runtime_contribution  # Runtime contribution
            )
            prob_downtime = min(prob_downtime + np.random.uniform(-0.02, 0.02), 1)  # Add small random noise
            
            # Determine downtime flag
            downtime = np.random.choice([0, 1], p=[1-prob_downtime, prob_downtime])
            
            # Append record
            data.append({
                'Machine_ID': f'MACH_{machine_id:03d}',
                'Temperature': temperature,
                'Run_Time': runtime,
                'Downtime_Flag': downtime,
                'Downtime_Probability': round(prob_downtime, 4)
            })
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    return df

# Generate the dataset
df_realistic = generate_realistic_machine_data()

# Save to CSV
df_realistic.to_csv('realistic_machine_downtime_data.csv', index=False)

print("Dataset generated and saved as 'realistic_machine_downtime_data.csv'.")
