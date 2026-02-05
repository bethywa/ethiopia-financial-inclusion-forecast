import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Optional
from src.data.loader import DataLoader
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DataExplorer:
    """Explore the dataset"""
    
    def __init__(self, data_loader: DataLoader):
        self.data_loader = data_loader
        self.logger = get_logger(__name__)
    
    def get_summary(self) -> Dict[str, Any]:
        """Get basic summary of the dataset"""
        data = self.data_loader.load_unified_data()
        main_df = data["data"]
        
        summary = {
            "total_records": len(main_df),
            "record_types": main_df["record_type"].value_counts().to_dict(),
            "pillars": main_df["pillar"].value_counts().to_dict(),
            "unique_indicators": main_df["indicator_code"].nunique(),
            "date_range": {
                "min": main_df["observation_date"].min(),
                "max": main_df["observation_date"].max()
            }
        }
        
        return summary
    
    def plot_account_ownership_trend(self):
        """Plot account ownership over time"""
        data = self.data_loader.load_unified_data()
        main_df = data["data"]
        
        # Filter for account ownership observations
        acc_data = main_df[
            (main_df["record_type"] == "observation") &
            (main_df["indicator_code"] == "ACC_OWNERSHIP") &
            (main_df["gender"] == "all")
        ].copy()
        
        if len(acc_data) == 0:
            self.logger.warning("No account ownership data found")
            return
        
        # Sort by date
        acc_data["observation_date"] = pd.to_datetime(acc_data["observation_date"])
        acc_data = acc_data.sort_values("observation_date")
        
        # Plot
        plt.figure(figsize=(12, 6))
        plt.plot(acc_data["observation_date"], acc_data["value_numeric"], 
                marker='o', linewidth=2, markersize=8)
        
        plt.title("Ethiopia Account Ownership Trend (2011-2024)", fontsize=16)
        plt.xlabel("Year", fontsize=12)
        plt.ylabel("Account Ownership (%)", fontsize=12)
        plt.grid(True, alpha=0.3)
        
        # Add data labels
        for x, y in zip(acc_data["observation_date"], acc_data["value_numeric"]):
            plt.text(x, y + 1, f"{y}%", ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()
        
        return acc_data