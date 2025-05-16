# ansible_lighthouse

Ansible role for deploying Lighthouse consensus or validator client

## Auto-generated

- [Defaults](#default-vars)
  - [lighthouse_beacon_datadir](#lighthouse_beacon_datadir)
  - [lighthouse_beacon_node_config](#lighthouse_beacon_node_config)
  - [lighthouse_beacon_node_custom_config](#lighthouse_beacon_node_custom_config)
  - [lighthouse_beacon_node_custom_options](#lighthouse_beacon_node_custom_options)
  - [lighthouse_beacon_service_name](#lighthouse_beacon_service_name)
  - [lighthouse_binary_download_url](#lighthouse_binary_download_url)
  - [lighthouse_binary_path](#lighthouse_binary_path)
  - [lighthouse_dir_base](#lighthouse_dir_base)
  - [lighthouse_dir_beacon](#lighthouse_dir_beacon)
  - [lighthouse_dir_binary](#lighthouse_dir_binary)
  - [lighthouse_dir_config](#lighthouse_dir_config)
  - [lighthouse_dir_data](#lighthouse_dir_data)
  - [lighthouse_dir_log](#lighthouse_dir_log)
  - [lighthouse_dir_secrets](#lighthouse_dir_secrets)
  - [lighthouse_dir_systemd](#lighthouse_dir_systemd)
  - [lighthouse_dir_validators](#lighthouse_dir_validators)
  - [lighthouse_download_url](#lighthouse_download_url)
  - [lighthouse_general_owner](#lighthouse_general_owner)
  - [lighthouse_group](#lighthouse_group)
  - [lighthouse_jwt_secret_path](#lighthouse_jwt_secret_path)
  - [lighthouse_mode](#lighthouse_mode)
  - [lighthouse_network](#lighthouse_network)
  - [lighthouse_reinstall](#lighthouse_reinstall)
  - [lighthouse_user](#lighthouse_user)
  - [lighthouse_validator_client_config](#lighthouse_validator_client_config)
  - [lighthouse_validator_client_custom_config](#lighthouse_validator_client_custom_config)
  - [lighthouse_validator_custom_options](#lighthouse_validator_custom_options)
  - [lighthouse_validator_service_name](#lighthouse_validator_service_name)
- [Tags](#tags)

- [Dependencies](#dependencies)

---

## Defaults

### lighthouse_beacon_datadir

Data directory for the beacon node.

### lighthouse_beacon_node_config

List of configuration options for the Lighthouse beacon node.

#### Defaults

```YAML
lighthouse_beacon_node_config:
  - name: network
    description: The network name
    value: '{{ lighthouse_network }}'
  - name: datadir
    description: Data directory for the beacon node
    value: '{{ lighthouse_dir_beacon }}'
  - name: execution-endpoint
    description: Execution client endpoint
    value: http://localhost:8551
  - name: execution-jwt
    description: Path to JWT secret file for authentication with execution client
    value: '{{ lighthouse_jwt_secret_path }}'
  - name: http
    description: Enable the HTTP API server
    value: true
  - name: http-address
    description: Address to bind the HTTP server to
    value: 127.0.0.1
  - name: http-port
    description: Port to bind the HTTP server to
    value: 5052
  - name: metrics
    description: Enable the Prometheus metrics HTTP server
    value: true
  - name: metrics-address
    description: Address to bind the metrics server to
    value: 127.0.0.1
  - name: metrics-port
    description: Port to bind the metrics server to
    value: 5054
  - name: listen-address
    description: Address to bind to for P2P traffic
    value: 0.0.0.0
  - name: port
    description: Port to bind to for P2P traffic (TCP/UDP)
    value: 9000
  - name: target-peers
    description: Target number of peers to connect to
    value: 50
  - name: logfile
    description: Log file path
    value: '{{ lighthouse_dir_log }}/beacon.log'
  - name: debug-level
    description: Logging level
    value: info
  - name: checkpoint-sync-url
    description: Checkpoint for fast sync
    value: https://sync-mainnet.beaconcha.in
```

### lighthouse_beacon_node_custom_config

Custom configuration options for the Lighthouse beacon node.

### lighthouse_beacon_node_custom_options

#### Defaults

```YAML
lighthouse_beacon_node_custom_options: []
```

### lighthouse_beacon_service_name

Systemd service name for Lighthouse beacon node.

#### Defaults

```YAML
lighthouse_beacon_service_name: lighthouse-beacon
```

### lighthouse_binary_download_url

#### Defaults

```YAML
lighthouse_binary_download_url:
  https://github.com/sigp/lighthouse/releases/download/v7.0.1/lighthouse-v7.0.1-x86_64-unknown-linux-gnu.tar.gz
```

### lighthouse_binary_path

Path to the Lighthouse binary.

#### Defaults

```YAML
lighthouse_binary_path: '{{ lighthouse_dir_binary }}/lighthouse'
```

### lighthouse_dir_base

Base directory for Lighthouse installation.

#### Defaults

```YAML
lighthouse_dir_base: /opt/lighthouse
```

### lighthouse_dir_beacon

#### Defaults

```YAML
lighthouse_dir_beacon: '{{ lighthouse_dir_data }}/beacon'
```

### lighthouse_dir_binary

Directory to install the Lighthouse binary.

#### Defaults

```YAML
lighthouse_dir_binary: /usr/local/bin
```

### lighthouse_dir_config

Directory for Lighthouse configuration files.

#### Defaults

```YAML
lighthouse_dir_config: '{{ lighthouse_dir_base }}/config'
```

### lighthouse_dir_data

Directory for Lighthouse data storage.

#### Defaults

```YAML
lighthouse_dir_data: '{{ lighthouse_dir_base }}/data'
```

### lighthouse_dir_log

Directory for Lighthouse log files.

#### Defaults

```YAML
lighthouse_dir_log: '{{ lighthouse_dir_base }}/logs'
```

### lighthouse_dir_secrets

Directory for validator secrets (only used in validator mode).

#### Defaults

```YAML
lighthouse_dir_secrets: '{{ lighthouse_dir_base }}/secrets'
```

### lighthouse_dir_systemd

Systemd service directory for Lighthouse.

#### Defaults

```YAML
lighthouse_dir_systemd: /lib/systemd/system
```

### lighthouse_dir_validators

Directory for validator keys (only used in validator mode).

#### Defaults

```YAML
lighthouse_dir_validators: '{{ lighthouse_dir_base }}/validators'
```

### lighthouse_download_url

URL to download the Lighthouse binary.

### lighthouse_general_owner

General owner for Lighthouse system files.

#### Defaults

```YAML
lighthouse_general_owner: root
```

### lighthouse_group

Group for running the Lighthouse node.

#### Defaults

```YAML
lighthouse_group: lighthouse
```

### lighthouse_jwt_secret_path

Path to the JWT secret for authentication with execution client.

#### Defaults

```YAML
lighthouse_jwt_secret_path: '{{ lighthouse_dir_config }}/jwt.hex'
```

### lighthouse_mode

Mode to run Lighthouse in (beacon or validator).

#### Defaults

```YAML
lighthouse_mode: beacon
```

### lighthouse_network

The network to connect to (mainnet, gnosis, chiado, sepolia, holesky).

#### Defaults

```YAML
lighthouse_network: mainnet
```

### lighthouse_reinstall

Force reinstall Lighthouse binary.

#### Defaults

```YAML
lighthouse_reinstall: false
```

### lighthouse_user

Username for the Lighthouse node.

#### Defaults

```YAML
lighthouse_user: lighthouse
```

### lighthouse_validator_client_config

List of configuration options for the Lighthouse validator client.

#### Defaults

```YAML
lighthouse_validator_client_config:
  - name: network
    description: The network name
    value: '{{ lighthouse_network }}'
  - name: datadir
    description: Data directory for the validator client
    value: '{{ lighthouse_validator_datadir }}'
  - name: beacon-nodes
    description: List of beacon nodes to connect to (comma-separated)
    value: http://localhost:5052
  - name: validators-dir
    description: Directory containing validator keystores and definitions
    value: '{{ lighthouse_dir_validators }}'
  - name: secrets-dir
    description: Directory containing validator keystore passwords
    value: '{{ lighthouse_dir_secrets }}'
  - name: metrics
    description: Enable the Prometheus metrics HTTP server
    value: true
  - name: metrics-address
    description: Address to bind the metrics server to
    value: 127.0.0.1
  - name: metrics-port
    description: Port to bind the metrics server to
    value: 5064
  - name: debug-level
    description: Logging level
    value: info
```

### lighthouse_validator_client_custom_config

Custom configuration options for the Lighthouse validator client.

### lighthouse_validator_custom_options

#### Defaults

```YAML
lighthouse_validator_custom_options: []
```

### lighthouse_validator_service_name

Systemd service name for Lighthouse validator client.

#### Defaults

```YAML
lighthouse_validator_service_name: lighthouse-validator
```

## Tags

**_lighthouse-config_**

**_lighthouse-install_**

**_lighthouse-prepare_**

## Dependencies

None.
