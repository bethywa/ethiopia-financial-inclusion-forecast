"""
Data enrichment module for adding new observations, events, and impact links
"""

import pandas as pd
from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path
import json

# Create a simple logger if not using the full one
class SimpleLogger:
    def __init__(self, name):
        self.name = name
    
    def info(self, msg):
        print(f"[INFO] {msg}")
    
    def warning(self, msg):
        print(f"[WARNING] {msg}")
    
    def error(self, msg):
        print(f"[ERROR] {msg}")

logger = SimpleLogger("DataEnricher")


class DataEnricher:
    """Class for enriching the dataset with new observations, events, and impact links"""
    
    def __init__(self):
        """
        Initialize DataEnricher
        """
        self.logger = logger
        self._enrichment_log: List[Dict[str, Any]] = []
        self._next_record_id = 1000  # Start high to avoid conflicts
    
    def _generate_record_id(self, prefix: str) -> str:
        """Generate a unique record ID"""
        self._next_record_id += 1
        return f"{prefix}_{self._next_record_id:04d}"
    
    def add_observation(
        self,
        pillar: str,
        indicator: str,
        indicator_code: str,
        value_numeric: float,
        observation_date: str,
        source_name: str,
        source_url: str,
        confidence: str = "medium",
        record_type: str = "observation",
        collected_by: Optional[str] = None,
        original_text: Optional[str] = None,
        notes: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Add a new observation record
        """
        observation = {
            "record_id": self._generate_record_id("REC"),
            "record_type": record_type,
            "pillar": pillar,
            "indicator": indicator,
            "indicator_code": indicator_code,
            "value_numeric": value_numeric,
            "observation_date": observation_date,
            "source_name": source_name,
            "source_url": source_url,
            "confidence": confidence,
            "collected_by": collected_by or "Your Name",
            "collection_date": datetime.now().strftime("%Y-%m-%d"),
            "original_text": original_text or "",
            "notes": notes or "",
            **kwargs
        }

        self._enrichment_log.append({
            "type": "observation",
            "data": observation,
            "timestamp": datetime.now().isoformat()
        })

        self.logger.info(f"✓ Added observation: {indicator_code} = {value_numeric} on {observation_date}")
        return observation
    
    def add_event(
        self,
        category: str,
        event_date: str,
        source_name: str,
        source_url: str,
        description: str,
        confidence: str = "medium",
        record_type: str = "event",
        collected_by: Optional[str] = None,
        original_text: Optional[str] = None,
        notes: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Add a new event record (pillar should be left empty)
        """
        event = {
            "record_id": self._generate_record_id("EVT"),
            "record_type": record_type,
            "category": category,
            "pillar": "",  # Events should have empty pillar
            "indicator": description,  # Use description as indicator
            "indicator_code": f"EVT_{category.upper()}_{self._next_record_id:04d}",
            "event_date": event_date,
            "observation_date": event_date,
            "source_name": source_name,
            "source_url": source_url,
            "confidence": confidence,
            "collected_by": collected_by or "Your Name",
            "collection_date": datetime.now().strftime("%Y-%m-%d"),
            "original_text": original_text or "",
            "notes": notes or "",
            **kwargs
        }

        self._enrichment_log.append({
            "type": "event",
            "data": event,
            "timestamp": datetime.now().isoformat()
        })

        self.logger.info(f"✓ Added event: {description} on {event_date}")
        return event
    
    def add_impact_link(
        self,
        parent_id: str,
        pillar: str,
        related_indicator: str,
        impact_direction: str,
        impact_magnitude: Optional[float] = None,
        lag_months: Optional[int] = None,
        evidence_basis: Optional[str] = None,
        confidence: str = "medium",
        collected_by: Optional[str] = None,
        notes: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Add a new impact link connecting an event to an indicator
        """
        impact_link = {
            "record_id": self._generate_record_id("IMP"),
            "parent_id": parent_id,
            "record_type": "impact_link",
            "pillar": pillar,
            "related_indicator": related_indicator,
            "impact_direction": impact_direction,
            "impact_magnitude": impact_magnitude,
            "lag_months": lag_months,
            "evidence_basis": evidence_basis,
            "confidence": confidence,
            "collected_by": collected_by or "Your Name",
            "collection_date": datetime.now().strftime("%Y-%m-%d"),
            "notes": notes or "",
            **kwargs
        }

        self._enrichment_log.append({
            "type": "impact_link",
            "data": impact_link,
            "timestamp": datetime.now().isoformat()
        })

        self.logger.info(f"✓ Added impact link: Event {parent_id} → {related_indicator}")
        return impact_link
    
    def merge_enrichments(
        self,
        original_data_path: Path,
        output_path: Optional[Path] = None
    ) -> Dict[str, pd.DataFrame]:
        """
        Merge new enrichments with existing data
        """
        self.logger.info("Merging enrichments with existing data...")
        
        # Load original data
        try:
            original_data = pd.read_excel(original_data_path, sheet_name="ethiopia_fi_unified_data")
            original_impact = pd.read_excel(original_data_path, sheet_name="Impact_sheet")
        except Exception as e:
            self.logger.error(f"Error loading original data: {e}")
            raise
        
        # Separate enrichments by type
        observations = []
        events = []
        impact_links = []
        
        for entry in self._enrichment_log:
            if entry["type"] == "observation":
                observations.append(entry["data"])
            elif entry["type"] == "event":
                events.append(entry["data"])
            elif entry["type"] == "impact_link":
                impact_links.append(entry["data"])
        
        # Convert to DataFrames
        new_obs_df = pd.DataFrame(observations) if observations else pd.DataFrame()
        new_events_df = pd.DataFrame(events) if events else pd.DataFrame()
        new_impact_df = pd.DataFrame(impact_links) if impact_links else pd.DataFrame()
        
        # Merge with original data
        merged_data = pd.concat([original_data, new_obs_df, new_events_df], ignore_index=True)
        merged_impact = pd.concat([original_impact, new_impact_df], ignore_index=True)
        
        self.logger.info(f"✓ Merged data: {len(merged_data)} total records")
        self.logger.info(f"✓ Merged impact links: {len(merged_impact)} total records")
        
        # Save if output path provided
        if output_path:
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                merged_data.to_excel(writer, sheet_name='data', index=False)
                merged_impact.to_excel(writer, sheet_name='impact_links', index=False)
            self.logger.info(f"✓ Saved enriched dataset to: {output_path}")
        
        return {
            "data": merged_data,
            "impact_links": merged_impact
        }
    
    def get_enrichment_log(self) -> List[Dict[str, Any]]:
        """Get the enrichment log"""
        return self._enrichment_log
    
    def clear_enrichment_log(self):
        """Clear the enrichment log"""
        self._enrichment_log.clear()
        self.logger.info("Enrichment log cleared")
    
    def save_enrichment_log(self, filepath: Path):
        """Save enrichment log to JSON file"""
        with open(filepath, 'w') as f:
            json.dump(self._enrichment_log, f, indent=2, default=str)
        self.logger.info(f"✓ Enrichment log saved to: {filepath}")