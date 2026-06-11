//! Configuration management for Nexus Core
//!
//! Supports TOML/JSON loading for mesh peers, agent params, crypto keys,
//! and integration settings with Python layers and Grok Launcher.

use serde::{Deserialize, Serialize};
use std::path::Path;

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct Config {
    pub mesh: MeshConfig,
    pub agents: AgentConfig,
    pub crypto: CryptoConfig,
    pub python_bridge: PythonBridgeConfig,
    pub monitoring: MonitoringConfig,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MeshConfig {
    pub yggdrasil_peers: Vec<String>,
    pub nova_net_enabled: bool,
    pub qnet_port: u16,
    pub peerlist_path: String,
}

impl Default for MeshConfig {
    fn default() -> Self {
        Self {
            yggdrasil_peers: vec!["[::]:0".to_string()],
            nova_net_enabled: true,
            qnet_port: 1776,
            peerlist_path: "mesh/peerlist.json".to_string(),
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AgentConfig {
    pub swarm_size: usize,
    pub emotional_evolution_rate: f64,
    pub genome_encoding: String, // "rust" | "python"
}

impl Default for AgentConfig {
    fn default() -> Self {
        Self {
            swarm_size: 42,
            emotional_evolution_rate: 0.618,
            genome_encoding: "rust".to_string(),
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct CryptoConfig {
    pub xcoin_enabled: bool,
    pub privacy_layer: String, // "tor" | "i2p" | "none"
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct PythonBridgeConfig {
    pub emotional_layer_script: String,
    pub use_ffi: bool, // future PyO3
    pub ipc_method: String, // "json" | "grpc"
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct MonitoringConfig {
    pub interval_secs: u64,
    pub self_healing: bool,
}

impl Config {
    pub fn from_file<P: AsRef<Path>>(path: P) -> Result<Self, Box<dyn std::error::Error>> {
        // TODO: implement toml or json loading with serde
        // For now return default
        Ok(Self::default())
    }

    pub fn save(&self, path: &Path) -> Result<(), Box<dyn std::error::Error>> {
        let content = serde_json::to_string_pretty(self)?;
        std::fs::write(path, content)?;
        Ok(())
    }
}
