import pandas as pd
import os
import logging

# Configure logging
logging.basicConfig(
    filename='data_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def merge_csvs(input_dir='channel_data', output_file='merged_data.csv'):
    """Merge all channel CSVs into one file with source tracking"""
    try:
        all_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
        dfs = []

        for file in all_files:
            df = pd.read_csv(os.path.join(input_dir, file))
            df['source_channel'] = os.path.splitext(file)[0]  
            dfs.append(df)
            logging.info(f"Merged {len(df)} rows from {file}")

        merged_df = pd.concat(dfs, ignore_index=True)
        merged_df.to_csv(output_file, index=False)
        logging.info(f"Successfully merged {len(merged_df)} total records")
        
        return merged_df
    
    except Exception as e:
        logging.error(f"Merge failed: {str(e)}")
        raise

if __name__ == "__main__":
    merged_data = merge_csvs()