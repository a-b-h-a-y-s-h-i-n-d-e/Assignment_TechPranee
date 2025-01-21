import pandas as pd
import numpy as np

def generate_realistic_machine_data(num_records=1000, num_machines=100):
    data = []
    np.random.seed(42) 

    for machine_id in range(1, num_machines + 1):
        base_temp = np.random.uniform(60, 75)  
        temp_variance = np.random.uniform(5, 15) 
        
        for _ in range(num_records // num_machines):
            
            temperature = np.random.normal(base_temp, temp_variance)
            temperature = round(max(min(temperature, 100), 30), 2) 
            
            runtime = round(np.random.exponential(60), 2)
            runtime = min(runtime, 300)  
            
            
            temp_contribution = np.exp((temperature - 80) / 10) if temperature > 80 else 0
            runtime_contribution = np.exp((runtime - 200) / 50) if runtime > 200 else 0
            
            
            prob_downtime = (
                0.05 + 
                0.5 * temp_contribution + 
                0.5 * runtime_contribution  
            )
            prob_downtime = min(prob_downtime + np.random.uniform(-0.02, 0.02), 1) 
            
            
            downtime = np.random.choice([0, 1], p=[1-prob_downtime, prob_downtime])
            
            
            data.append({
                'Machine_ID': f'MACH_{machine_id:03d}',
                'Temperature': temperature,
                'Run_Time': runtime,
                'Downtime_Flag': downtime,
                
            })
    
    
    df = pd.DataFrame(data)
    return df


df_realistic = generate_realistic_machine_data()


df_realistic.to_csv('realistic_machine_downtime_data.csv', index=False)

print("Dataset generated and saved as 'realistic_machine_downtime_data.csv'.")
