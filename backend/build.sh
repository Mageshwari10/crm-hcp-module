#!/bin/bash
set -e

# Set environment variables to prevent Cargo cache issues on read-only filesystems
export CARGO_NET_OFFLINE=false
export PIP_NO_CACHE_DIR=1
export RUSTFLAGS="-C target-dir=/tmp/target"

# Install Python dependencies with only pre-built wheels
pip install --upgrade pip
pip install --only-binary :all: --no-cache-dir -r requirements.txt

echo "Build completed successfully"
