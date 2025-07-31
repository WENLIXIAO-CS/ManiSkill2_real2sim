"""
Global controller configuration store for passing config from training scripts to controllers.
"""
import numpy as np
from typing import Optional, Dict, Any


class ControllerConfigStore:
    """Singleton class to store and access controller configurations globally."""
    
    _instance = None
    _config = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def set_config(self, config: Dict[str, Any]):
        """Set the controller configuration."""
        self._config = config
    
    def get_config(self, key: str = None, default: Any = None):
        """Get configuration value by key, or entire config if key is None."""
        if self._config is None:
            return default
        
        if key is None:
            return self._config
        
        return self._config.get(key, default)
    
    def get_pose_clip_bounds(self):
        """Get pose clipping bounds with sensible defaults."""
        if self._config is None:
            # Return default bounds if no config is set
            raise ValueError("No controller config set")
        
        return {
            'pos_lower': np.array(self._config['clip_pos_lower']),
            'pos_upper': np.array(self._config['clip_pos_upper']),
            'rot_lower': np.array(self._config['clip_rot_lower']),
            'rot_upper': np.array(self._config['clip_rot_upper'])
        }


# Global instance
controller_config_store = ControllerConfigStore()