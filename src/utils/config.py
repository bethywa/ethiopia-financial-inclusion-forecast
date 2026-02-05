from pathlib import Path

class Config:
    """Configuration settings"""
    
    def __init__(self):
        # Project root
        self.project_root = Path(__file__).parent.parent.parent
        
        # Data paths
        self.data_raw = self.project_root / "data" / "raw"
        self.data_processed = self.project_root / "data" / "processed"
        
        # File paths
        self.unified_data_file = self.data_raw / "ethiopia_fi_unified_data.xlsx"
        
        # Create directories if they don't exist
        self.data_raw.mkdir(parents=True, exist_ok=True)
        self.data_processed.mkdir(parents=True, exist_ok=True)

config = Config()