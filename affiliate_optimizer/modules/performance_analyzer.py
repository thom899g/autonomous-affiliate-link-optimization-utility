from typing import Dict, Optional
import logging
import pandas as pd

logger = logging.getLogger(__name__)

class PerformanceAnalyzer:
    """Analyzes performance metrics and generates insights."""
    
    def __init__(self):
        self.df = None  # DataFrame to store performance data
        
    def analyze(self, data: Dict[str, Dict]) -> Dict[str, float]:
        """Processes raw data and returns key performance metrics."""
        try:
            if not data:
                logger.warning("No data provided for analysis.")
                return {}
                
            self._process_data(data)
            metrics = self._calculate_metrics()
            
            return metrics
            
        except Exception as e:
            logger.error(f"Performance analysis failed: {e}")
            raise
    
    def _process_data(self, data: Dict[str, Dict]) -> None:
        """Converts raw data into a structured DataFrame."""
        try:
            df = pd