import pandas as pd
import os

def fix_paths(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Fix the paths by adding the correct prefixes
    df['path'] = 'images/' + df['path'].str.replace('images/heatmaps/', '').str.replace('images/', '')
    df['path_prev'] = 'images/' + df['path_prev'].str.replace('images/heatmaps/', '').str.replace('images/', '')
    df['path_preprev'] = 'images/' + df['path_preprev'].str.replace('images/heatmaps/', '').str.replace('images/', '')
    df['path_gt'] = 'heatmaps/' + df['path_gt'].str.replace('images/heatmaps/', '').str.replace('heatmaps/', '')
    
    # Save the corrected file
    df.to_csv(output_file, index=False)
    print(f"Fixed paths saved to {output_file}")
    
    # Show first few rows
    print("\nFirst few rows:")
    print(df.head())

if __name__ == "__main__":
    # Fix training labels
    fix_paths('datasets/trackNet/labels_train_original.csv', 'datasets/trackNet/labels_train.csv')
    
    # Fix validation labels (copy from test)
    fix_paths('datasets/trackNet/labels_test.csv', 'datasets/trackNet/labels_val.csv')
