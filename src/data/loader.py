import pandas as pd
from pathlib import Path
from typing import Dict, Optional, Any
from src.utils.logger import get_logger
from src.utils.config import config

logger = get_logger(__name__)

class DataLoader:
    """Load the Ethiopia financial inclusion dataset"""
    
    def __init__(self):
        self.logger = get_logger(__name__)
    
    def load_unified_data(self) -> Dict[str, pd.DataFrame]:
        """
        Load the unified dataset from Excel file
        
        Returns:
            Dictionary with 'data' and 'impact_links' DataFrames
        """
        try:
            file_path = config.unified_data_file
            
            if not file_path.exists():
                raise FileNotFoundError(f"Data file not found: {file_path}")
            
            self.logger.info(f"Loading data from: {file_path}")
            
            # Load both sheets
            data_df = pd.read_excel(file_path, sheet_name="ethiopia_fi_unified_data")
            impact_links_df = pd.read_excel(file_path, sheet_name="Impact_sheet")
            
            self.logger.info(f"✓ Loaded {len(data_df)} rows in main sheet")
            self.logger.info(f"✓ Loaded {len(impact_links_df)} rows in impact links")
            
            # Display summary
            self.logger.info("\n=== Data Summary ===")
            self.logger.info(f"Observations: {len(data_df[data_df['record_type'] == 'observation'])}")
            self.logger.info(f"Events: {len(data_df[data_df['record_type'] == 'event'])}")
            self.logger.info(f"Targets: {len(data_df[data_df['record_type'] == 'target'])}")
            self.logger.info(f"Impact Links: {len(impact_links_df)}")
            
            return {
                "data": data_df,
                "impact_links": impact_links_df
            }
            
        except Exception as e:
            self.logger.error(f"Error loading data: {e}")
            raise
    
    def save_enriched_data(self, data_df: pd.DataFrame, impact_df: pd.DataFrame, 
                          filename: str = "enriched_data.xlsx"):
        """Save enriched data to Excel file"""
        output_path = config.data_processed / filename
        
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            data_df.to_excel(writer, sheet_name='data', index=False)
            impact_df.to_excel(writer, sheet_name='impact_links', index=False)
        
        self.logger.info(f"✓ Enriched data saved to: {output_path}")
        return output_path