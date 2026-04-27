#!/bin/bash
set -e

# Set environment variables to prevent Cargo cache issues on read-only filesystems
export CARGO_NET_OFFLINE=true
export PIP_NO_CACHE_DIR=1
export RUSTFLAGS="-C target-dir=/tmp/target"

# Ensure we are in the backend directory
cd backend

# Install Python dependencies with only pre-built wheels to avoid building from source
pip install --upgrade pip
pip install --only-binary :all: --no-cache-dir -r requirements.txt

echo "Build completed successfully"
