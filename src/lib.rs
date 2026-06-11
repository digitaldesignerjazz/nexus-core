//! Nexus Hyperspace Core Library
//!
//! High-performance Rust components for:
//! - Mesh networking (NovaNet, QNET, Yggdrasil peer management)
//! - AI agent swarms & emotional evolution kernels
//! - Blockchain primitives (XCoin/QCoin integration)
//! - Grok Launcher egui dashboard backend
//! - Privacy (Tor/I2P ready abstractions)
//!
//! Hybrid architecture: Rust for perf-critical paths + Python for simulation/emotional layers.

pub mod config;
pub mod mesh;
pub mod agents;
pub mod crypto;
pub mod monitoring;

use tracing::info;

/// Initialize the core systems.
/// Loads config, starts tracing (already done in bin), prepares FFI/IPC bridges.
pub fn init() {
    info!("[lib] Nexus Core library initialized");
    // TODO: load default config, init crypto RNG, mesh runtime stubs
}

/// Version info for integration with Grok Launcher or other tools.
pub fn version() -> &'static str {
    env!("CARGO_PKG_VERSION")
}
