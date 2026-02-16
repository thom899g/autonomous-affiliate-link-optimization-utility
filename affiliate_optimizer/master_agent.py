from typing import Dict, List, Optional
import logging
from .modules.data_collector import DataCollector
from .modules.performance_analyzer import PerformanceAnalyzer
from .modules.optimizer import Optimizer
from .modules.dashboard_connector import DashboardConnector

logger = logging.getLogger(__name__)

class MasterAgent:
    """The central controller for the affiliate optimization system.
    
    Attributes:
        data_collector: Handles data ingestion from multiple sources.
        performance_analyzer: Processes and evaluates performance metrics.
        optimizer: Designs and implements optimization strategies.
        dashboard_connector: Communicates with the monitoring dashboard.
    """
    
    def __init__(self):
        self.data_collector = DataCollector()
        self.performance_analyzer = PerformanceAnalyzer()
        self.optimizer = Optimizer()
        self.dashboard_connector = DashboardConnector()
        
    def run(self) -> None:
        """Orchestrates the optimization process."""
        try:
            data = self._collect_data()
            logger.info("Collected affiliate performance data.")
            
            metrics = self._analyze_performance(data)
            logger.info(f"Calculated performance metrics: {metrics}")
            
            strategies = self._generate_strategies(metrics)
            logger.info(f"Generated optimization strategies: {strategies}")
            
            self._apply_strategies(strategies)
            logger.info("Applied optimization strategies.")
            
            self._update_dashboard()
            logger.info("Updated dashboard with latest results.")
            
        except Exception as e:
            logger.error(f"Critical failure in master agent: {e}")
            raise
        
    def _collect_data(self) -> Dict[str, Dict]:
        """Collects raw affiliate performance data."""
        try:
            return self.data_collector.collect()
        except Exception as e:
            logger.warning(f"Data collection failed: {e}")
            raise
    
    def _analyze_performance(self, data: Dict[str, Dict]) -> Dict[str, float]:
        """Analyzes collected data to generate performance metrics."""
        try:
            return self.performance_analyzer.analyze(data)
        except Exception as e:
            logger.warning(f"Performance analysis failed: {e}")
            raise
    
    def _generate_strategies(self, metrics: Dict[str, float]) -> List[Dict]:
        """Generates optimization strategies based on performance metrics."""
        try:
            return self.optimizer.generate(metrics)
        except Exception as e:
            logger.warning(f"Strategy generation failed: {e}")
            raise
    
    def _apply_strategies(self, strategies: List[Dict]) -> None:
        """Applies generated optimization strategies."""
        try:
            self.optimizer.apply(strategies)
        except Exception as e:
            logger.error(f"Strategy application failed: {e}")
            raise
    
    def _update_dashboard(self) -> None:
        """Updates the dashboard with latest performance metrics and strategies."""
        try:
            self.dashboard_connector.update()
        except Exception as e:
            logger.warning(f"Dashboard update failed: {e}")